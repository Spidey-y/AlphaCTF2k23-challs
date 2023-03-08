from flask import Flask, request,jsonify
from base64 import b64decode,b64encode


app = Flask(__name__)

@app.route("/docs")
def documentation():
  documentation = {
    "endpoints": {
      "/docs": {
        "description": "Returns the documentation for all endpoints of our amazing, super 'secure' and well built API!",
        "methods": ["GET"]
      },
      "/g1mm3-fl4g": {
        "description": "A special gift. Only accessible with a valid auth.",
        "methods": ["GET"]
      }
    }
  }
  return jsonify(documentation)


def encrypt(string):
  binary = " ".join([bin(ord(i))[2::].zfill(8) for i in string])
  hex_string = " ".join([hex(ord(i))[2::] for i in binary])
  return b64encode(hex_string.encode("utf-8")).decode("utf-8")[::-1]


def decrypt(encrypted_string):
  base64_string = b64decode(encrypted_string[::-1].encode("utf-8")).decode("utf-8").replace(" ", "")
  hex = [base64_string[i:i+2] for i in range(0,len("".join([chr(int(i,16)) for i in base64_string])),2)]
  return "".join([chr(int(i,2)) for i in "".join([chr(int(i,16)) for i in hex]).split(" ")])


@app.route("/g1mm3-fl4g")
def reveal_flag():
  try:
    hacker_cookie = request.cookies.get("auth")
    if hacker_cookie and decrypt(hacker_cookie).lower() == "hack3r=true":
      return jsonify({"very good Hack3r":"AlphaCTF{1_3a7_c00ki35_f0r_br34kf45t}"})
    else:
      return jsonify({"error":"You do not have access to this endpoint :("})
  except:
    return jsonify({"error":"Something went wrong :("})


@app.route("/")
def home():
  response = jsonify({"message":"Welcome visitor! Enjoy your stay :)"})
  response.set_cookie("auth", encrypt("hack3r=False"))
  return response


if __name__ == "__main__":
  app.run(host='0.0.0.0')
