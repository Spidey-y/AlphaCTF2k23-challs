# Magic Links

## Description

Why use passwords ? I created a service that you can use with just your email :D check it out, and if you have any feedback make sure to email me, i always check my inbox 

## Write up

After inspecting the page we see an endpoint `/new` it sends the host header + email after that we get an email of the host + token, the solution is to steal the admin token using your own server host for ex ngrok or webhook in the host header, and use the admin's email so when the admin clicks on the link you will get the token, use that token to get the flag: `AlphaCTF{g0tTA_watCH_7hE_H0$7_h34d3r}` 