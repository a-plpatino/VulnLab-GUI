import sqlite3
from datetime import datetime
import os

DB_PATH = "/app/payloads.db"

def crear_tabla_si_no_existe():
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
    conn.commit()
    conn.close()

def guardar_payload(payload, tipo="XSS"):
    crear_tabla_si_no_existe()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (payload, tipo, fecha) VALUES (?, ?, ?)",
                   (payload, tipo, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

