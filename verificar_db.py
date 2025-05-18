# verificar_db.py
import sqlite3
import os

# Ruta a la base de datos
db_path = os.path.join(os.path.dirname(__file__), "payloads.db")

# Verifica si existe
if not os.path.exists(db_path):
    print("⚠️ No se encontró el archivo payloads.db")
else:
    # Conectar a la base y consultar datos
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registros ORDER BY fecha DESC")
    registros = cursor.fetchall()

    print("📋 Contenido de payloads.db:")
    for reg in registros:
        print(f"ID: {reg[0]} | Payload: {reg[1]} | Tipo: {reg[2]} | Fecha: {reg[3]}")

    conn.close()