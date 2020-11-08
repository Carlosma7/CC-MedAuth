## Modelos

---

El proyecto sigue la siguiente estructura:

```
core
    ├── controlador.py
    ├── __init__.py
    └── modelos
        ├── autorizacion.py
        ├── cita.py
        ├── especialidad.py
        ├── __init__.py
        ├── moduloExtra.py
        ├── poliza.py
        ├── prescripcion.py
        ├── tipoPoliza.py
        ├── usuarioAdmin.py
        ├── usuarioCliente.py
        └── usuario.py
```

Se han creado los modelos y el controlador asociado a la lógica de negocio de las siguientes entidades:

* **Core**

    * [Controlador](https://github.com/Carlosma7/MedAuth/blob/main/src/core/controlador.py)
    
    * [__init__](https://github.com/Carlosma7/MedAuth/blob/main/src/core/__init__.py)

    * *Modelos*
    
        * [TipoPoliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/tipoPoliza.py)
        * [ModuloExtra](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/moduloExtra.py)
        * [Especialidad](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/especialidad.py)
        
        * [Usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/usuario.py)
        * [UsuarioAdmin](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/usuarioAdmin.py)
        * [UsuarioCliente](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/usuarioCliente.py)
        
        * [Póliza](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/poliza.py)
        
        * [Prescripción](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/prescripcion.py)
        
        * [Autorización](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/autorizacion.py)
        
        * [Cita](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/cita.py)
        
        * [__init__](https://github.com/Carlosma7/MedAuth/blob/main/src/core/modelos/__init__.py)

Se puede comprobar que son sintácticamente correctas ejecutando:

```bash
python3 -m py_compile <class>
```

Por ejemplo:

```bash
python3 -m py_compile src/core/modelos/poliza.py
```

Y se puede comprobar la correcta integración de los modelos, y por tanto, asegurarnos de la corrección sintáctica de los archivos ejecutando:

```bash
python3 src/main.py
```
