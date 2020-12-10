## Modelos

---

El proyecto sigue la siguiente estructura:

```
src
 ├── core
 │   ├── autorizacion.py
 │   ├── cita.py
 │   ├── controlador.py
 │   ├── especialidad.py
 │   ├── moduloExtra.py
 │   ├── poliza.py
 │   ├── prescripcion.py
 │   ├── tipoPoliza.py
 │   ├── usuario.py
 │   ├── usuarioAdmin.py
 │   └── usuarioCliente.py
 ├── main.py
 └── test
     ├── testAutorizacion.py
     ├── testCita.py
     ├── testControlador.py
     ├── testPoliza.py
     ├── testPrescripcion.py
     ├── testUsuario.py
     ├── testUsuarioAdmin.py
     └── testUsuarioCliente.py



```

Se han creado los modelos y el controlador asociado a la lógica de negocio de las siguientes entidades:

* **Core**

    * [Controlador](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py)

    * *Modelos*
    
        * [TipoPoliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/tipoPoliza.py)
        * [ModuloExtra](https://github.com/Carlosma7/MedAuth/blob/main/src/core/moduloExtra.py)
        * [Especialidad](https://github.com/Carlosma7/MedAuth/blob/main/src/core/especialidad.py)
        * [Usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuario.py)
        * [UsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioAdmin.py)
        * [UsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/usuarioCliente.py)
        * [Póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/poliza.py)
        * [Prescripción](https://github.com/Carlosma7/MedAuth/blob/main/src/core/prescripcion.py)
        * [Autorización](https://github.com/Carlosma7/MedAuth/blob/main/src/core/autorizacion.py)
        * [Cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/cita.py)

* **Test**
	* [testControlador](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py)
	
	* *Test*
		* [testUsuario](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testUsuario.py)
		* [testUsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testUsuarioAdmin.py)
		* [testUsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testUsuarioCliente.py)
		* [testPoliza](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testPoliza.py)
		* [testPrescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testPrescripcion.py)
		* [testAutorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testAutorizacion.py)
		* [testCita](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testCita.py)

Se puede comprobar que son sintácticamente correctas ejecutando:

```bash
python3 -m py_compile <class>
```

Por ejemplo:

```bash
python3 -m py_compile src/core/poliza.py
```

Y se puede comprobar la correcta integración de los modelos, y por tanto, asegurarnos de la corrección sintáctica de los archivos ejecutando:

```bash
python3 src/main.py
```
