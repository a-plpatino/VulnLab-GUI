import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import os

def ver_historial():
    def cargar_datos(filtro):
        # Limpia la tabla
        for i in tree.get_children():
            tree.delete(i)

        # Consulta según filtro
        if filtro == "Todos":
            cursor.execute("SELECT payload, tipo, fecha FROM registros ORDER BY fecha DESC")
        else:
            cursor.execute("SELECT payload, tipo, fecha FROM registros WHERE tipo = ? ORDER BY fecha DESC", (filtro,))

        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)

    def borrar_registros():
        if messagebox.askyesno("Confirmar", "¿Estás seguro de borrar todos los registros?"):
            cursor.execute("DELETE FROM registros")
            conn.commit()
            cargar_datos(filtro_var.get())

    ventana = tk.Tk()
    ventana.title("Historial de Payloads")
    ventana.geometry("700x350")

    filtro_var = tk.StringVar(value="Todos")

    frame_filtros = tk.Frame(ventana)
    frame_filtros.pack(pady=10)

    tk.Label(frame_filtros, text="Filtrar por tipo:").pack(side=tk.LEFT)

    opciones = ["Todos", "XSS", "SQLi", "CSRF"]
    combo = ttk.Combobox(frame_filtros, textvariable=filtro_var, values=opciones, state="readonly", width=10)
    combo.pack(side=tk.LEFT, padx=5)

    btn_borrar = tk.Button(frame_filtros, text="Borrar historial", command=borrar_registros, bg="red", fg="white")
    btn_borrar.pack(side=tk.LEFT, padx=10)

    tree = ttk.Treeview(ventana, columns=("payload", "tipo", "fecha"), show="headings")
    tree.heading("payload", text="Payload")
    tree.heading("tipo", text="Tipo")
    tree.heading("fecha", text="Fecha y Hora")
    tree.column("payload", width=350)
    tree.column("tipo", width=80)
    tree.column("fecha", width=150)

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    db_path = os.path.join(os.path.dirname(__file__), "..", "payloads.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Carga inicial
    cargar_datos(filtro_var.get())

    # Evento al cambiar filtro
    combo.bind("<<ComboboxSelected>>", lambda e: cargar_datos(filtro_var.get()))

    ventana.mainloop()

