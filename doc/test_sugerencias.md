## Test y Sugerencias

---

Criterios tests realizados

A la hora de realizar tests significativos, tal y como se explica y detalla en el [avance del código](https://carlosma7.github.io/MedAuth/doc/avance_codigo) del proyecto se han tenido en cuenta los siguientes criterios a la hora de realizar tests:

* Comprobar integridad de un objeto, ya sea comparándose consigo mismo o con otro idéntico, siendo idéntico aquel que sin ser el mismo objeto, posee las mismas características.
* Comprobar valores correctos, incluyendo los valores de las clases *enum*.
* Comprobar la correcta inserción y eliminación de los objetos que se almacenan.
* Comprobar la unicidad de los identificadores que se contemplan en el sistema.

Sugerencias de hitos previos

Las sugerencias que se han contemplado a la hora de realizar los avances en el proyecto han sido:

* Uso de las buenas prácticas del lenguaje. Entre una de ellas destaca el uso de empaquetamiento de módulos para hacer importaciones correctas en lugar de utilizar importaciones absolutas como en la entrega anterior (model.usuario.usuario).
* Uso de clases *enum* para representar variables con un conjunto de valores delimitado: [Tipo de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/tipoPoliza.py), [Módulo extra de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/moduloExtra.py) y [Especialidad médica](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/especialidad.py).
* Se realiza una gestión de usuarios, ya que son necesarios para relacionar las distintas entidades del sistema, entre las cuales forman parte. Sin embargo, no se consideran tareas de *Login* o administración de contraseñas.


