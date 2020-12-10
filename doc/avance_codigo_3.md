## Avance del proyecto

---

Tras realizar el [primer avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo) y el [segundo avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo_2), se debía avanzar el proyecto según el [roadmap](https://carlosma7.github.io/MedAuth/doc/roadmap) realizando las distintas operaciones de **administración de autorizaciones** y **administración de citas médicas**:

* **Gestión de autorizaciones** (requiere administración de usuarios, pólizas y autorizaciones)
	* Historias de usuario que se resuelven:
		* [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización](https://github.com/Carlosma7/MedAuth/issues/38): Método [consultar_autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L244)  y su test [test_consultar_poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L243).
		* [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica](https://github.com/Carlosma7/MedAuth/issues/36): Método [subir_prescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L167) y test [test_subir_prescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py#L167).

### Mejoras tras correcciones

Durante las correcciones previas se sugirieron las siguientes consideraciones:

1. **Jerarquización de las clases de usuario**: Se comentó que las clases *UsuarioAdmin* y *UsuarioCliente* poseían atributos en común, y los métodos de gestión de los mismos eran una clara repetición de código, por lo que se ha optado por hacer uso del **polimorfismo**, y crear una clase genérica [Usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuario.py), de la cual heredan información las clases [UsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioAdmin.py) y [UsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioCliente.py). 

	Además, para el almacenamiento de usuarios se ha optado por una [lista de usuarios](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L20) que engloba ambos tipos, en lugar de dos listas separadas para cada tipo.

	Por último, se han unificado los métodos *crear_admin*, *crear_cliente*, *modificar_admin*, *modificar_cliente*, *eliminar_admin* y *eliminar_cliente* en los métodos [crear_usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L26), [modificar_usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L67), [eliminar_usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L91).
	
2. **Establecer formatos de atributos**: Se comentó que en ningún momento se comprobaba que la información introducida siguiera un formato, por lo que se podía introducir un *DNI*, *Email* o *IBAN* incorrecto. Para ello, se han establecido comprobaciones mediante expresiones regulares para los siguientes elementos de la forma:

    * [DNI](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L34): ```"[0-9]{8}-[A-Z]"```, la cual comprueba que el *DNI* posea 8 dígitos y una letra mayúscula.
    * [Email](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L36): ```"([a-zA-Z0-9]+@[a-zA-Z]+\.)(com|es)"```, la cual comprueba que siga el formato ```usuario@dominio.com```, permitiendo que existan números en la dirección, y de momento solo se contemplan los dominios terminados en *.com* o *.es*.
    * [IBAN](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L47): ```"ES[0-9]{22}"```, la cual comprueba el formato de *ES* seguido de 22 dígitos, aunque en un supuesto más realista, supondría desglosar las diferentes partes del código, pero de momento ya se contempla un formato más aproximado.

3. **Excepciones**: Se comentó que no se contemplaban excepciones en ninguna parte del programa, por lo que se ha decidido implementar las siguientes excepciones de acuerdo a los requisitos del proyecto:

    * [DNI incorrecto](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L61): ```'DNI not valid.'```
    * [Email incorrecto](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L59):```'Email not valid.'``` 
    * [Tipo de usuario incorrecto](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L53): ```'Wrong user type.'```
    * [IBAN incorrecto](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L51):```'IBAN not valid.'```
    * Inexistencia de un elemento: ```'User doesn´t exist.'```, ```'Policy doesn´t exist.'```, entre otros, donde se comprueba que un determinado objeto exista en el sistema.
    * Existencia de un elemento: ```'An user exists with DNI provided.'``` cuando se intenta crear un usuario con un *DNI* registrado, se puede ver [aquí](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py#L64).
    * Asociaciones entre objetos: ```'The prescription is not associated with the active policy.'```, ```'The authorization is not associated with the active policy.'```, donde se comprueba que una prescripción o autorización se intenta crear con una póliza inactiva o inexistente.

