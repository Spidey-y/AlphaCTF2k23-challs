with open("flag.txt", "r") as f:
    t = [*f.readline()]
    m = f.readline().split(" ")
print(len(m))
i = 0
s = []
print(len(m))
while i<len(m):
    j = 0
    tmp = ""
    while j<8:
        i += 1
        if m[i-1] == "zero":
            tmp += "0"
        else:
            tmp += "1"
        j += 1
    s.append(tmp)

flag = [chr(int(i, 2)) for i in s]
allowed_chars = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-*{}"))
flag = [c for c in flag if c in allowed_chars]
for i in range(len(flag)):
    if flag[i] == "*":
        flag[i] = t.pop(0)
n = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
flag = ''.join(flag).split("-")
flag = [str(n.index(s.lower())) if s.lower() in n else s for s in flag]
flag = ''.join(flag)
print(flag)
#AlphaCTF{pAsswOrd_Is_bAsic_EnOugh_And_yOu_knOw_It_And_ItSAlphA_And_ItS_AlwAys_aLpHA_And_ThiS_iS_juST_A_pAddinG}
