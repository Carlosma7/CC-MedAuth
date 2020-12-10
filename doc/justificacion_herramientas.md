## Herramientas

---

##### Lenguaje de programación

El lenguaje con el que se van a desarrollar los distintos microservicios va a ser [Python](https://www.python.org/). Tras valorar otras opciones como *Node.js*, *Ruby* o *Go*, y observar algunas [comparativas](https://www.clariontech.com/blog/5-best-technologies-to-build-microservices-architecture).

La versión escogida será [Python 3.6](https://www.python.org/downloads/release/python-360/), por lo que será la versión mínima requerida, siendo compatible con las versiones superiores. De esta forma quedará establecido:

* Mínima: *Python 3.6*.
* Máxima: *Python 3.9*.

Por lo tanto, las herramientas que se escogan a continuación buscarán obtener la mayor integración natural posible con el lenguaje.

##### Gestor de tareas

El gestor de tareas empleado será [Invoke](http://www.pyinvoke.org/). Se han examinado otras herramientas, realizado una comparativa y realizado la decisión, tal y como se puede ver [aquí](https://carlosma7.github.io/MedAuth/doc/gestor_tareas).

##### Biblioteca de aserciones

Como biblioteca de aserciones se ha decidido utilizar [assertpy](https://github.com/assertpy/assertpy), tras realizar una comparativa con otras opciones, junto a las aserciones estándar de *Python*, tal y como se puede ver [aquí](https://carlosma7.github.io/MedAuth/doc/biblioteca_asercion).

##### Marco de pruebas

Se ha escogido como marco de pruebas [Pytest](https://docs.pytest.org/en/stable/), tras realizar un análisis de las diferentes opciones disponibles, el cual se puede ver [aquí](https://carlosma7.github.io/MedAuth/doc/marco_pruebas).

##### Contenerización Docker

Para la contenerización del proyecto, se ha decidido utilizar dos registros distintos [Docker Hub](https://hub.docker.com/) y [GitHub Container Registry](https://github.com/features/packages), tras realizar un estudio sobre la imagen base de *Docker* que se puede ver [aquí](https://carlosma7.github.io/MedAuth/doc/estudio_docker/estudio_contenedor_base).

La información se organiza de la siguiente forma:

* [Documentación sobre Dockerfile](https://carlosma7.github.io/MedAuth/doc/estudio_docker/documentacion_dockerfile)
* [Docker Hub y automatización de subidas](https://carlosma7.github.io/MedAuth/doc/estudio_docker/documentacion_docker_hub)
* [Github Container Registry y automatización de subidas](https://carlosma7.github.io/MedAuth/doc/estudio_docker/github_container_registry)

##### Integración continua

Se ha decidido utilizar varias herramientas de *CI*, entre las cuales se encuentran:

* [TravisCI](https://carlosma7.github.io/MedAuth/doc/integracion_continua/configuracion_travis)
* [CircleCI](https://carlosma7.github.io/MedAuth/doc/integracion_continua/configuracion_circleci)
* [Shippable](https://carlosma7.github.io/MedAuth/doc/integracion_continua/configuracion_shippable)
* [GitHub Actions](https://carlosma7.github.io/MedAuth/doc/integracion_continua/configuracion_github_action)

Además se puede encontrar un [estudio](https://carlosma7.github.io/MedAuth/doc/integracion_continua/estudio_ci) sobre las herramientas *CI* existentes.

Por último se puede observar una documentación sobre la integración del [gestor de tareas con las herramientas de CI](https://carlosma7.github.io/MedAuth/doc/integracion_continua/justificacion_invoke) y el [aprovechamiento del contenedor Docker para CI](https://carlosma7.github.io/MedAuth/doc/integracion_continua/justificacion_docker).
