# Todo App

Una aplicación simple de gestión de tareas desarrollada con Flask, SQLite y Bootstrap.

## 🚀 Características

- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Interfaz responsiva con Bootstrap
- ✅ Almacenamiento en SQLite
- ✅ API REST para tareas
- ✅ Contenedorización con Docker
- ✅ Pipelines de CI/CD con GitHub Actions

## 📋 Requisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### Desarrollo Local

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd proyecto2
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
python app.py
```

5. Abrir el navegador y acceder a:
```
http://localhost:5000
```

### Docker

1. Construir la imagen:
```bash
docker build -t todo-app .
```

2. Ejecutar el contenedor:
```bash
docker run -p 5000:5000 todo-app
```

## 🧪 Pruebas

Para ejecutar las pruebas:
```bash
pytest tests/ -v
```

## 📁 Estructura del Proyecto

```
proyecto2/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias de Python
├── Dockerfile         # Configuración de Docker
├── templates/         # Plantillas HTML
│   └── index.html    # Interfaz de usuario
├── tests/            # Pruebas unitarias
│   ├── __init__.py   # Inicializador del paquete
│   └── test_app.py   # Pruebas de la aplicación
├── .github/workflows/ # Pipelines de CI/CD
│   ├── test.yml      # Pipeline de pruebas
│   ├── lint.yml      # Pipeline de análisis de código
│   ├── build.yml     # Pipeline de construcción
│   └── actions.yml   # Acciones personalizadas
└── README.md         # Este archivo
```

## 🔄 Pipelines de CI/CD

### 1. **Test Pipeline** (`test.yml`)
- Ejecuta pruebas automáticamente
- Genera reporte de cobertura de código
- Se ejecuta en push a `main` y pull requests

### 2. **Lint Pipeline** (`lint.yml`)
- Verifica el estilo del código con `flake8`
- Verifica el formato con `black`
- Verifica imports con `isort`
- Se ejecuta en push a `main` y `develop`

### 3. **Build Pipeline** (`build.yml`)
- Construye imagen Docker
- Prueba que la aplicación funcione en contenedor
- Sube a Docker Hub (solo en `main`)

### 4. **Custom Actions** (`actions.yml`)
- Acciones manuales para información, pruebas y deploy
- Se ejecuta manualmente desde GitHub Actions

## 🛠️ Desarrollo

### Linting
```bash
flake8 app.py tests/
black app.py tests/
```

### Formateo automático
```bash
black app.py tests/
isort app.py tests/
```

## 📝 Uso

1. **Agregar tarea**: Completa el formulario y haz clic en el botón "+"
2. **Completar tarea**: Haz clic en el círculo verde junto a la tarea
3. **Eliminar tarea**: Haz clic en el botón de papelera
4. **API**: Accede a `/api/todos` para obtener JSON de todas las tareas

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. 