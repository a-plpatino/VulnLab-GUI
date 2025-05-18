import subprocess
import webbrowser
from tkinter import messagebox

def lanzar_dvwa():
    try:
        subprocess.run(["docker", "run", "-d", "-p", "8080:80", "vulnerables/web-dvwa"], check=True)
        webbrowser.open("http://localhost:8080")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "No se pudo iniciar DVWA. Verifica Docker.")
