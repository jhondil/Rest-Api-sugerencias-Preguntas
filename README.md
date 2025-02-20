# REST API Sugerencias de Preguntas

## Descripción
Esta API permite a los asesores recibir sugerencias automáticas basadas en preguntas frecuentes. Se implementan endpoints:
- **POST /suggest:** Recibe una consulta y devuelve una sugerencia.
- **GET /history:** Devuelve el historial de consultas.
- **POST /questions:** Permite agregar nuevas preguntas/respuestas (solo para rol admin).
#### AUTH
- **POST /login:** Autentica al usuario y retorna un token JWT.
- **POST users/register:**  Permite al administrador registrar nuevos usuarios.
- **GET users/:** Recupera la lista de usuarios registrados.

## Autenticación
Se utiliza JWT. Existen dos roles:
- **questionUser:** Puede solicitar sugerencias.
- **admin:** Puede gestionar la base de conocimiento.

## Cómo Correr el Proyecto


1. **Clonar el repositorio**
Abre una terminal y ejecuta: 
 ```bash
   git clone https://github.com/jhondil/Rest-Api-sugerencias-Preguntas.git
 ```

2. **Navegar al directorio del proyecto**
 ```bash
   cd Rest-Api-sugerencias-Preguntas
 ```
3. **Crear y activar el entorno virtual**

 ```bash
   python -m venv venv

En Windows:
venv\Scripts\activate

En Linux/macOS:
source venv/bin/activate
 ```

4. **Instalar Dependencias**  
   Asegúrate de tener Python 3.10 o superior instalado. Luego, instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar Variables de Entorno**  
   Cambia el archivo .env-example a .env en la raíz del proyecto y configura las variables
 ```bash
   SECRET_KEY =
    ALGORITHM = 
   ```

6. **Ejecutar la Aplicación**
Para correr la aplicación en modo desarrollo , ejecuta:
   ```bash
   fastapi dev ./app/main.py
```

La API estará disponible en:
http://localhost:8000/api/v1

La API Documentacion estará disponible en :
http://localhost:8000/docs#/


## Usuarios

#### Admin
username: admin /
Password: PasswordAdmin

#### questionUser
username: userQuestion /
Password: Password123!

## Docker
Si prefieres usar Docker:
   ```bash
   docker build -t mi_api_sugerencias .
```

Ejecuta el contenedor:
   ```bash
   docker run -d -p 8000:8000 mi_api_sugerencias

```
La API estará disponible en:
http://localhost:8000/api/v1

La API Documentacion estará disponible en :
http://localhost:8000/docs#/

## Pruebas/test
Para ejecutar las pruebas unitarias con pytest, desde la raíz del proyecto ejecuta:
   ```bash
pytest
```

## Proyecto desplegado
https://rest-api-sugerencias-preguntas.onrender.com/docs#/

## Tecnologías Utilizadas

- **Python 3.10+**  
  Lenguaje de programación empleado para desarrollar la API y sus módulos.

- **FastAPI**  
  Framework web moderno y de alto rendimiento para construir APIs. Facilita la validación de datos, la generación automática de documentación (Swagger/OpenAPI) y el manejo de peticiones asíncronas.

- **Uvicorn**  
  Servidor ASGI utilizado para ejecutar la aplicación FastAPI tanto en desarrollo como en producción.

- **PyJWT**  
  Biblioteca para la creación y validación de JSON Web Tokens (JWT), fundamental para la autenticación y autorización.

- **Pydantic**  
  Herramienta para la validación y serialización de datos mediante modelos, utilizada para definir los esquemas de entrada y salida de la API.

- **Docker**  
  Plataforma de contenerización que permite empaquetar la aplicación junto con todas sus dependencias, facilitando su despliegue en cualquier entorno.

- **pytest**  
  Framework de testing que facilita la organización y ejecución de pruebas unitarias en el proyecto.

- **python-dotenv**  
  Permite cargar variables de entorno desde un archivo `.env`, ayudando a gestionar configuraciones sensibles sin exponerlas directamente en el código.
