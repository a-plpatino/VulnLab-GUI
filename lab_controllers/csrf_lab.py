import subprocess
import webbrowser

def lanzar_csrf_lab():
    try:
        subprocess.run(["docker", "compose", "up", "-d", "csrf_lab"], check=True)
        webbrowser.open("http://localhost:5004")
    except subprocess.CalledProcessError as e:
        print("Error al lanzar CSRF Lab:", e)
