import webbrowser
import os

def render_payload(payload):
    ruta = os.path.join(os.path.dirname(__file__), "preview.html")
    html = f"""
    <html>
        <head><title>Vista previa de Payload</title></head>
        <body>
            <h2>Payload en ejecución:</h2>
            <div>{payload}</div>
        </body>
    </html>
    """
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open(ruta)