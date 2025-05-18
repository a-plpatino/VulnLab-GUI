import webbrowser
import os
from lab_controllers.db_logger import guardar_payload

def render_payload(payload):
    guardar_payload(payload)  # ← REGISTRA

    ruta = os.path.join(os.path.dirname(__file__), "..", "sandbox", "preview.html")
    html = f"""
    <html>
    <head>
        <title>XSS Payload Preview</title>
        <style>
            body {{ font-family: Arial; background-color: #f5f5f5; padding: 50px; text-align: center; }}
            .payload-box {{ background: white; padding: 30px; border-radius: 10px;
                            box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h2 {{ color: #333; }}
        </style>
    </head>
    <body>
        <div class="payload-box">
            <h2>Payload en ejecución:</h2>
            <div>{payload}</div>
        </div>
    </body>
    </html>
    """
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open(ruta)
