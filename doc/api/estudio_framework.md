
### Estudio inicial

Existen numerosas herramientas destinadas al diseño y configuración de *APIs* para microservicios, por lo que para escoger una que se adapte a las necesidades de nuestro proyecto, se van a evaluar las principales herramientas observando sus principales ventajas y desventajas de cara a nuestro proyecto:

[Django](https://www.djangoproject.com/): Es un marco web avanzado que puede desarrollar rápidamente sitios web seguros y fáciles de mantener. Es gratuito y de código abierto, tiene una comunidad activa, mucha documentación y considerables opciones de soporte gratuitas y de pago.

| Ventajas                                                 | Desventajas                                                                                |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Filosofía *DRY*, incluyendo baterías de configuraciones. | Es monolítico, permite configurar pero basándose en unos ajustes estándar.                 |
| Utiliza una arquitectura MVC.                            | Es una herramienta muy potente, pero no adecuada para proyectos pequeños.                  |
| Permite desarrollo paralelo.                             | Utiliza expresiones regulares para las URLs, generando más código y sintaxis más compleja. |
| Escalable.                                               | Los errores con templates no están gestionados.                                            |
| Encriptación de información.                             |                                                                                            |
| Buena documetnación y comunidad activa.                  |                                                                                            |
| Integración sencilla con bases de datos.                 |                                                                                            |


[Flask](https://flask.palletsprojects.com/en/1.1.x/): Es un microframework escrito en *Python* que no requiere herramientas o bibliotecas específicas y admite extensiones que pueden agregar funcionalidad a la aplicación como si estuvieran implementadas en el propio *Flask*.

| Ventajas                                                           | Desventajas                                                   |
|--------------------------------------------------------------------|---------------------------------------------------------------|
| Fácil y cómodo de usar.                                            | No es asíncrono salvo que se configure como tal.              |
| Gran comunidad y documentación.                                    | Orientado a HTML.                                             |
| Extensible mediante plugins.                                       | La modularización requiere una mayor gestión de la seguridad. |
| Muy flexible.                                                      |                                                               |
| Diseño minimalista.                                                |                                                               |
| Permite tests unitarios, y se integra principalmente con *pytest*. |                                                               |
| Debug fácil y rápido.                                              |                                                               |


[Web2py](http://www.web2py.com/): Es un framework completo de código abierto gratuito para el desarrollo rápido de aplicaciones basadas en web escalables, rápidas y seguras. Escrito y programado en *Python*.

| Ventajas                                | Desventajas                                      |
|-----------------------------------------|--------------------------------------------------|
| Extensible                              | Comunidad casi inexistente.                      |
| Documentación a modo de libro tutorial. | El IDE web es muy limitado.                      |
| Soporte de usuario.                     | Poca documentación no oficial.                   |
| Fácil mantenimiento.                    | No soporta tests unitarios. Aunque sí *doctest*. |
| Posee un IDE basado en web.             | Requiere demasiado tiempo la integración.        |


[Bottle](https://bottlepy.org/docs/dev/): Es un microframework web *WSGI* rápido, simple y ligero para *Python*. Se distribuye como un módulo de archivo único y no tiene más dependencias que la Biblioteca estándar de *Python*.

| Ventajas                                                      | Desventajas                                                   |
|---------------------------------------------------------------|---------------------------------------------------------------|
| Flexible mediante plugins.                                    | Pequeña comunidad.                                            |
| Incluido en las librerías estándar.                           | Poca documentación no oficial y tutoriales demasiado simples. |
| Asíncrono.                                                    | Orientada a proyectos minimalistas.                           |
| Toda la configuración se encuentra en el fichero *bottle.py*. | Poco extensible.                                              |


[Tornado](https://www.tornadoweb.org/en/stable/): Es un framework web desarrollado en *Python* junto a una biblioteca de red asincrónica. Al usar E/S de red sin bloqueo, *Tornado* puede escalar a miles de conexiones abiertas.

| Ventajas                                                            | Desventajas                                                                                                                                 |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Minimalista.                                                        | El modo *WSGI* no permite aprovechar todas sus características.                                                                             |
| Paradigma basado en eventos, via IOLoop. Para tareas de networking. | La comunidad y la documentación es pequeña.                                                                                                 |
| El sistema de templates es muy flexible.                            | Poca documentación no oficial.                                                                                                              |
| Servidor HTTP muy rápido desarrollado en su mayoría en *Python*.    | Los ficheros son almacenados en el servidor, no en directorios temporales.                                                                  |
| Muy utilizado en campos de minería de datos.                        | Muchas bases de datos y librerías puede producir problemas de bloqueo del IOLoop, y gestionar este problema requiere bastante conocimiento. |
|                                                                     | Difícil de aprender y poco intuitivo, muy orientado a un determinado sector.                                                                |


[Pyramid](https://trypyramid.com/): Es un framework web desarrolado en *Python* pequeño, rápido y práctico. Se desarrolla como parte del Proyecto *Pylones*. Tiene una licencia similar a *BSD*.

| Ventajas                      | Desventajas                                                               |
|-------------------------------|---------------------------------------------------------------------------|
| Flexible mediante templates.  | No permite gestión de bases de datos. Se necesitan herramientas externas. |
| Soporta arquitectura MVC.     | Enfoca el desarrollo del proyecto en un único fichero.                    |
| Fácil de entender y extender. | Muy pesado, por lo que no es recomendable para proyectos pequeños.        |
| Moderno.                      | Documentación escasa, y pequeña comunidad debido a su poco tiempo.        |


[TurboGears](https://turbogears.org/): Es un framework desarrollado en *Python* con capa full-stack implementada sobre un núcleo de microframework con soporte para MongoDB, aplicaciones conectables y administración autogenerada.

| Ventajas                                                                    | Desventajas                                        |
|-----------------------------------------------------------------------------|----------------------------------------------------|
| Soporta varias bases de datos.                                              | Comunidad pequeña.                                 |
| Orientado al manejo de bases deda tos.                                      | Poca documentación, tanto oficial como no oficial. |
| Sistema de transacciones que maneja transacciones de varias bases de datos. | Existen mejores opciones, como *Django*.           |
| Flexible mediante plugins.                                                  |                                                    |
| Fácil para crear librerías reutilizables.                                   |                                                    |
| Sistema de administración propio.                                           |                                                    |


[CherryPy](https://cherrypy.org/): Es un framework web orientado a objetos desarrollado en *Python*. Tiene como objetivo desarrollar rápidamente aplicaciones Web, pero las funcionalidades son demasiado básicas para proyectos con muchas especificaciones.

| Ventajas                                      | Desventajas                                                    |
|-----------------------------------------------|----------------------------------------------------------------|
| Sencillo y fácil de entender.                 | La documentación es escasa e insuficiente.                     |
| La opción más ligera.                         | Las funcionalidades son muy limitadas para pequeños proyectos. |
| Permite diseñar APIs y manejar formatos JSON. | Existen opciones mejor como *Flask*.                           |
| Configuración robusta.                        |                                                                |


[Hug](https://www.hug.rest/): Es una pequeña biblioteca para crear API que son fáciles de entender y mantener. Permite crear APIs muy rápidamente con muy poco código y siguiendo unas buenas prácticas. *Hug* no es una biblioteca patentada para hacer API web, sino que se centra en permitirle crear API desde la perspectiva más amplia: una interfaz que permite el uso automático (a través del código) de los programas.

| Ventajas                           | Desventajas                                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Muy simple e intuitiva.            | Documentación escasa y sin comunidad existente.                                                                       |
| Sencillez a la hora de configurar. | Es una opción interesante, pero a la vez demasiado arriesgada debido a la falta de documentación que permita saberlo. |
| Gestión de APIs sencillas.         |                                                                                                                       |
| Minimalista.                       |                                                                                                                       |


[FastAPI](https://fastapi.tiangolo.com/): Es un framework rápido, con poco tiempo ya que se originó en 2019. Permite crear APIs con *Python* 3.6+ basado en sugerencias de tipado *Python* estándar.

| Ventajas                                        | Desventajas                    |
|-------------------------------------------------|--------------------------------|
| Moderna y sencilla.                             | Comunidad pequeña.             |
| Asíncrona.                                      | Poca documentación no oficial. |
| Independiente de base de datos.                 |                                |
| Generación automática de documentaciónd de API. |                                |
| Validación de datos.                            |                                |
| Inyección de dependencias.                      |                                |


[Falcon Framework](https://falconframework.org/): Es una biblioteca *WSGI* minimalista que sirve para crear APIs web rápidas y backends de aplicaciones. El diseño de *Falcon* es simple y claro, utilizando estilos arquitectónicos *HTTP* y *REST*.

| Ventajas                         | Desventajas                         |
|----------------------------------|-------------------------------------|
| Ligero con dependencias mínimas. | Limitado al diseño de APIs REST.    |
| Gran performance.                | Solamente posee backend.            |
| Ligero con dependencias mínimas. | Únicamente documentación oficial.   |
|                                  | Documentación oficial algo confusa. |

[Starlette](https://www.starlette.io/): Es un conjunto de herramientas y framework *ASGI* liviano, ideal para crear servicios *asyncio* de alto rendimiento.


| Ventajas                                                                                                                      | Desventajas                                        |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Alto rendimiento.                                                                                                             | No posee interfaz de administrador.                |
| Comunidad activa.                                                                                                             | No existe apenas documentación que no sea oficial. |
| Optimizado con *ASGI*.                                                                                                        | Existen opciones similares como *FastAPI*.         |
| Excelente documentación oficial.                                                                                              |                                                    |
| Permite una definición de rutas aisladas, permitiendo crear una jerarquía de forma sencilla y de forma separada del programa. |                                                    |

Tras un análisis inicial, se ha decidido seguir explorando las siguientes herramientas:
* *Flask*: La opción más utilizada junto a *Django*, además de ser la opción minimalista principal. Quizás se ajuste para el proyecto mejor que *Django*. Un gran contra es el de no soportar las peticiones asíncronas, aunque se evaluará la forma de suplirlo.
* *FastAPI*: Opción más moderna, es muy interesante ya que ofrece ventajas frente a los otros dos competidores, y parece ser una opción a considerar importante en un futuro próximo.
* *Starlette*: Igual que *FastAPI*, es una opción novedosa e interesante, realmente se podrían considerar competidores.
* *Django*: Opción más conocida, y de las que más ventajas ofrece, aunque quizás sea una herramienta demasiado pesada con opciones innecesarias.

### Análisis opciones

Tras una investigación más profunda, se ve claramente que *Django* no es la opción más adecuada para el proyecto, ya que generaría más código del ya existente y la mayoría de las funcionalidades que ofrece no serían utilizadas, básicamente sería el equivalente a "*matar moscas a cañonazos*". Por este motivo, la decisión se decidirá entre **Flask** y **FastAPI**.

El principal problema encontrado a la hora de elegir *Flask* es el de las peticiones asíncronas, ya que en el contexto del proyecto, carece de sentido realizar las peticiones de forma síncrona, ya que un cliente no puede quedar a la espera de otro para solicitar una autorización, por ejemplo.

Tras evaluar las diferentes opciones posibles para configurar *Flask* con peticiones asíncronas, se han encontrado las siguientes opciones:
*  [Flask-aiohttp](https://flask-aiohttp.readthedocs.io/en/latest/): Trata de solventar el problema realizando peticiones *asyncio*, pero las funcionalidades de *Flask* se ven reducidas, por lo que no es realmente una opción válida.
* Utilizar *Flask* junto a una cola de eventos y un broker para las diferentes peticiones: Es una opción válida, que permitiría una configuración correcta de cada elemento por separado, pero que conllevaría un mayor trabajo, y uso de herramientas que realmente se podrían omitir con la utilización de otros microframeworks asíncronos que realizan esta función de por sí.
* [Quart](https://gitlab.com/pgjones/quart): Probablemente la opción más interesante, ya que se basa complemante en la API de *Flask* y añade la funcionalidad de *async* para peticiones asíncronas, por lo que realmente es una librería top de *Flask*.
* [Sanic](https://sanic.readthedocs.io/en/latest/):  Es otra opción interesante, ya que utiliza una API similar a la de *Flask*, y se podría considerar un competidor directo de *Quart*, por lo que realmente no hay demasiadas diferencias a la hora de escoger un framework u otro.

Tras analizar estas opciones, realmente el debate se encuentra en utilizar *Quart*, *Sanic* o *FastAPI*. Si bien todas las opciones son interesantes, y *FastAPI* es una gran opción a considerar, la documentación de la misma considero que es insuficiente para asegurar la continuidad del proyecto en este momento, mientras que *Flask* posee una gran trayectoria, una gran comunidad y una documentación extensa ofrece una mayor confiabilidad, y al estar *Quart* desarrollada sobre *Flask*, posee esta ventaja, y *Sanic* se presenta como una alternativa del mismo.

*FastAPI* es una herramienta que promete ser un gran competidor de *Flask*, pero que al haber sido creada tan recientemente, no ofrece garantías suficientes aún de poder superar a *Flask* y la curva de aprendizaje es considerablemente superior.

Por último, aunque la decisión debería basarse en decisiones técnicas, realmente no hay aspectos que definan cual de los dos frameworks es mejor para el proyecto, ya que ambos son completamente válidos. Por cuestión de curiosidad e investigación, y por tener menor popularidad pese a ser una herramienta bastante interesante, se utilizará *Quart*, con el objetivo de aprender a utilizar un framework nuevo.

Finalmente el microframework sobre el que se va a desarrollar la API del proyecto es **Quart**.

