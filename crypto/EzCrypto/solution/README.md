# Ez Crypto

## Description

  > Eazy crypto challenge, just decrypt the flag and submit it.
  > [files](https://drive.google.com/drive/folders/1Q7oqKF0jwtSo_aKcHg4buhJMstHsYH71?usp=share_link)

## Write up
you can also solve it with some online tools
```python
with open("flag.txt", "r") as f:
    t = [*f.readline()]
    s = f.readline().split(" ")
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

```