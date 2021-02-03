from pwn import * 
import re
import time
 
def compare(start, temp):
    comm = ""
    end = (start + temp) // 2
    global gcomm
    for i in range(start, end):
        comm += "{} ".format(i)
    if len(comm.split(" ")) == 2:
        while True:
            p.sendline(comm)
            tmp = p.recvline()
            if "10\n" in tmp:
                while True:
                    p.sendline(gcomm)
                    tmp = p.recvline()
                    if "Correct" in tmp:
                        return
                        break
            else:
                if "Correct" in tmp:
                    return
                    break
    p.sendline(comm)
    tmp = p.recvline()
    if "Correct" in tmp:
        return
    if tmp.endswith("9\n"):
        gcomm=comm.split(" ")[-2]
        compare(start, end+1)
    else:
        compare(end, temp)
 
np = re.compile("N=(\d+)")
cp = re.compile("C=(\d+)")
gcomm=""
 
p = remote("pwnable.kr",  9007)
tmp = p.recvline()
 
while tmp:
    print(tmp)
    if tmp.startswith("N="):
        n = int(np.search(tmp).group(1))
        c = int(cp.search(tmp).group(1))
        compare(0, n)
    tmp = p.recvline()
