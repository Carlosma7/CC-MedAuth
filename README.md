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

El plan de desarrollo del proyecto va a seguir una serie de etapas que irán añadiendo determinadas funcionalidades y herramientas para poder desarrollar un *producto mínimo viable* en cada entrega, que se irá desarrollando en las distintas etapas y que añadirá nueva funcionalidad de forma consecuente a cada fase del desarrollo.

1. **Fase inicial**: En una primera entrega del desarrollo, se constará de un esquema inicial del proyecto, en el que se determinarán las entidades iniciales con las que se han de trabajar en el problema, indicar que funcionalidades poseen y diseñar una clase inicial para dichas entidades, de forma que quede una estructura inicial a seguir en el desarrollo.

    En esta primera fase se relacionan las clases diseñadas a las distintas *historias de usuario* de todos los *milestones* del proyecto, ya que es necesario definir el esquema inicial:
    
* Entidad usuario:
    * [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema.](https://github.com/Carlosma7/MedAuth/issues/43)
    * [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema.](https://github.com/Carlosma7/MedAuth/issues/44)
* Entidad póliza:
    * [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada.](https://github.com/Carlosma7/MedAuth/issues/34)
* Entidad prescripción:
    * [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica.](https://github.com/Carlosma7/MedAuth/issues/36)
* Entidad autorización: 
    * [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico.](https://github.com/Carlosma7/MedAuth/issues/37)
* Entidad cita:
    * [Como asegurado quiero consultar una cita médica fijada para ver la información asociada.](https://github.com/Carlosma7/MedAuth/issues/41)

2. **Segunda fase**: En esta entrega de un nuevo producto mínimo viable, se empiezan a desarrollar las primeras tareas de gestión administrativa de los distintos componentes del sistema. Además se introduce un entorno de testeo adecuado que permita comprobar que las tareas de desarrollo realizadas se desenvuelven correctamente.

    Inicialmente se realizará toda la funcionalidad de [administración de pólizas](https://github.com/Carlosma7/MedAuth/milestone/10):
    * [Como administrativo quiero modificar la póliza de un asegurado para cambiar las condiciones o el tipo de póliza.](https://github.com/Carlosma7/MedAuth/issues/35)
    
    Tras la gestión de pólizas, se realizará la [administración de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/9), la cual depende de la gestión de pólizas anteriormente mencionada:
    * [Como administrativo quiero administrar una autorización médica de un asegurado para ver o modifcar una autorización.](https://github.com/Carlosma7/MedAuth/issues/39)
    * [Como administrativo quiero cambiar la aprobación o denegación de una autorización para tratar un caso excepcional.](https://github.com/Carlosma7/MedAuth/issues/40)
    
    Finalmente, se realizará la [administración de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/11), las cuales son creadas tras las autorizaciones:
    * [Como administrativo quiero modificar una cita médica fijada para cambiar información asociada a la cita.](https://github.com/Carlosma7/MedAuth/issues/49)
    
3. **Tercera fase**: En esta fase se añaden las funcionalidades asociadas a la gestión de una cita médica y una autorización médica. En esta fase además se cumplen los requisitos administrativos previos para poder gestionar por la parte administrativa los distintos elementos a tratar.

    Inicialmente, se realizará la [gestión de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/7), preparando el escenario para desarrollar en un futuro la solicitud de autorizaciones con toda la funcionalidad previa necesaria:
    * [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica.](https://github.com/Carlosma7/MedAuth/issues/36)
    * [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización.](https://github.com/Carlosma7/MedAuth/issues/38)
    
    Posteriormente, tras dotar al sistema de la funcionalidad de cara al cliente para gestionar autorizaciones, se añadiran las funcionalidades básicas de [gestión de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/8):
    * [Como asegurado quiero consultar una cita médica fijada para ver la información asociada.](https://github.com/Carlosma7/MedAuth/issues/41)
    
4. **Fase final**: Finalmente en esta entrega, se añaden las funcionalidades que intercomunican todos los elementos anteriormente definidos y desarrollados, añadiendo las funcionalidades de solicitud de autorización médica y los cambios que implican en el sistema. Se añaden también funcionalidades relativas a notificación del usuario sobre citas médicas.

    Para realizar el proceso completo de [gestión de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/7), se añade el procedimiento de solicitud:
    * [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico.](https://github.com/Carlosma7/MedAuth/issues/37)
    
    Por último, además de haber conectado toda la funcionalidad anterior del sistema, se añade un extra de [gestión de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/8) como es la notificación previa a una cita por correo:
    * [Como asegurado quiero ser notificado para saber cuando debo asistir a una cita médica.](https://github.com/Carlosma7/MedAuth/issues/42)


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
