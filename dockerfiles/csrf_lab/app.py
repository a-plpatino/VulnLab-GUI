from flask import Flask, request
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

user_password = {"admin": "admin123"}

DB_PATH = "/app/payloads.db"

def registrar_evento_csrf(payload):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payload TEXT NOT NULL,
                tipo TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
        """)
        cursor.execute("INSERT INTO registros (payload, tipo, fecha) VALUES (?, ?, ?)",
                       (payload, "CSRF", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error al registrar evento CSRF:", e)

@app.route('/')
def profile():
    return f"""
    <html>
    <head>
        <title>CSRF Lab</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                text-align: center;
                padding-top: 50px;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                display: inline-block;
                min-width: 350px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 90%;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            h2 {{ color: #333; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Perfil de usuario</h2>
            <p><strong>Usuario:</strong> admin</p>
            <p><strong>Contraseña actual:</strong> <b>{user_password['admin']}</b></p>
            <form method="POST" action="/cambiar">
                <label>Nueva contraseña:</label><br>
                <input name="newpass" type="text"><br>
                <input type="submit" value="Cambiar contraseña">
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/cambiar', methods=['POST'])
def cambiar():
    global user_password
    newpass = request.form.get("newpass", "")
    user_password["admin"] = newpass

    registrar_evento_csrf(f"Nueva contraseña: {newpass}")

    return f"""
        <html>
        <body style='font-family: Arial; text-align: center; padding-top: 50px;'>
            <p style='color:green;'>✅ Contraseña cambiada a: <b>{newpass}</b></p>
            <a href='/'>🔙 Volver al perfil</a>
        </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)



