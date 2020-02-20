# Comparación de rendimiento de pyro vs http

## Pyro

Iniciar el server con:

```
python pyro_server.py
```

Y ejecutar el cliente con timeit:

```
python -m timeit -n 10000 -s 'from pyro_client import main' 'main(1024)'
```

Se puede variar el tamaño del payload en el argumento a `main`.


## Flask

Hay varios archivos de configuración de gunicorn para probar distintas opciones.

Iniciar el servicio con gunicorn:

```
gunicorn -c gunicorn_<type>.conf flask_server:app
```

Ejecutar el cliente con timeit:

```
python -m timeit -n 10000 -s 'from flask_client import main' 'main(1024)'
```


## Fierro

Para probar contra fierro hay un `docker-compose-fierro.yml`.

Tienen que estar disponibles las imágenes `fierroserver:1.37.2` y `fierrocli:1.37.2`.

Hay que definir algunas variables en un archivo `.env`:

```
DB_NAME=<bb dd>
USER=<usuario fierro>
PASSWORD=<password fierro>
```


Luego se prueban los dos protocolos con:

```
docker-compose -f docker-compose-fierro.yml up client_pyro
```

y

```
docker-compose -f docker-compose-fierro.yml up client_http
```
