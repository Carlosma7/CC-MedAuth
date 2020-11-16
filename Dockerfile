# Python 3.8-slim (Debian buster-slim based)
FROM python:3.8-slim

MAINTAINER Carlos Morales <carlos7ma@correo.ugr.es>

# Creación de usuario con permisos básicos
RUN useradd -ms /bin/bash medauth

# Se configura para utilizarse el usuario creado
USER medauth

WORKDIR /home/medauth
COPY . .

CMD /bin/bash
