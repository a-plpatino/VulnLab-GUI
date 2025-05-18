from flask import Flask, request
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

DB_PATH = "/app/payloads.db"

def registrar_evento_sql(payload):
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
                       (payload, "SQLi", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        print(f"💾 Guardado: {payload}")
    except Exception as e:
        print("Error al registrar evento SQLi:", e)

@app.route('/', methods=['GET', 'POST'])
def login():
    result = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        registrar_evento_sql(f"Usuario: {username} | Clave: {password}")

        conn = sqlite3.connect('vulnlab.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            result = f"<p class='success'>Bienvenido, {username}!</p>"
        else:
            result = "<p class='error'>Credenciales inválidas</p>"

    html = f"""
    <html>
    <head>
        <title>SQL Injection Demo</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; padding-top: 50px; }}
            .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 15px rgba(0,0,0,0.1); display: inline-block; }}
            input {{ display: block; width: 100%; margin-bottom: 10px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }}
            .success {{ color: green; }}
            .error {{ color: red; }}
            label {{ text-align: left; display: block; margin-bottom: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Login (vulnerable a SQL Injection)</h2>
            <form method='post'>
                <label>Usuario:</label>
                <input name='username'>
                <label>Clave:</label>
                <input name='password' type='password'>
                <input type='submit' value='Login'>
            </form>
            <div>{result}</div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
