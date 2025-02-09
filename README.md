# portal-hero-test

# Development steps:

Inicializar proyecto con Poetry (permite gestionar dependencias y entornos virtuales):
```
poetry init
```

Se agrega base de datos en contenedor Docker. Se ejecuta con docker-compose de la siguiente manera:
```
docker compose -f 'docker-compose.yml' up -d --build 'db'
```