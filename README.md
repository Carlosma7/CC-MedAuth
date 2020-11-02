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

Para poder plantear una arquitectura, primero hay que entender como funciona el entorno real en el que vamos a desarrollar la solución y las características que este requiere:

La gestión de los distintos elementos que conforman el proceso de una autorización médica, son elementos completamente independientes que se gestionan de forma individual, como una póliza o una prescripción médica. A su vez, una autorización, requiere de varios de estos elementos mediante un procedimiento que hace uso de ellos. Además, estos elementos son utilizados también en otros procedimientos de la empresa para distintas actividades, por lo que no son exclusivos del entorno en el que se va desarrollar la solución.

Por otro lado, cuando un cliente va a realizar una autorización a la oficina, esta es procesada por el administrativo correspondiente, sin tener que esperar a que se confirme o deniegue dicha autorización, ya que el procesamiento procedimental y automático.

Por último, todas las gestiones que se realizan en nuestro escenario, son gestiones útiles para otras funcionalidades de la empresa, por lo que buscar una arquitectura que haga uso de la modularización en distintos componentes útiles, que puedan interconectarse no solo sería beneficioso para este proyecto, sino también para futuras aplicaciones que puedan tener relación con el mismo.

Siguiendo esta filosofía de conectar distintas funcionalidades que tiene una empresa de seguros, en la que la gestión se realiza de forma individual, pero para poder realizar un procedimiento tan complejo como una autorización, han de gestionarse estas distintas funcionalidades, se ha decidido emplear una **arquitectura de microservicios** que nos permita la gestión de los distintos componentes del escenario y como se comunican entre sí.

Con esta arquitectura, podremos llevar una gestión sencilla de cada uno de los elementos que conforman el problema, y a que su vez se comuniquen para conseguir un fin mayor, como es una autorización médica con su cita asociada.

## Herramientas

---

La justificación de la elección de las herramientas propuestas se puede ver [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/justificacion_herramientas.md).

## Roadmap

---

En una primera fase del desarrollo el *producto mínimo viable* inicial constará de la administración del sistema, que incluye la gestión de pólizas del sistema siendo las operaciones crear usuario administrativo, crear usuario de asegurado, consultar póliza y modificar póliza de un asegurado las funciones básicas y minimales del sistema. La historia de este desarrollo puede seguirse tal y como indicamos a continuación:

* [Administración de pólizas](https://github.com/Carlosma7/CC-MedAuth/milestone/10)
    - [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema.](https://github.com/Carlosma7/CC-MedAuth/issues/43)
    - [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema.](https://github.com/Carlosma7/CC-MedAuth/issues/44)
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


## Modelos

---


Se han creado los modelos *Usuario* y *Póliza* de acuerdo a las historias de usuario mencionadas en la primera fase [Administración de pólizas](https://github.com/Carlosma7/CC-MedAuth/milestone/10):

* [Usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/models/usuario.py)
* [Póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/models/poliza.py)

Se puede comprobar que son sintácticamente correctas ejecutando:

```bash
python -m py_compile src/models/usuario.py
python -m py_compile src/models/poliza.py
```

Y se puede comprobar la correcta integración de los modelos, y por tanto, asegurarnos de la corrección sintáctica de los archivos ejecutando:

```bash
python src/main.py
```
