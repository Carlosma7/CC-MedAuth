## Herramientas de Integración Continua (*CI*)
---
### Estudio inicial
Existen numerosas herramientas destinadas a la integración continua (algunas de ellas además poseen también herramientas de despliegue continuo), por lo que para escoger una que se adapte a las necesidades de nuestro proyecto, se van a evaluar las Principales herramientas de *CI* (referencias al final del documento) observando sus principales ventajas y desventajas de cara a nuestro proyecto:

* [Jenkins](https://www.jenkins.io/): Es un servidor de automatización *open source*, proporciona cientos de de plugins y está desarrollado en *Java*. Es la herramienta más utilizada actualmente.

| Ventajas                                                        | Desventajas                                                                                                                      |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Interfaz intuitiva y sencilla de usar.                          | Dificultad de integración de plugins.                                                                                            |
| Extensible gracias a su comunidad de usuarios mediante plugins. | No está hosteado, por lo que hay que adquirir una máquina virtual y configurarlo.                                                |
| Gratis y *open source*.                                         | Pese a sus actualizaciones, el núcleo sigue utilizando funciones de *Java EE*, por lo que existe un gran número de dependencias. |
| Se puede encontrar una extensa documentación.                   | El núcleo puede resultar arcaico frente a otras herramientas más modernas.                                                       |
| Integración con *Git*.                                          |                                                                                                                                  |

	
* [CircleCI](https://circleci.com/): Es una plataforma moderna de integración continua y despliegue continuo. Automatiza la construcción, prueba e implementación de software.

| Ventajas                                                                                                                | Desventajas                                                         |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Configuración inicial automática con *GitHub*, detectando el lenguaje y creando una configuración básica para el mismo. | Opciones limitadas en el plan gratis.                               |
| Configuración sencilla mediante *YAML*.                                                                                 | Precio alto, aunque en nuestro caso no es realmente una desventaja. |
| Soporte *SSH*, para acceder a la máquina virtual.                                                                       | Necesidad de conocer *YAML*.                                        |
| Interfaz de usuario sencilla y intuitiva.                                                                               | Existen otras opciones con mejor documentación.                     |
| Soporte *Docker*.                                                                                                       |                                                                     |
| Paralelización de tests.                                                                                                |                                                                     |

* [TeamCity](https://www.jetbrains.com/es-es/teamcity/) : Es un servidor de gestión de compilación e integración continua de JetBrains. Permite ejecución remota y confirmaciones sometidas a prueba previa.

| Ventajas                                                    | Desventajas                                                                    |
|-------------------------------------------------------------|--------------------------------------------------------------------------------|
| Instalación sencilla mediante paquetes en los distintos SO. | Algunos de los plugins no funcionan según los usuarios en foros.               |
| Paralelización de tests en diferentes entornos.             | Prueba gratuita limitada a 100 *builds*.                                       |
| Facíl de configurar, extensible e interactivo.              | Logs poco intuitivos y con un formato que no resulta agradable de interpretar. |
| Permite asignación de roles y permisos.                     | Errores en ocasiones poco claros.                                              |
| Documentación sencilla, limpia e intuitiva.                 | Suele ofrecer problemas en las actualizaciones de version.                     |
|                                                             |                                                                                |

* [Shippable](https://www.shippable.com/): Es una plataforma de DevOps que ayuda a los desarrolladores y equipos de DevOps a lograr integración continua y despliegue continuo, y hacer lanzamientos de software frecuentes, predecibles y sin errores. 

| Ventajas                                                                                    | Desventajas                                                                                                                                  |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Gratis para proyectos *open source* con builds ilimitados. Permite 5 repositorios privados. | Escasez de información no oficial.                                                                                                           |
| Soporte *Docker*.                                                                           | Al haber sido adquirida por jFrog, se debe tener en cuenta también su otro nombre de cara a realizar búsquedas externas (*jFrog Pipelines*). |
| Integración con *GitHub*.                                                                   | No soporta todos los lenguajes, solo un pequeño conjunto.                                                                                    |
| Integración natural de tests.                                                               |                                                                                                                                              |
| Configurable mediante YAML.                                                                 |                                                                                                                                              |
| Documentación clara de pasos básicos en los distintos lenguajes que soporta.                |                                                                                                                                              |


* [CodeShip](https://codeship.com/): Es una plataforma alojada de integración y despliegue continuo. Se integra con el repositorio de código fuente y el entorno de alojamiento, y prueba e implementa automáticamente cada cambio en la plataforma.

| Ventajas                                                                                                | Desventajas                                                    |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Configura equipos y permisos para organizaciones y miembros del equipo con el centro de notificaciones. | Prueba gratuita limitada a 100 *builds*.                       |
| Se integra con cualquier herramienta, servicio y entorno de nube.                                       | No soporta módulso de *Git*.                                   |
| Integración con GitHub sencilla.                                                                        | Quedan expuestos los *secrets* y variables de entorno ocultas. |
| Soporte *Docker*.                                                                                       | No favorece el desarrollo *open source*                        |
| Configuración sencilla.                                                                                 |                                                                |

* [Wercker](https://devcenter.wercker.com/):  Es una plataforma de integración continua y despliegue continuo basada en Docker que ayuda a los desarrolladores de software a construir e implementar sus aplicaciones y microservicios.

| Ventajas                                                  | Desventajas                                                                                           |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Completamente gratis en repositorios en fase Beta.        | No queda muy claro hasta que punto se considera un repositorio en fase Beta, por lo que es un riesgo. |
| Libertad completa a la hora de realizar la configuración. | Documentación excesivamente compleja e incomprensible.                                                |
| Integración con GitHub.                                   | Escasez de información no oficial, lo cual es inesperado tratándose de una herramienta de Oracle.     |
| Chatbot que facilita las notificaciones.                  |                                                                                                       |

* [Drone.io](https://www.drone.io/): Es una plataforma de integración continua moderna que permite a los equipos ocupados automatizar sus flujos de trabajo de creación, prueba y lanzamiento mediante un potente motor de canalización nativo en la nube.

| Ventajas                             | Desventajas                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| Integración con GitHub.              | Escasez de documentación.                                                   |
| Realiza el hosteo de forma autónoma. | No permite realizar esperas entre tareas.                                   |
| Integración con Docker.              | Poco soporte de la herramienta.                                             |
| Plan gratis de 5000 *builds* al año. | Para las características que presenta, es preferible utilziar **CircleCI**. |
| Paralelismo de tests.                | Hardware no configurable.                                                   |
| Configurable mediante YAML.          |                                                                             |

* [AppVeyor](https://www.appveyor.com/): Es un servicio de integración continua alojado y distribuido que se utiliza para construir y probar proyectos alojados en GitHub y otros servicios de alojamiento de código fuente en una máquina virtual Microsoft Windows, así como máquinas virtuales Ubuntu Linux.

| Ventajas                                                      | Desventajas                                                                   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------|
| Gratis para proyectos *open source*.                          | Configuración limitada a todo el proyecto o una única rama.                   |
| Posee entornos de construcción tanto para Windows como Linux. | Existen opciones mejores como *CircleCI* o *Travis*, y con más documentación. |
| Interfaz limpia y sencilla.                                   |                                                                               |
| Configurable mediante *YAML*.                                 |                                                                               |
| Paralelismo de tests.                                         |                                                                               |

* [SemaphoreCI](https://semaphoreci.com/): Es un servicio alojado de integración continua y despliegue continuo utilizado para probar y desplegar proyectos de software alojados en GitHub y BitBucket.

| Ventajas                             | Desventajas                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------|
| Gratis para proyectos *open source*. | Prueba gratuita limitada a 100 *builds*.                                          |
| Soporte *Docker*.                    | No permite su uso con repositorios privados.                                      |
| Integración con *GitHub*.            | No está hosteado, por lo que hay que adquirir una máquina virtual y configurarlo. |

Además de las previamente analizadas, se han estudiado también opciones como [GitLabCI](https://docs.gitlab.com/ee/ci/), [Bamboo](https://www.atlassian.com/es/software/bamboo), [Buddy](https://buddy.works/) o [GoCD](https://www.gocd.org/), que han sido rechazadas directamente por distintos motivos. Se puede observar que realmente hay un amplio abanico de opciones a elegir para realizar la integración continua en el proyecto, por lo que dentro de elegir aquellas que más se adecúen al proyecto, también cabe observar aquellas que resulten más interesantes para el mismo.

Tras analizar las distintas opciones, se ha decidido finalmente realizar la integración continua con distintas herramientas y ver como se realiza en cada una de ellas:

* **CircleCI**: Es la herramienta más popular en la actualidad, y la que en un principio presenta mejores características de cara al proyecto. Además se trata de un competidor directo de *Travis*, por lo que resultará interesante analizarlo.

* **Shippable**: Evidentemente es una de las herramientas que más ventajas presenta a simple vista respecto a las pocas desventajas que se han podido encontrar. Aunque existía con anterioridad se trata de una herramienta que ha sido adquirida recientemente en 2019 por [jFrog](https://jfrog.com/), por lo que realmente resultará interesante estudiar la herramienta propuesta para la realización de integración continua por una de las grandes empresas actuales de DevOps.

* **Github Actions**: Realmente resulta interesante tratar las propias *Actions* de *GitHub* como herramienta de integración continua, tal y como se ha podido observar en distintos proyectos durante la investigación, obteniendo así una integración completa en el proyecto.

