from pwn import *
import time
import sys

def main():
    host = 'pwnalbe.kr'
    port = 9007

    r = remote(host, port)
    time.sleep(3)

    print r.recv()

    cnt = 0

    for i in range(100):
        r.recvuntil('N= ')
        n = int(r.recvuntil(' '))
        r.recvuntil('C= ')
        c = int(r.recv())

        print "N= {}, C= {}".format(n, c)

        src = 1
        des = n
        t = 0

        while(True):
            if(src > des):
                break

            message = ''

            for i in range(src, (src + des)/2 + 1):
                message += '{0} '.format(i)

            print "[-] set : {0}".format(message)

            r.sendline(message)
            result = r.recv()

            print "[*] result : {0}".format(result)

            if result.find('Correct') > -1:
                t = 1
                break
            elif result[0] == 'N':
                des = n
            elif result.find('error') > -1:
                break
            elif result.find('time') > -1:
                print "[!] time out!"
                sys.exit(1)
            elif int(result) % 10 != 0:
                des = (src + des)/2
            else:
                src = (src + des)/2 + 1

        if(t == 0):
            r.sendline(str(src))
            correctmsg = r.recv()

        cnt += 1
        print "[+] count : {0}\n".format(cnt)

    flag = r.recv()
    print "\n[*] FLAG : {0}".format(flag)

if __name__ == "__main__" :
    main()
