## Herramientas

---

##### Lenguaje de programación

El lenguaje con el que se van a desarrollar los distintos microservicios va a ser [Python](https://www.python.org/). Tras valorar otras opciones como *Node.js*, *Ruby* o *Go*, y observar algunas [comparativas](https://www.clariontech.com/blog/5-best-technologies-to-build-microservices-architecture).

La versión escogida será [Python 3.6](https://www.python.org/downloads/release/python-360/), por lo que será la versión mínima requerida, siendo compatible con las versiones superiores. De esta forma quedará establecido:

* Mínima: *Python 3.6*.
* Máxima: *Python 3.9*.

Por lo tanto, las herramientas que se escogan a continuación buscarán obtener la mayor integración natural posible con el lenguaje.

##### Framework

Se empleará como framework [Flask](https://flask.palletsprojects.com/en/1.1.x/), frente a *Django* y otros competidores, el cual nos permitirá realizar el proceso de construcción de nuestra web. Se ha escogido *Flask* debido a que se trata un framework más sencillo de desarrollar frente a *Django*, tras analizar las distintas [ventajas y desventajas](https://openwebinars.net/blog/django-vs-flask/) que ofrecen ambos.

##### Configuración distribuida

Se utilizará Consul como sistema de descubrimiento de servicios ya que permite un registro de los servicios, es compatible con APIs basadas en HTML y JSON, utiliza un sistema de almacenamiento por pares clave-valor, y posee una documentación detallada y sencilla.

##### Log

Para realizar una configuración con loggers se utilizará un propio módulo de *Python*, que es la librería [Logging](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/logging-de-python/). Este módulo permite realizar una gestión y análisis de errores, seguimiento de acciones y depuración del sistema bastante sencilla y de forma natural con el lenguaje propuesto.
