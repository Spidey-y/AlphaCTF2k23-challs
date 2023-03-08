# SoS

## Description

Call the ambulance, but not for me ... no, but actually you should look for some help :)

## Write up

this challenge was inspired by vvxhid docs challs in both AlphaCTF2k22 and Hackini 2.0, the first step is to look at `/docs` we find an endpoint named `/g1mm3-fl4g` which is accessible only with a valid auth<br>
we make a request but this time the flag isn't there, instead we get 
> You do not have access to this endpoint :(
>
let's check our cookies, we find a cookie named auth, inside it we find what seems like a base64 encoded string, but it's reversed (= comes last in base64)<br>
>=EzMgAzMgEzMgAzMgAzMgEzMgEzMgAzMgAjMgEzMgEzMgAzMgAzMgEzMgEzMgEzMgAzMgAjMgAzMgAzMgEzMgEzMgAzMgEzMgEzMgAzMgAjMgEzMgAzMgAzMgAzMgAzMgEzMgEzMgAzMgAjMgAzMgEzMgEzMgAzMgAzMgAzMgEzMgAzMgAjMgEzMgAzMgEzMgEzMgEzMgEzMgAzMgAzMgAjMgAzMgEzMgAzMgAzMgEzMgEzMgEzMgAzMgAjMgEzMgEzMgAzMgAzMgEzMgEzMgAzMgAzMgAjMgEzMgEzMgAzMgEzMgAzMgEzMgEzMgAzMgAjMgEzMgEzMgAzMgAzMgAzMgEzMgEzMgAzMgAjMgEzMgAzMgAzMgAzMgAzMgEzMgEzMgAzMgAjMgAzMgAzMgAzMgEzMgAzMgEzMgEzMgAzM
>
let's used cyberchef and decode the base64 after reversing it<br>
>30 31 31 30 31 30 30 30 20 30 31 31 30 30 30 30 31 20 30 31 31 30 30 30 31 31 20 30 31 31 30 31 30 31 31 20 30 30 31 31 30 30 31 31 20 30 31 31 31 30 30 31 30 20 30 30 31 31 31 31 30 31 20 30 31 30 30 30 31 31 30 20 30 31 31 30 30 30 30 31 20 30 31 31 30 31 31 30 30 20 30 31 31 31 30 30 31 31 20 30 31 31 30 30 31 30 31
>
we'll get a hex, again let's use cyberchef<br>
>01101000 01100001 01100011 01101011 00110011 01110010 00111101 01000110 01100001 01101100 01110011 01100101
>
after that we get a binary and finally after converting it to char we find:
>hack3r=False
>
lets set it to `True` and encode it like it was, and there you go: `AlphaCTF{1_3a7_c00ki35_f0r_br34kf45t}`