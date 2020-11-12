## Test y Sugerencias

---

##### Criterios tests realizados

A la hora de realizar tests significativos, tal y como se explica y detalla en el [avance del código](https://carlosma7.github.io/MedAuth/doc/avance_codigo) del proyecto se han tenido en cuenta los siguientes criterios a la hora de realizar tests:

* Comprobar integridad de un objeto, ya sea comparándose consigo mismo o con otro idéntico, siendo idéntico aquel que sin ser el mismo objeto, posee las mismas características.
* Comprobar valores correctos, incluyendo los valores de las clases *enum*.
* Comprobar la correcta inserción y eliminación de los objetos que se almacenan.
* Comprobar la unicidad de los identificadores que se contemplan en el sistema.

Sugerencias de hitos previos

##### Las sugerencias que se han contemplado a la hora de realizar los avances en el proyecto han sido:

* Uso de las buenas prácticas del lenguaje. Entre una de ellas destaca el uso de importaciones relativas correctas en lugar de utilizar importaciones absolutas como en la entrega anterior (model.usuario.usuario).
* Uso de clases *enum* para representar variables con un conjunto de valores delimitado: [Tipo de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/tipoPoliza.py), [Módulo extra de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/moduloExtra.py) y [Especialidad médica](https://github.com/Carlosma7/MedAuth/blob/main/src/test/modelos/especialidad.py).
* Se realiza una gestión de usuarios, ya que son necesarios para relacionar las distintas entidades del sistema, entre las cuales forman parte. Sin embargo, no se consideran tareas de *Login* o administración de contraseñas, como se comentó en clase.

##### Sugerencias tenidas en cuenta tras la primera corrección

* Se han evaluado los gestores de tareas más allá de un simple análisis y prueba. Se ha utilizado *Makefile* e instalado y probado *Poetry* (pese a no ser la elección final, considero que ha sido útil aprenderla y conocerla para poder comprender por qué decido realmente escoger uno u otro).
* Se ha comprendido el uso de las bibliotecas de aserciones, e incluso se ha cambiado la opción escogida inicialmente por la biblioteca *assertpy*, ya que además de ser muy útil considero más interesante tras hacer pruebas con distintas de las bibliotecas. Realmente sirve para entender que es una biblioteca de aserciones y en que difieren unas y otras, o para darse cuenta de la relevancia que tiene *unittest* en este marco (pese a no ser el escogido). Cabe destacar también la importancia de pensar no solo en la facilidad de uso, sino en la sencillez de comprensión de cara a alguien que no sea el desarrollador del proyecto, el cual es uno de los motivos por los que he hecho mi decisión.
* Uno de los errores más importantes ha sido confundir *unittest* con un marco de pruebas (aunque cabe destacar que en Python estos conceptos van prácticamente entrelazados, por lo que consultar cualquier información puede llevar a un planteamiento erróneo). Tras investigar diversos frameworks de testeo, he podido observar por qué *pytest* realmente ha supuesto una revolución en este ámbito, y que existen otras herramientas con diversas características que pueden ser realmente útil dependiendo del enfoque y proyecto.
* Se ha tratado de seguir buenas prácticas a la hora de realizar commits, crear issues, enlazar historias de usuario, etc. Enlazar pequeños cambios por mucho que afecten a diversas cosas no tiene sentido, es mejor enfocar dicho cambio donde se produce. 
* Como detalle más importante, tras un primer planteamiento completamente erróneo de como se debe plantear un desarrollo basado en test, y numerosas malas prácticas, he comprendido el fin real del desarrollo basado en pruebas, y como este enfoque ayuda a obtener finalmente un desarrollo robusto, seguro y de mayor calidad. También me ha hecho comprender que un test no necesita ser excesivamente complejo ni detallado, sino comprobar lo que es realmente se necesita sin redundancias.
* Se ha tenido en cuenta el poder facilitar la corrección del mismo, indicando clara y ordenadamente dónde se encuentra cada información, una justificación lo más clara posible e indicar las distintas rúbricas a tener en cuenta.


