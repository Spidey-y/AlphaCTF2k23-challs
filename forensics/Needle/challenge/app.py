import sqlite3
import os
from flask import Flask, jsonify, request, g, Response

app = Flask(__name__)
app.database = "challenge.db"
FLAG = 'AlphaCTF{1_f0UND_th3_NeEDL3_yaY}'

def connect_db():
    return sqlite3.connect(app.database)

def init_db():
    with app.app_context():
        g.db = connect_db()
        g.db.execute("DROP TABLE IF EXISTS users")
        g.db.execute("""CREATE TABLE IF NOT EXISTS users (\n
        id INTEGER PRIMARY KEY AUTOINCREMENT,\n
        name TEXT UNIQUE NOT NULL,\n
        secret VARCHAR(32) NOT NULL)\n
        """)
        g.db.execute("DROP TABLE IF EXISTS messages")
        g.db.execute("""CREATE TABLE IF NOT EXISTS messages (\n
        id INTEGER PRIMARY KEY AUTOINCREMENT,\n
        message TEXT NOT NULL)\n
        """)
        g.db.execute(
            f"INSERT INTO users (id, name, secret) VALUES (1, 'fa2y', '{FLAG}')")
        g.db.commit()
        g.db.close()


init_db()

@app.route('/')
def index():
    return jsonify({'success': 'post message'})

@app.route('/message', methods=['POST'])
def message():
    if request.method == 'POST':
        g.db = connect_db()
        message = request.form['message']
        if message:
            try:
                g.db.execute(f"INSERT INTO messages (message) VALUES ('{message}')")
                g.db.commit()
            except Exception as e:
                return jsonify({'error': str(e)})
        g.db.close()
        return jsonify({'success': True})
    return jsonify({'success': False})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
