# Servicio de solicitudes de autorizaciones médicas

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/) [![Versions](https://img.shields.io/badge/Python-3.6|3.7|3.8|3.9-red.svg)](https://www.python.org/downloads/release/python-360/) [![Build Test](https://img.shields.io/travis/Carlosma7/CC-MedAuth/main)](https://travis-ci.org/github/Carlosma7/CC-MedAuth) 

---

**Autor:** Carlos Morales Aguilera

**Asignatura:** Cloud Computing

**Universidad:** Universidad de Granada (UGR)

## Descripción de problema y solución del proyecto

---

La descripción detallada del problema y la solución propuesta se puede leer [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/descripcion_problema.md).

## Arquitectura

---

La elección y justificación de la arquitectura planteada se puede leer [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/arquitectura.md).

## Herramientas

---

La justificación de la elección de las herramientas propuestas se puede ver [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/justificacion_herramientas.md).

## Roadmap

---

El Roadmap y la planificación del proyecto se pueden ver [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/roadmap.md).


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
