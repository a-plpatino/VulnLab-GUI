# VulnLab GUI

VulnLab GUI es una aplicación educativa desarrollada en Python con customtkinter, que permite ejecutar y practicar vulnerabilidades web como XSS, SQL Injection y CSRF a través de una interfaz gráfica. Integra contenedores Docker para desplegar entornos como DVWA y laboratorios personalizados, y registra los payloads utilizados en una base de datos SQLite.

## Características
- Lanzamiento automático de DVWA con Docker.
- Simulador local de XSS con vista previa en navegador.
- Laboratorios en Flask vulnerables a XSS, SQLi y CSRF.
- Registro de todos los payloads utilizados en una base de datos.
- Visualización del historial desde la interfaz.
- Apertura directa del proyecto en Visual Studio Code.

## Requisitos
- Python 3.10+
- Docker
- Visual Studio Code
- pip (administrador de paquetes Python)

## Instalación
- pip install -r requirements.txt

## Estructura del proyecto
```
VULNLAB_GUI/
├── dockerfiles/
│   ├── csrf_lab/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── payloads.db
│   ├── custom_flask_lab/
│   │   ├── app.py
│   │   └── Dockerfile
│   └── sqli_lab/
│       ├── app.py
│       ├── Dockerfile
│       └── init_db.py
├── gui/
│   ├── home.py
│   ├── modules.py
│   └── __init__.py
├── lab_controllers/
│   ├── csrf_lab.py
│   ├── db_logger.py
│   ├── dvwa.py
│   ├── flask_lab.py
│   ├── sql_lab.py
│   ├── utils.py
│   ├── ver_logs.py
│   ├── xss_tester.py
│   └── __init__.py
├── labs_info/
│   └── vulnerabilities.json
├── sandbox/
│   ├── preview.html
│   └── preview_payload.py
├── docker-compose.yml
├── main.py
├── payloads.db
├── README.md
└── requirements.txt
```
## Ejecución

### Levantar los contenedores (DVWA, SQLi, CSRF, Flask Lab)
docker compose up -d

### Ejecutar la interfaz gráfica
python main.py

## Laboratorios Disponibles

| Laboratorio | Puerto | URL | Descripción |
| ------ | ------ | ------ | ------ |
| Flask | 5000 | http://localhost:5000 | Demostración de XSS |
| SQLi Lab | 5003 | http://localhost:5003 | Inyección SQL vulnerable |
| CSRF Lab | 5004 | http://localhost:5004 |  Cambio de contraseña vulnerable |
| DVWA | 8080 | http://localhost:8080 | Plataforma de pruebas múltiples |

## Ejemplo de uso
- Ejecutar main.py
- Usar la interfaz para:
    - Lanzar DVWA, Flask Lab, SQLi Lab, CSRF Lab
    - Probar un payload XSS
    - Ver historial de ataques
    - Abrir el proyecto en Visual Studio Code

## Herramientas utilizadas

Herramienta | Propósito |
| ------ | ------ |
| Python | Lenguaje base para lógica e interfaz |
| Flask | Framework web para los laboratorios |
| Docker + Compose | Contenedores para entornos vulnerables |
| SQLite | Almacenamiento local de payloads |
| CustomTkinter | Creación de interfaz gráfica moderna |
| VS Code | Editor de código con apertura desde GUI |

## Conclusiones
- VulnLab GUI proporciona un entorno seguro para aprender y practicar explotación de vulnerabilidades web.
- La separación por laboratorios permite estudiar casos concretos.
- El historial de pruebas refuerza el análisis posterior.