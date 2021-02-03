from pwn import *
 
p = remote("pwnable.kr",9007)
 
print(p.recv())
for j in range(100):
    print(p.recvuntil("N="))
    a = int(p.recvuntil(" "))                           
    print(p.recvuntil("C="))
    b = int(p.recvuntil("\n"))
    print(b)
 
    low = 0
    high = a
    cnt = 0
    while cnt != b :
        cnt = cnt + 1
        snd = ""
        mid = (low+high)/2
        for i in range(low,mid):
            snd += str(i)
            snd += " "
        snd += str(mid)
        print(snd)
        p.sendline(snd)
        a = int(p.recv())
        print(a)
        if a % 10 == 9 :
            high = mid
        else:
            low = mid + 1
 
    mid = (low+high)/2
    p.sendline(str(mid))
    print(str(mid))
    print(p.recv())
print(p.recv())
