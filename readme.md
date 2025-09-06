[![logo.png](https://i.postimg.cc/GtKtmZgL/logo.png)](https://postimg.cc/WqDT9fPC)
# Encriptador Web con FastAPI

Un servicio web simple y robusto para encriptar y desencriptar texto, construido con **FastAPI** y **Python**.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

---

## 📄 Tabla de Contenidos
- [Características](#-características)
- [Tecnologías Usadas](#-tecnologías-usadas)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Licencia](#-licencia)

---

## Características
- **Encriptación y Desencriptación:** Funcionalidad principal para proteger la confidencialidad de los textos.
- **Interfaz de Usuario (UI) Moderna:** Front-end elegante y responsivo, diseñado con **Bootstrap**.
- **API Robusta:** Construida sobre **FastAPI**, lo que garantiza alto rendimiento y documentación interactiva automática (Swagger UI).
- **Seguridad:** Utiliza la librería `cryptography` para una encriptación segura.
- **PWA** Para una flexibilidad en entornos android.


## Tecnologías Usadas
- **Backend:**
  - **FastAPI:** Framework web de alto rendimiento.
  - **Uvicorn:** Servidor ASGI para la aplicación.
  - **Python:** Lenguaje de programación principal.
  - **Cryptography:** Librería para encriptación y desencriptación.
- **Frontend:**
  - **HTML:** Estructura de la interfaz.
  - **CSS:** Estilos personalizados.
  - **JavaScript:** Lógica de la interfaz para interactuar con la API.
  - **Bootstrap:** Framework de CSS para el diseño.

## 🚀 Instalación

Sigue estos pasos para poner a funcionar el proyecto en tu máquina local.

1.  **Clona el repositorio:**
    ```bash
    git clone
    cd directorio
    ```
2.  **Crea un entorno virtual y actívalo:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install fastapi uvicorn cryptography
    ```
    *Para gestionar las dependencias de manera ordenada, puedes crear un archivo `requirements.txt` con el comando `pip freeze > requirements.txt`.*

## 💡 Uso

1.  **Inicia el servidor:**
    ```bash
    fastapi dev
    ```
2.  **Accede a la aplicación:**
    - Abre tu navegador y ve a [http://127.0.0.1:8000](http://127.0.0.1:8000) para usar la interfaz gráfica.
    - Para ver la documentación interactiva de la API (Swagger UI), visita [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Aplicacion desplegada en render:  [app-render+pwa](https://encriptador-desencriptador-fastapi.onrender.com)

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
