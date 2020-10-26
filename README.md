# Servicio de solicitudes de autorizaciones médicas

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/) [![Versions](https://img.shields.io/badge/Python-3.6|3.7|3.8|3.9-red.svg)](https://www.python.org/downloads/release/python-360/) [![Build Test](https://img.shields.io/travis/Carlosma7/CC-MedAuth/main)](https://travis-ci.org/github/Carlosma7/CC-MedAuth) 

---

**Autor:** Carlos Morales Aguilera

**Asignatura:** Cloud Computing

**Universidad:** Universidad de Granada (UGR)

## Configuración inicial del repositorio

---

La configuración del entorno de Git y Github en mi máquina local se puede visualizar [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/config_entorno.md).

## Descripción de problema y solución del proyecto

---

La descripción detallada del problema y la solución propuesta se puede leer [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/descripcion_problema.md).

## Arquitectura

---

La arquitectura propuesta se trata de una arquitectura basada en [microservicios](https://decidesoluciones.es/arquitectura-de-microservicios), frente a una arquitectura monolítica, tras valorar las distintas características y ver [comparativas](https://www.chakray.com/es/devops-arquitectura-monolitica-vs-microservicios/). De este modo podemos realizar un despliegue en la nube ofreciendo la posibilidad de obtener un servicio compuesto de un conjunto de microservicios que funcionan de forma aislada pero a su vez se puedan comunicar entre ellos.

Al emplear esta arquitectura contaremos con ventajas como pueden ser la *escalabilidad*, *versatilidad*, *autonomía*, *mantenimiento simple* y *aislamiento de errores*. Por todos estos motivos he decidido emplear esta arquitectura frente a otras opciones.

La arquitectura propuesta estará compuesta de los siguientes microservicios:

*  **Microservicio de autorizaciones médicas**: Se encargará de toda la funcionalidad asociada a las autorizaciones de intervenciones, operaciones o pruebas de diagnóstico.
*  **Microservicio de citas médicas**: Se encargará de la visualización y notificación de citas concertadas para los pacientes.

A continuación se muestra el esquema de nuestra arquitectura: 

![Arquitectura de microservicios](./doc/img/arquitectura.png "Arquitectura de microservicios")

## Herramientas

---

* Lenguaje de programación: [Python](https://www.python.org/), concretamente la versión mínima será la [Python 3.6](https://www.python.org/downloads/release/python-360/).
* Framework REST-API: [Flask](https://flask.palletsprojects.com/en/1.1.x/).
* Almacenamiento: [MongoDB](https://www.mongodb.com/es) con la herramienta [PyMongo](https://pymongo.readthedocs.io/en/stable/).
* Descubrimiento de servicios: [Consul](https://www.consul.io/).
* Gestor de eventos: [Celery](https://docs.celeryproject.org/en/stable/).
* Gestor de tareas: [Invoke](http://www.pyinvoke.org/).
* Gestor de versiones: [venv](https://docs.python.org/3/library/venv.html).

La justificación de la elección de las herramientas propuestas se puede ver [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/justificacion_herramientas.md).

## Milestones e issues resueltos

* [Configuración inicial repositorio](https://github.com/Carlosma7/CC-MedAuth/milestone/1)
    * [Crear .README.md](https://github.com/Carlosma7/CC-MedAuth/issues/1)
    * [Crear .gitignore](https://github.com/Carlosma7/CC-MedAuth/issues/2)
    * [Añadir licencia GPLv3](https://github.com/Carlosma7/CC-MedAuth/issues/3)
    * [Crear directorio de documentación y subida de imágenes](https://github.com/Carlosma7/CC-MedAuth/issues/4)
    * [Subir documento de configuración del entorno](https://github.com/Carlosma7/CC-MedAuth/issues/5)
    * [Crear fichero travis.yml](https://github.com/Carlosma7/CC-MedAuth/issues/6)
    * [Enlazar la configuración inicial de Github al README](https://github.com/Carlosma7/CC-MedAuth/issues/7)

* [Arquitectura](https://github.com/Carlosma7/CC-MedAuth/milestone/5)
    * [Escoger arquitectura y herramientas](https://github.com/Carlosma7/CC-MedAuth/issues/8)
    * [Reestructuración arquitectura de la aplicación](https://github.com/Carlosma7/CC-MedAuth/issues/16)

* [Configuración entorno](https://github.com/Carlosma7/CC-MedAuth/milestone/4)
    * [Configuración Travis](https://github.com/Carlosma7/CC-MedAuth/issues/10)
    * [Corregir fichero requirements.txt](https://github.com/Carlosma7/CC-MedAuth/issues/11)
    * [Corrección .travis.yml](https://github.com/Carlosma7/CC-MedAuth/issues/12)
    * [Configurar tareas de Invoke](https://github.com/Carlosma7/CC-MedAuth/issues/13)
    * [Configuración .gitignore para entorno python](https://github.com/Carlosma7/CC-MedAuth/issues/14)
    * [Configuración cc.yaml](https://github.com/Carlosma7/CC-MedAuth/issues/24)
    * [Fix cc.yaml](https://github.com/Carlosma7/CC-MedAuth/issues/30)

* [Documentación](https://github.com/Carlosma7/CC-MedAuth/milestone/3)
    * [Corrección documentación de arquitectura](https://github.com/Carlosma7/CC-MedAuth/issues/9)
    * [Documentación sobre gestión de versiones](https://github.com/Carlosma7/CC-MedAuth/issues/17)
    * [Corrección detalles visuales documentación](https://github.com/Carlosma7/CC-MedAuth/issues/18)
    * [Extraer descripción problema](https://github.com/Carlosma7/CC-MedAuth/issues/19)
    * [Extraer justificación herramientas escogidas](https://github.com/Carlosma7/CC-MedAuth/issues/25)
    * [Añadir badges a la documentación](https://github.com/Carlosma7/CC-MedAuth/issues/27)
    * [Documentar milestones, issues e historias de usuario](https://github.com/Carlosma7/CC-MedAuth/issues/28)
    * [Fix enlaces de badges](https://github.com/Carlosma7/CC-MedAuth/issues/29)
    
## Historias de usuario planteadas

* [Usuario](https://github.com/Carlosma7/CC-MedAuth/milestone/6)
    * [[HU1] Registro de email para notificaciones de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/issues/15)
    * [[HU2] Solicitud autorización médica](https://github.com/Carlosma7/CC-MedAuth/issues/20)
    * [[HU3] Comprobar estado de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/issues/21)
    * [[HU4] Notificar usuario de procesamiento de autorización](https://github.com/Carlosma7/CC-MedAuth/issues/22)
    * [[HU5] Visualizar citas médicas](https://github.com/Carlosma7/CC-MedAuth/issues/23)
