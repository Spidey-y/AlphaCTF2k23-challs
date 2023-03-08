s= 20446037080787585380305433513438247156953335672653876543881076870948658039962177284513724087519288276722382
#AlphaCTF{GG_Y0Ur3_4_Cryp7o_L3G3Nd_Go_Submit}
def bin2str(l):
    s = ''.join(l)
    f = []
    while s:
        f.append(s[:8])
        s = s[8:]
    flag = []
    for i in f:
        flag.append(chr(int(i,2)))
    return ''.join(flag)

def decrypt(s,m):
    flag=[]
    for i in m:
        if (s>=i):
            flag.append('1')
            s -= i
        else:
            flag.append('0')
    return list(reversed(flag))
    

def public_key(num):
    m=[2]
    x = 2
    j = 1
    while True:
        x = 2 * x + 1
        m.append(x)
        j+=1
        if ((num-x) < 0):
            return list(reversed(m))
        

m = public_key(s)
bf = decrypt(s,m)
flag = bin2str(bf)
print(f"flag: {flag}")
