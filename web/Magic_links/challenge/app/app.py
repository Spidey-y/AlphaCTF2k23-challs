from flask import Flask, request, render_template, redirect,  url_for, jsonify
import sqlite3
import uuid
import smtplib
from email.mime.text import MIMEText
import traceback
import os

app = Flask(__name__)

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email text, token text, role text)")
cursor.execute("INSERT INTO users (email, token, role) VALUES (?, ?, ?)", (os.environ['EMAIL_ADDRESS'], "v3ry_s3cr37_4dm1n_t0k3n_9547896", "admin"))
conn.commit()
conn.close()

@app.route("/")
def index():
    try:
        token = request.args.get("token")
        if not token:
            return redirect(url_for("magic"))
        user = get_user(token)
        if user:
            if user["role"] == "admin":
                return render_template("index.html",message=os.environ['FLAG'])
            if user["role"] == "user":
                return render_template("index.html",message=f"email: {user['email']}\nrole: {user['role']}")
            return redirect(url_for("magic"))
        return redirect(url_for("magic"))
    except:
        return jsonify({"status": "something went wrong :("})

@app.route("/magic", methods=["GET"])
def magic():
    return render_template("magic.html")

@app.route("/new", methods=["POST"])
def new():
    try:
        email = request.json.get("email")
        #make admin token static so it won't be changed on each payload
        if email == os.environ['EMAIL_ADDRESS']:
            token = "v3ry_s3cr37_4dm1n_t0k3n_9547896"
        else:
            token = str(uuid.uuid4())
            
        #the fkin port isnt included for some reason in this domain so hard code the bitch
        if "alphabit.club" in request.headers.get('Host'): 
            url = f"https://challenges.ctf.alphabit.club:1406?token={token}"
        else:
            url = f"https://{request.headers.get('Host')}?token={token}"
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email=?", (email,))
        res = cursor.fetchone()
        if res:
            cursor.execute("UPDATE users SET token= ? where id= ?", (token,res[0]))
        else:
            cursor.execute("INSERT INTO users (email, token, role) VALUES (?, ?, 'user')", (email, token))
        conn.commit()
        conn.close()
        success = send_email(email, "Your Magic Link", url)
        if success:
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "error"})
    except:
        return jsonify({"status": "something went wrong :("})

def get_user(token):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, role FROM users WHERE token=?", (token,))
    res = cursor.fetchone()
    conn.close()
    return {"email": res[0], "role": res[1]} if res else None

def send_email(to, subject, url):
    try: 
        gmail_user = os.environ['EMAIL_ADDRESS']
        gmail_password = os.environ["EMAIL_PASSWORD"]
        msg = MIMEText(f"Dear user,\nHere's your magic link:\n{url}")
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = to
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, msg.as_string())
        server.close()
        return True
    except:
        print (traceback.format_exc())
        return False
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
