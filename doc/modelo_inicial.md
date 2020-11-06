## Modelos

---

Se han creado los modelos y controladores asociados a las entidades identificadas en la primera fase:

* [Usuario](https://github.com/Carlosma7/MedAuth/tree/main/src/models/usuario)
    * [Modelo: Usuario](https://github.com/Carlosma7/MedAuth/blob/main/src/models/usuario/usuario.py)
    * [Controlador: UsuarioController](https://github.com/Carlosma7/MedAuth/blob/main/src/models/usuario/usuarioController.py)

* [Póliza](https://github.com/Carlosma7/MedAuth/tree/main/src/models/poliza)
    * [Modelo: Poliza](https://github.com/Carlosma7/MedAuth/blob/main/src/models/poliza/poliza.py)
    * [Controlador: PolizaController](https://github.com/Carlosma7/MedAuth/blob/main/src/models/poliza/polizaController.py)

* [Prescripción](https://github.com/Carlosma7/MedAuth/tree/main/src/models/prescripcion)
    * [Modelo: Prescripcion](https://github.com/Carlosma7/MedAuth/blob/main/src/models/prescripcion/prescripcion.py)
    * [Controlador: PrescripcionController](https://github.com/Carlosma7/MedAuth/blob/main/src/models/prescripcion/prescripcionController.py)

* [Autorización](https://github.com/Carlosma7/MedAuth/tree/main/src/models/autorizacion)
    * [Modelo: Autorizacion](https://github.com/Carlosma7/MedAuth/blob/main/src/models/autorizacion/autorizacion.py)
    * [Controlador: AutorizacionController](https://github.com/Carlosma7/MedAuth/blob/main/src/models/autorizacion/autorizacionController.py)

* [Cita](https://github.com/Carlosma7/MedAuth/tree/main/src/models/cita)
    * [Modelo: Cita](https://github.com/Carlosma7/MedAuth/blob/main/src/models/cita/cita.py)
    * [Controlador: CitaController](https://github.com/Carlosma7/MedAuth/blob/main/src/models/cita/citaController.py)

Se puede comprobar que son sintácticamente correctas ejecutando:

```bash
python -m py_compile <class>
```

Por ejemplo:

```bash
python -m py_compile src/models/usuario.py
```

Y se puede comprobar la correcta integración de los modelos, y por tanto, asegurarnos de la corrección sintáctica de los archivos ejecutando:

```bash
python src/main.py
```
