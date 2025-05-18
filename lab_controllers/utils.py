import subprocess
from tkinter import messagebox

def abrir_vs_code():
    try:
        subprocess.run(["C:\\Users\\aplpatino\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", "."], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "VS Code no se pudo abrir. ¿Está bien instalado?")