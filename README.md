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

## Roadmap

---

En una primera fase del desarrollo el *producto mínimo viable* inicial constará de la administración del sistema, que incluye la gestión de pólizas del sistema siendo las operaciones consultar póliza y modificar póliza de un asegurado las funciones básicas y minimales del sistema. La historia de este desarrollo puede seguirse tal y como indicamos a continuación:

* [Administración de pólizas](https://github.com/Carlosma7/CC-MedAuth/milestone/10)
    - [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada.](https://github.com/Carlosma7/CC-MedAuth/issues/34)
    - [Como administrativo quiero modificar la póliza de un asegurado para cambiar las condiciones o el tipo de póliza.](https://github.com/Carlosma7/CC-MedAuth/issues/35)
    
En una segunda fase del desarrollo con objetivo de obtener el siguiente *producto mínimo viable* del desarrollo, se realizará la gestión de autorizaciones por parte del asegurado siendo las operaciones añadir una prescripción médica, solicitar una autorización médica y consultar una autorización médica. La historia de este desarrollo se organiza de la siguiente forma:

* [Gestión de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/milestone/7)
    - [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica.](https://github.com/Carlosma7/CC-MedAuth/issues/36)
    - [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico.](https://github.com/Carlosma7/CC-MedAuth/issues/37)
    - [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización.](https://github.com/Carlosma7/CC-MedAuth/issues/38)

En una tercera entrega del desarrollo de un *producto mínimo viable*, se realizará la administración de autorizaciones por parte del administrativo, siendo las operaciones de administración de autorizaciones médicas y aprobación/denegación de autorizaciones médicas. El esquema a seguir en este desarrollo se indica a continuación:

* [Administración de autorizaciones](https://github.com/Carlosma7/CC-MedAuth/milestone/9)
    - [Como administrativo quiero administrar una autorización médica de un asegurado para ver o modifcar una autorización.](https://github.com/Carlosma7/CC-MedAuth/issues/39)
    - [Como administrativo quiero cambiar la aprobación o denegación de una autorización para tratar un caso excepcional.](https://github.com/Carlosma7/CC-MedAuth/issues/40)

En una fase final del desarrollo, y por tanto, un producto final incluirá la gestión de citas médicas a lo anteriormente conseguido, siendo las operaciones de consultar citas médicas y obtener notificaciones previas a una cita médica. La historia del desarrollo se especifica de la forma:

* [Gestión de citas médicas](https://github.com/Carlosma7/CC-MedAuth/milestone/8)
    - [Como asegurado quiero consultar una cita médica fijada para ver la información asociada.](https://github.com/Carlosma7/CC-MedAuth/issues/41)
    - [Como asegurado quiero ser notificado para asistir a una cita médica.](https://github.com/Carlosma7/CC-MedAuth/issues/42)







