# Python 3.8-slim (Debian buster-slim based)
FROM python:3.8-slim

MAINTAINER Carlos Morales <carlos7ma@correo.ugr.es>

# Creación de usuario con permisos básicos
RUN useradd -ms /bin/bash medauth

# Se configura para utilizarse el usuario creado
USER medauth

# Se configura el directorio de trabajo
WORKDIR /home/medauth

# Se copia el repositorio ignorando la información indicada en .dockerignore
COPY . .

# Instalación de los requisitos y se borra el fichero tras la instalación
RUN pip install -r requirements.txt --no-warn-script-location \
	&& rm requirements.txt

# Se configura el PATH para ejecutar paquetes de Pip
ENV PATH=/home/medauth/.local/bin:$PATH

CMD ["invoke", "tests"]
