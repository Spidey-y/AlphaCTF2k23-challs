import zipfile
import os

flag = [bin(ord(i))[2::].zfill(8) for i in "nuQypgylAmFvJD9X4LLcNfUPZqspwIPpM1zfUPZqspwIPpM1z1tDMUrbFDrNJxa3Xya9mI5vi5pTV9viIQC8YA7VvwvDRhUixfAkb1tDMUrbFDrNJxaa4X7ba2QVlEXr3UnB3psN00Qe2r3Xya9mI5vixfAkbdIdtSoh5KqQ33mlNqSYApoBwe74Y1v1lQTn7vxe9qadxdXpREjjT5Hj5ks7svMK5pTV9viIQC8YA7VvwvDRhUibs5vCYlcf8W3Xya9mI5vixfAkb3Xya9mI5vixfAkbM9vLLnVZS7zCaqKH8XwPUCb1EDrfDfUPZqspwIPpM1z1tDMUrbFDrNJxau0Qe2r3Xya9mI5vixfAkbdIdtSoh5LdUzmCPCNykfAlphaCTF{4_R3aL_hACK3R_knOWs_how_t0_SCRipT}OSUso99ieeYkKXQkIKMc8dVP1BJ7z8Ir9BrZqCNxTLrA0Qe2r3Xya9mI5vixfAkbdIdtSoh5pTV9viIQC8YA7VvwvDRhUinLZGi"][::-1]


with zipfile.ZipFile("flag.zip", "w") as zip_file:
    zip_file.write("hello_world.txt")

previous_zip = "flag.zip"

for binary_char in flag:
    if os.path.exists(binary_char + ".zip"):
        previous_zip = binary_char + ".zip"
        continue
    with zipfile.ZipFile(binary_char + ".zip", "w") as zip_file:
        zip_file.write(previous_zip)
    new_zip = binary_char + ".zip"
    with zipfile.ZipFile(new_zip, "w") as zip_file:
        zip_file.write(previous_zip)
    if os.path.exists(previous_zip):
        os.remove(previous_zip)
    previous_zip = new_zip
    
with zipfile.ZipFile("chall.zip", mode="w") as archive:    
        archive.write(f"{previous_zip}")