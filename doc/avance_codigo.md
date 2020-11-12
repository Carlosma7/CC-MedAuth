## Avance del proyecto

---

Para el desarrollo del proyecto se ha realizado un desarrollo basado en test ([TDD](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas)) el cual nos va a permitir diseñar nuestro producto con la certeza de que cada funcionalidad que se realizar es correcta sintáctica y lógicamente.

Para el avance en búsqueda de la consecución de un *M.V.P.* se ha realizado primero el diseño completo de las clases que componen las entidades del sistema, y a continuación, se han diseñado en un controlador de lógica de negocio las distintas funcionalidades asociadas a las historias de usuario:

* **Administración de pólizas** (requiere usuarios)
    * [TestUsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testUsuarioAdmin.py) y [UsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioAdmin.py).
    * [TestUsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testUsuarioCliente.py) y [UsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioCliente.py)
    * Historias de usuario que se resuelven:
        * [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema](https://github.com/Carlosma7/MedAuth/issues/43): Método [crear_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L19) y test [test_crear_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L11).
        * [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema.](https://github.com/Carlosma7/MedAuth/issues/44): Método [crear_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L33) y test [test_crear_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L20).
        * [Como administrativo quiero gestionar los usuarios existentes en el sistema para modificar o eliminar usuarios.](https://github.com/Carlosma7/MedAuth/issues/55): Métodos [modificar_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L41), [modificar_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L54), [eliminar_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L66) y [eliminar_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L74) y sus respectivos tests [test_modificar_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L29), [test_modificar_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L37) y [test_eliminar_admin](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L46) y [test_eliminar_cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L54).
    * [TestPoliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testPoliza.py) y [Poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/poliza.py).
    * Historias de usuario que se resuelven:
        *  [Como administrativo quiero administrar la póliza de un asegurado para crear, modificar o dar de baja una póliza](https://github.com/Carlosma7/MedAuth/issues/35): Métodos [crear_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L81), [modificar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L103) y [desactivar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L122) y sus respectivos tests [test_crear_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L62), [test_modificar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L74) y [test_desactivar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L99).
        * [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada](https://github.com/Carlosma7/MedAuth/issues/34): Método [consultar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L129) y test [test_consultar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L89).

* **Administración de autorizaciones** (requiere modelo de prescripciones):
    * [TestPrescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testPrescripcion.py) y [Prescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/prescripcion.py).
    * [TestAutorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testAutorizacion.py) y [Autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/autorizacion.py).

* **Administración de citas médicas**:
    * [TestCita](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testCita.py) y [Cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/cita.py).

Además, se han utilizado clases **enum** para la representación de determinadas informaciones como:
* [Tipo de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/tipoPoliza.py).
* [Módulo extra de póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/moduloExtra.py)
* [Especialidad médica](https://github.com/Carlosma7/MedAuth/blob/main/src/core/especialidad.py)
