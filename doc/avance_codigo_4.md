## Avance del proyecto

---

Tras realizar los anteriores avances, se debía avanzar el proyecto según el [roadmap](https://carlosma7.github.io/MedAuth/doc/roadmap) realizando las distintas operaciones de **gestión de autorizaciones** y **administración de pólizas**:

* **Gestión de autorizaciones** (requiere administración de usuarios, pólizas y autorizaciones)
	* Historias de usuario que se resuelven:
		* [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico](https://github.com/Carlosma7/MedAuth/issues/37): Método [solicitar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L204)  y su test [test_solicitar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L193).

* **Administración de pólizas**
	* Historias de usuario que se resuelven:
		* [Como administrativo quiero consultar un usuario para poder ver la información asociada](https://github.com/Carlosma7/MedAuth/issues/96): Método [consultar_usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L355) y test [test_consultar_usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L376).

### Mejoras respecto al avance anterior
Durante las correcciones de compañeros, y consideraciones propias, se han realizado los siguientes cambios:

1. **Creación de clases específicas de excepciones**: Se pueden observar en [excepciones.py](https://github.com/Carlosma7/MedAuth/blob/main/src/core/excepciones.py) realizando una seria de clases de excepciones sencillas, que indican que tipo de excepción se produce.
2. **Modificación de métodos que realizaban modificaciones sobre objetos existentes**: Anteriormente se utilizaba un objeto para obtener su *ID* y modificar el correspondiente almacenado en la práctica, lo cual, lejos de ser una buena práctica, aumenta el coste computacional y dificultaba el diseño de la API, por lo que se ha modificado para trabajar únicamente con los identificadores.
3. **Nuevas HUs**: Tras revisar el estado actual del proyecto, se han encontrado dos funcionalidades no contempladas previamente, las cuales se añaden, y se ha implementado una de ellas. Dichas *HU* se pueden ver [[HU14] Consultar usuario](https://github.com/Carlosma7/MedAuth/issues/96) y [# [HU15] Solicitar una cita](https://github.com/Carlosma7/MedAuth/issues/97).
4. **Se ha desarrollado un contenedor de despliegue**: Si bien es uno de los puntos que corresponden a esta rúbrica, se ha detallado más detenidamente [aquí](https://carlosma7.github.io/MedAuth/doc/api/despliegue).

### Mejoras tras correcciones

Tras la primera corrección se han realizado las siguientes correcciones:

1. **Correcciones sobre la API** ([issue](https://github.com/Carlosma7/MedAuth/issues/99)): Se han eliminado los verbos en las órdenes HTTP. Se usan los métodos correctos para modificar partes de recursos.

2. **Correcciones sobre el log** ([issue](https://github.com/Carlosma7/MedAuth/issues/100)): Se ha implementado un middleware encargado de realizar funciones de logging.

3. **Nuevo estudio sobre framework** ([estudio](https://carlosma7.github.io/MedAuth/doc/api/estudio_framework)): En este nuevo estudio se consideran implementaciones de un mismo método de la API del proyecto y se evalúan aspectos técnicos. Se consideran menos opciones, pero sí más realistas con la naturaleza y necesidades del proyecto.

4. **Asociación de tests a HU**: Anteriormente se relacionaban con un issue genérico, a partir de ahora se relacionarán con las HU directamente.

