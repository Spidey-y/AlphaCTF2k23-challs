# {secret_png}

## Write-up

The challenge is a simple xor between a PNG image and a key. 

As known, png is a compressed image format contain a header with distinctive "signature" byte sequence, allowing programs to recognize the file as a PNG image regardless of its name files, to recover the key you need to xor the file bytes with each printable character then compare it to the original header, if they match then append it to the key. 

After finding the key, xor it again with the file attached , the result is a PNG image containing the flag . 

Attached you'll find a python script demonstrating solution .
