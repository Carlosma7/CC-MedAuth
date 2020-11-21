
## Avance del proyecto

---

Tras realizar el [primer avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo), en el que se realizaron las tareas de administración de pólizas, y en la que se definían los modelos de las distintas entidades a tratar en el proyecto, se debía avanzar el proyecto según el [roadmap](https://carlosma7.github.io/MedAuth/doc/roadmap) realizando las distintas operaciones de **administración de autorizaciones** y **administración de citas médicas**:

* **Administración de autorizaciones** (requiere administración de usuarios y pólizas)
	* Historias de usuario que se resuelven:
		* [Como administrativo quiero administrar una autorización médica de un asegurado para crear, ver o modifcar una autorización](https://github.com/Carlosma7/MedAuth/issues/39): Métodos [crear_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L144), [modificar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L170)  y sus respectivos tests [test_crear_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L113), [test_modificar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L129).
		* [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización](https://github.com/Carlosma7/MedAuth/issues/38): Método [consultar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L185) y test [test_consultar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L143).
		* [Como administrativo quiero cambiar la aprobación o denegación de una autorización para tratar un caso excepcional](https://github.com/Carlosma7/MedAuth/issues/40): Método [aprobar_denegar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L193) y test [test_aprobar_denegar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L155).

* **Administración de citas** (requiere administración de autorizaciones)
	* Historias de usuario que se resuelven:
		* [Como administrativo quiero administrar una cita médica para crear una cita o modificar información asociada a una cita existente](https://github.com/Carlosma7/MedAuth/issues/49): Métodos [crear_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L204), [modificar_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L212)  y sus respectivos tests [test_crear_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L169), [test_modificar_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L185).
		* [Como asegurado quiero consultar una cita médica fijada para ver la información asociada](https://github.com/Carlosma7/MedAuth/issues/41): Método [consultar_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L225) y test [test_consultar_cita](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L198).
