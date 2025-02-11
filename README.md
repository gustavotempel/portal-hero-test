# portal-hero-test

Este proyecto es una API desarrollada con FastAPI y SQLAlchemy, que permite procesar y sincronizar catálogos de productos desde archivos CSV con una base de datos PostgreSQL.

## Funcionalidades Principales:

- Importación y validación de archivos CSV.
- Inserción, actualización y eliminación de productos en la base de datos.
- Sincronización con portales externos.
- API para consultar productos.
- Logging detallado de las operaciones realizadas.
- Pruebas unitarias y de integración con pytest.


## Instalación y configuración:

Clonar el repositorio
```
git clone https://github.com/gustavotempel/portal-hero-test.git
```

Ingresar al repositorio:
```
cd portal-hero-test
```

Configurar el contenedor de la base de datos de la siguiente manera:
```
docker compose -f 'docker-compose.yml' up -d --build 'db'
```

Para iniciar la aplicación con Poetry:
```
poetry run uvicorn main:app --reload
```
Si no se cuenta con Poetry, se puede instalar en Mac y Linux con:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```
En Windows PowerShell con:
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

Si no se desea instalar Poetry, también se puede crear un entorno virtual e instalar las dependencias con pip, pero es necesario contar con Python 3.11
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Y luego iniciar la aplicación:
```
uvicorn main:app --reload
```
La API estará disponible en: http://127.0.0.1:8000

No se consideró utilizar un gestor de migraciones como Alembic ya que era una base de datos muy pequeña

## Estructura del proyecto:

```
📂 portal-hero-test
│   📂 app
│   │── 📂 api
│   │   ├── routes.py          # Rutas de la API
│   │── 📂 core
│   │   ├── database.py        # Configuración de la base de datos
│   │   ├── logger.py          # Configuración de logging
│   │── 📂 models
│   │   ├── product.py         # Modelo de Producto
│   │── 📂 services
│   │   ├── parser.py          # Procesamiento de CSV
│   │   ├── repository.py      # Operaciones con la base de datos
│   │   ├── sync.py            # Lógica de sincronización
│   │── 📂 utils
│   │   ├── file_reader.py     # Lectura de archivos CSV
│   │   ├── validators.py      # Validación de datos
│── 📂 tests
│   ├── 📂 unit
│   │   ├── test_csv.py            # Prueba de lectura de CSV
│   │   ├── test_models.py         # Prueba de creación de modelos
│   │   ├── test_repository.py     # Prueba de operaciones en DB
│   │   ├── test_sync.py           # Prueba de sincronización
│   │   ├── test_validators.py     # Prueba de validación
│   ├── 📂 integration
│   │   ├── test_api.py            # Pruebas de integración API
│   │   conftest.py            # Configuración para los tests
│── .gitignore             # Archivos ignorados por git
│── docker-compose.yaml    # Configuración de los contenedores
│── main.py                # Punto de entrada de la aplicación
│── pyproject.toml         # Configuración del proyecto
│── README.md              # Documentación
│── requirements.txt       # Dependencias del proyecto
```

## Uso la aplicación:

Importar productos del feed:
```
curl localhost:8000/products/ --form file=@./samples/feed_items.csv
```
Sincronizar productos de portales:
```
curl localhost:8000/sync/ --form file=@./samples/portal_items.csv
```
Consultar productos:
```
curl localhost:8000/products/
```

## Tests:

Para ejecutar los tests se puede hacer de la siguiente manera:
```
pytest tests
```
Y para tener un detalle de la cobertura de los tests:
```
coverage report -m
```