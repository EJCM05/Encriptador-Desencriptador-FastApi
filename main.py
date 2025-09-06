from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# ... (el resto de las importaciones que ya tenías)
from pydantic import BaseModel
from cryptography.fernet import Fernet
import os

# Inicializar la aplicación
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    title="Encriptador con FastAPI",
    description="Una API para encriptar y desencriptar texto de manera segura."
)

# Configurar los directorios para archivos estáticos y templates
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory="templates")

# ... (el código de la clave Fernet que ya tenías)
KEY_FILE = "secret.key"

if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

f = Fernet(key)

# Modelo de datos para la entrada de la API
class Data(BaseModel):
    text: str

# Endpoint para servir el HTML
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ... (tus endpoints de /encrypt y /decrypt van aquí, sin cambios)
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