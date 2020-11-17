# Python 3.8-slim (Debian buster-slim based)
FROM python:3.8-slim

# Se indica mantenedor de la imagen
MAINTAINER Carlos Morales <carlos7ma@correo.ugr.es>

# Creación de usuario con permisos básicos
RUN useradd -ms /bin/bash medauth \
	&& mkdir -p app/test \
	&& chown medauth /app/test

# Se configura para utilizarse el usuario creado
USER medauth

# Se configura el directorio de trabajo
WORKDIR /app/test

# Se copia el fichero de requisitos de paquetes pip
COPY requirements.txt .

# Instalación de los requisitos y se borra el fichero tras la instalación
RUN pip install -r requirements.txt --no-warn-script-location \
	&& rm requirements.txt


# Se configura el PATH para ejecutar paquetes de Pip
ENV PATH=/home/medauth/.local/bin:$PATH

# Ejecución
CMD ["invoke", "tests"]
