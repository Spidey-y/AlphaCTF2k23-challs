# ZipFile

## Description

Grab a cup of coffee, it will take you so long to reach the secret :) but aren't you a hacker ? prove me wrong and show me your hacking skills

## Write up

Unzip, read the char, till the end:
```
import zipfile
import os


flag = ""
r = zipfile.ZipFile("chall.zip", "r")
r.extractall()
current_zip = r.namelist()[0]

try:
    while True:
        with zipfile.ZipFile(current_zip, "r") as zip_file:
            zip_file.extractall()
            os.remove(current_zip)
            flag += chr(int(os.path.basename(current_zip).split(".zip")[0], 2))
            file_inside = os.path.splitext(zip_file.namelist()[0])[0]
            current_zip = os.path.join(os.getcwd(), file_inside)+".zip"
except:
    print(flag[flag.index("AlphaCTF"):flag.index("}")+1:])
```
flag: `AlphaCTF{4_R3aL_hACK3R_knOWs_how_t0_SCRipT}`