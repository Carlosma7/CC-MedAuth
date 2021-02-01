### Contenedores

#### Contenedores propuestos

El cluster sigue la siguiente composición:

![Cluster](../img/cluster_compose.png "Cluster")

Por lo que cabe señalar los siguientes contendores:

* **API MedAuth**: Contendrá la API del proyecto y sus fuentes.
* **MongoDB**: BD no relacional donde se almacenará la información del proyecto.
* **Client**: Contendrá el [cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/client.py) del proyecto y se quedará ejecutándose en segundo plano para poder realizar llamadas a la API.

#### API MedAuth

Se puede ver el [Dockerfile](https://github.com/Carlosma7/MedAuth/blob/main/Dockerfile.despliegue), el cual copia todos los fuentes del proyecto, los requisitos y el fichero de tareas de *Invoke*, haciendo uso de un fichero [.dockerignore](https://github.com/Carlosma7/MedAuth/blob/main/Dockerfile.despliegue.dockerignore). Esta imagen toma de base una imagen oficial vista anteriormente en el proyecto, que contiene *Python* ya instalado y se trata de una imagen ligera y con los requisitos necesarios, como se vió para el contenedor de tests del proyecto.

```Dockerfile
# Python 3.8-slim (Debian buster-slim based)

FROM python:3.8-slim

# Se indica mantenedor de la imagen

LABEL maintainer="Carlos Morales <carlos7ma@correo.ugr.es>"

# Se etiqueta la imagen para almacenarla en Github Container Registry

LABEL org.opencontainers.image.source https://github.com/carlosma7/medauth

# Etiquetas relativas a la imagen creada

LABEL build-date="21/10/2020"

LABEL description="Medical Authorization Project on Python3.8-slim debian based docker."

LABEL github.url="https://github.com/Carlosma7/MedAuth"

LABEL version="1.0.0"

# Se configura el PATH para ejecutar paquetes de Pip

ENV PATH=/home/medauth/.local/bin:$PATH

# Creación de usuario con permisos básicos

RUN useradd -ms /bin/bash medauth \

&& mkdir -p app/test \

&& chown medauth /app/test

# Se configura para utilizarse el usuario creado

USER medauth

# Se configura el directorio de trabajo

WORKDIR /app/test

# Se copia el fichero de requisitos de paquetes pip

COPY . .

# Instalación de los requisitos y se borra el fichero tras la instalación

RUN pip install -r requirements.txt --no-warn-script-location \

&& rm requirements.txt

# Abrir puerto 2020

EXPOSE 2020

# Ejecución

CMD ["invoke", "execute"]
```

Dentro de este contenedor se contendrán los fuentes del proyecto y se lanzará la API en el puerto *2020*, haciendo uso del host *0.0.0.0*. Este contenedor lanza con *hypercorn* el servidor como un servicio *ASGI*:

```
hypercorn src/core/main.py --bind '0.0.0.0:2020'
```

Este contenedor a su vez, realiza una conexión con una base de datos no relacional de **MongoDB**, dentro del fichero [controlador.py](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py), obteniendo de las variables de entorno los valores que conforman la ruta de conexión a la BD, o utilizando ```mongodb://localhost:27017/medauthdb``` como configuración por defecto en caso de no encontrar dichas variables de entorno.

Este contenedor puede trabajar de forma independiente ya que está preparado para trabajar tanto con una BD local como con otro contenedor mediante composición (como se verá más adelante). En su defecto, si no existe una BD de **MongoDB** disponible, utiliza un almacenamiento local, lo que permite funcionar también de forma aislada este contenedor.

#### MongoDB

Para definir este contenedor se utilizará una [imagen oficial de *Docker Hub*](https://hub.docker.com/_/mongo), el cual define una base de datos de *MongoDB 4.4.2*, con una base de datos con nombre *medauthdb* y que opera sobre el puerto estándar de *MongoDB*, siendo este el *27017*.

Se puede ver la configuración y parametrización de esta imagen en el [fichero de composición](https://github.com/Carlosma7/MedAuth/blob/main/docker-compose.yml):

```YAML
  mongodb:
    image: mongo:4.4.2
    container_name: mongodb
    restart: unless-stopped
    environment:
      MONGO_INITDB_DATABASE: medauthdb
      MONGODB_DATA_DIR: /data/db
      MONDODB_LOG_DIR: /dev/null
    ports:
      - 27017:27017
    networks:
      - app-tier
```

#### Client

Se puede ver el [Dockerfile](https://github.com/Carlosma7/MedAuth/blob/main/Dockerfile.cliente), el cual copia el fichero [client.py](https://github.com/Carlosma7/MedAuth/blob/main/src/client.py), el cual realiza las funciones de cliente de la API del proyecto, además de instalar la librería [requests](https://requests.readthedocs.io/en/master/) de *Python*, con la que el cliente realiza las diferentes peticiones.

Al igual que el contenedor de despliegue y el contenedor de pruebas del proyecto, utiliza la imagen ```python:3.8-slim```, ya que es ligera y trae integrado *Python*, por lo que resulta ideal si queremos un contenedor para el cliente.

```Dockerfile
# Python 3.8-slim (Debian buster-slim based)

FROM python:3.8-slim

# Se indica mantenedor de la imagen

LABEL maintainer="Carlos Morales <carlos7ma@correo.ugr.es>"

# Se etiqueta la imagen para almacenarla en Github Container Registry

LABEL org.opencontainers.image.source https://github.com/carlosma7/medauth

# Etiquetas relativas a la imagen creada

LABEL build-date="21/10/2020"

LABEL description="Medical Authorization Project on Python3.8-slim debian based docker."

LABEL github.url="https://github.com/Carlosma7/MedAuth"

LABEL version="1.0.0"

# Se configura el PATH para ejecutar paquetes de Pip

ENV PATH=/home/medauth/.local/bin:$PATH

# Creación de usuario con permisos básicos

RUN useradd -ms /bin/bash medauth \

&& mkdir -p app/test \

&& chown medauth /app/test

# Se configura para utilizarse el usuario creado

USER medauth

# Se configura el directorio de trabajo

WORKDIR /app/test

# Se copia el fichero de requisitos de paquetes pip

COPY src/client.py .

# Instalación de los requisitos y se borra el fichero tras la instalación

RUN pip install requests

# Ejecución

CMD ["python"]
```

Este contenedor, al igual que el contenedor de despliegue de la API, obtiene las variables de conexión (en este caso respecto al contenedor de la API) mediante variables de entorno, o en su defecto utiliza la ruta ```http://0.0.0.0:2020```, ya que son los parámetros por defecto de la API.

