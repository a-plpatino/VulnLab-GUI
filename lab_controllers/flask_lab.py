import subprocess
import webbrowser

def lanzar_flask_lab():
    try:
        # Ejecuta Docker Compose para levantar el contenedor
        subprocess.run(["docker", "compose", "up", "-d", "flasklab"], check=True)

        # Abre el navegador con el laboratorio Flask
        webbrowser.open("http://localhost:5000/?name=<script>alert('XSS')</script>")
    except subprocess.CalledProcessError as e:
        print("Error al lanzar el laboratorio Flask con Docker Compose:", e)