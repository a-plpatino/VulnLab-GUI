import customtkinter as ctk
from lab_controllers.dvwa import lanzar_dvwa
from lab_controllers.utils import abrir_vs_code
from lab_controllers.xss_tester import render_payload
from lab_controllers.flask_lab import lanzar_flask_lab
from lab_controllers.sql_lab import lanzar_sql_lab
from lab_controllers.csrf_lab import lanzar_csrf_lab
from lab_controllers.ver_logs import ver_historial

def launch_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("VulnLab GUI - Laboratorio de Vulnerabilidades")
    app.geometry("750x750")

    ctk.CTkLabel(app, text="VulnLab GUI", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
    ctk.CTkLabel(app, text="Explora y practica vulnerabilidades como XSS, SQLi, CSRF, y más.").pack()

    ctk.CTkButton(app, text="Lanzar DVWA", command=lanzar_dvwa).pack(pady=10)
    ctk.CTkButton(app, text="Lanzar Flask Lab", command=lanzar_flask_lab).pack(pady=10)
    ctk.CTkButton(app, text="Lanzar SQLi Lab", command=lanzar_sql_lab).pack(pady=10)
    ctk.CTkButton(app, text="Lanzar CSRF Lab", command=lanzar_csrf_lab).pack(pady=10)
    ctk.CTkButton(app, text="Ver Historial", command=ver_historial).pack(pady=10)
    
    # --- NUEVA SECCIÓN DE PRUEBA DE XSS ---
    ctk.CTkLabel(app, text="\n Prueba tu Payload XSS", font=ctk.CTkFont(size=20, weight="bold")).pack()

    entrada_payload = ctk.CTkTextbox(app, width=600, height=120)
    entrada_payload.pack(pady=5)
    entrada_payload.insert("0.0", "<script>alert('XSS')</script>")  # Valor por defecto

    status_label = ctk.CTkLabel(app, text="", text_color="white")
    status_label.pack(pady=5)

    def probar_payload():
        payload = entrada_payload.get("1.0", "end").strip()
        if payload:
            render_payload(payload)
            status_label.configure(text="Payload enviado al navegador.", text_color="green")
        else:
            status_label.configure(text=" Escribe un payload para probar.", text_color="orange")

    ctk.CTkButton(app, text="Probar Payload", command=probar_payload).pack(pady=10)
    ctk.CTkButton(app, text="Abrir Código en VS Code", command=abrir_vs_code).pack(pady=10)

    app.mainloop()