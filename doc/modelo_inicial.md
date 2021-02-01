
## Modelos

---

El proyecto sigue la siguiente estructura:

```
src/
├── client.py
├── core
│   ├── api.py
│   ├── autorizacion.py
│   ├── cita.py
│   ├── controlador.py
│   ├── especialidad.py
│   ├── excepciones.py
│   ├── main.py
│   ├── moduloExtra.py
│   ├── poliza.py
│   ├── prescripcion.py
│   ├── server.py
│   ├── tipoPoliza.py
│   ├── usuarioAdmin.py
│   ├── usuarioCliente.py
│   └── usuario.py
└── test
    ├── testApi.py
    ├── testAutorizacion.py
    ├── testBD
    │   └── testBD.py
    ├── testCita.py
    ├── testControlador.py
    ├── testPoliza.py
    ├── testPrescripcion.py
    ├── testUsuarioAdmin.py
    ├── testUsuarioCliente.py
    └── testUsuario.py
```

Se han creado los modelos y el controlador asociado a la lógica de negocio de las siguientes entidades:

* **Core**

    * [Controlador](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py)
    * [API](https://github.com/Carlosma7/MedAuth/blob/main/src/core/api.py) 
    * [Server](https://github.com/Carlosma7/MedAuth/blob/main/src/core/server.py)

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
	* [testBD](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testBD/testBD.py)
* [Cliente](https://github.com/Carlosma7/MedAuth/blob/main/src/client.py)

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

