## Arquitectura

---

Para poder plantear una arquitectura, primero hay que entender como funciona el entorno real en el que vamos a desarrollar la solución y las características que este requiere:

La gestión de los distintos elementos que conforman el proceso de una autorización médica, son elementos completamente independientes que se gestionan de forma individual, como una póliza o una prescripción médica. A su vez, una autorización, requiere de varios de estos elementos mediante un procedimiento que hace uso de ellos. Además, estos elementos son utilizados también en otros procedimientos de la empresa para distintas actividades, por lo que no son exclusivos del entorno en el que se va desarrollar la solución.

Por otro lado, cuando un cliente va a realizar una autorización a la oficina, esta es procesada por el administrativo correspondiente, sin tener que esperar a que se confirme o deniegue dicha autorización, ya que el procesamiento procedimental y automático.

Por último, todas las gestiones que se realizan en nuestro escenario, son gestiones útiles para otras funcionalidades de la empresa, por lo que buscar una arquitectura que haga uso de la modularización en distintos componentes útiles, que puedan interconectarse no solo sería beneficioso para este proyecto, sino también para futuras aplicaciones que puedan tener relación con el mismo.

Siguiendo esta filosofía de conectar distintas funcionalidades que tiene una empresa de seguros, en la que la gestión se realiza de forma individual, pero para poder realizar un procedimiento tan complejo como una autorización, han de gestionarse estas distintas funcionalidades, se ha decidido emplear una **arquitectura de microservicios** que nos permita la gestión de los distintos componentes del escenario y como se comunican entre sí.

Con esta arquitectura, podremos llevar una gestión sencilla de cada uno de los elementos que conforman el problema, y a que su vez se comuniquen para conseguir un fin mayor, como es una autorización médica con su cita asociada.
