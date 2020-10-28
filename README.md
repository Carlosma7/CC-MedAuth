# Servicio de solicitudes de autorizaciones médicas

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/) [![Versions](https://img.shields.io/badge/Python-3.6|3.7|3.8|3.9-red.svg)](https://www.python.org/downloads/release/python-360/) [![Build Test](https://img.shields.io/travis/Carlosma7/CC-MedAuth/main)](https://travis-ci.org/github/Carlosma7/CC-MedAuth) 

---

**Autor:** Carlos Morales Aguilera

**Asignatura:** Cloud Computing

**Universidad:** Universidad de Granada (UGR)

## Descripción de problema y solución del proyecto

---

La descripción detallada del problema y la solución propuesta se puede leer [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/descripcion_problema.md).

## Arquitectura

---

Existen diversos tipos de arquitectura que podrían solucionar el problema propuesto, pero a continuación se van a detallar las ventajas que presenta la arquitectura basada en [microservicios](https://decidesoluciones.es/arquitectura-de-microservicios), frente una arquitectura monolítica o por capas.

* El código se simplifica y añadir funcionalidad en las diferentes etapas, y por lo tanto en los *productos mínimos viables* futuros, hacer un cambio en un producto es más sencillo que en las arquitecturas monolíticas.
* Ante un problema puntual de un microservicio, el funcionamiento del resto de componentes (tanto de la misma aplicación, como de otros servicios que consuman, externos a la aplicación) no se vería afectado.
* Escalar a un mayor número de clientes es tan sencillo como crear nuevas instancias de un microservicio.
* Además, el uso de microservicios aporta una naturaleza cultural **DevOps**, obligándonos a desarrollar, implementar, testear, desplegar y monitorizar en un proceso completo frente a la metodología tradicional del administrador del sistema.

En este problema, cada uno de los procesos de gestión de citas médicas, pólizas de asegurados y autorizaciones de intervenciones se gestionan como servicios independientes, que a su vez se comunican permitiendo la interoperabilidad y obteniendo un sistema general con una funcionalidad completa.

Por lo tanto, la arquitectura propuesta estará compuesta de los siguientes microservicios:

* **Gestión de pólizas de asegurados**.
* **Gestión de autorizaciones y solicitudes**.
* **Consulta de citas médicas y notificaciones**.

## Herramientas

---

* Lenguaje de programación: [Python](https://www.python.org/), concretamente la versión mínima será la [Python 3.6](https://www.python.org/downloads/release/python-360/).
* Framework REST-API: [Flask](https://flask.palletsprojects.com/en/1.1.x/).
* Almacenamiento: [MongoDB](https://www.mongodb.com/es) con la herramienta [PyMongo](https://pymongo.readthedocs.io/en/stable/).
* Gestor de tareas: [Invoke](http://www.pyinvoke.org/).
* Entorno virtual de desarrollo: [venv](https://docs.python.org/3/library/venv.html).

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
    * [Documentación de estructuración del proyecto según milestones e issues resueltos](https://github.com/Carlosma7/CC-MedAuth/issues/26)
    * [Añadir badges a la documentación](https://github.com/Carlosma7/CC-MedAuth/issues/27)
    * [Documentación de historias de usuario del proyecto](https://github.com/Carlosma7/CC-MedAuth/issues/28)
    * [Fix enlaces de badges](https://github.com/Carlosma7/CC-MedAuth/issues/29)
    * [Corrección de milestones en la documentación](https://github.com/Carlosma7/CC-MedAuth/issues/31)
    
## Historias de usuario planteadas

* [Usuario](https://github.com/Carlosma7/CC-MedAuth/milestone/6)
    * [[HU1] Registro de email para notificaciones de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/issues/15)
    * [[HU2] Solicitud autorización médica](https://github.com/Carlosma7/CC-MedAuth/issues/20)
    * [[HU3] Comprobar estado de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/issues/21)
    * [[HU4] Notificar usuario de procesamiento de autorización](https://github.com/Carlosma7/CC-MedAuth/issues/22)
    * [[HU5] Visualizar citas médicas](https://github.com/Carlosma7/CC-MedAuth/issues/23)
