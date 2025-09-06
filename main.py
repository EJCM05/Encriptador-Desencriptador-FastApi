import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    title="Encriptador con FastAPI",
    description="Una API para encriptar y desencriptar texto de manera segura."
)

# Configurar los directorios para archivos estáticos y templates
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Lógica para manejar la clave de cifrado
key = os.environ.get("SECRET_KEY")

if key:
    f = Fernet(key.encode())
else:
    KEY_FILE = "secret.key"
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
            f = Fernet(key)
    else:
        # Esto solo debería ocurrir en un entorno local si la clave no existe
        print("ADVERTENCIA: La variable de entorno 'SECRET_KEY' no está configurada y 'secret.key' no existe. Se generará una clave temporal.")
        key = Fernet.generate_key()
        f = Fernet(key)
        # Opcionalmente, guardar la clave temporal para no generar una nueva en cada reinicio
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

# Modelo de datos para la entrada de la API
class Data(BaseModel):
    text: str

# Endpoint para servir el HTML
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return FileResponse(os.path.join(BASE_DIR, "templates", "index.html"))

# Endpoint para servir el Service Worker
@app.get("/service-worker.js", response_class=HTMLResponse)
def read_root(request: Request):
    return FileResponse(os.path.join(BASE_DIR, "service-worker.js"))

# Endpoints de la API para encriptar y desencriptar
@app.post("/encrypt/")
def encrypt_text(data: Data):
    encrypted_text = f.encrypt(data.text.encode())
    return {"encrypted_text": encrypted_text.decode('utf-8')}

@app.post("/decrypt/")
def decrypt_text(data: Data):
    try:
        decrypted_text = f.decrypt(data.text.encode())
        return {"decrypted_text": decrypted_text.decode('utf-8')}
    except Exception as e:
        return {"error": "El texto no puede ser desencriptado, revisa el formato."}
