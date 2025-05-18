import subprocess
import webbrowser

def lanzar_sql_lab():
    try:
        subprocess.run(["docker", "compose", "up", "-d", "sqli_lab"], check=True)
        webbrowser.open("http://localhost:5003")
    except subprocess.CalledProcessError as e:
        print("Error al lanzar SQLi Lab:", e)