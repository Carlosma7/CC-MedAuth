# Servicio de solicitudes de autorizaciones médicas

---

**Autor:** Carlos Morales Aguilera

**Asignatura:** Cloud Computing

**Universidad:** Universidad de Granada (UGR)

## Configuración inicial del repositorio

---

La configuración del entorno de Git y Github en mi máquina local se puede visualizar [aquí](https://github.com/Carlosma7/CC-MedAuth/blob/main/doc/config_entorno.md).

## Descripción del problema

---

Hoy en día cada vez es más normal la inclusión de sistemas y aplicaciones informáticas en las gestiones bancarias, burocráticas, etc. Sin embargo, estas tecnologías no están completamente incorporadas en empresas de seguros de salud, donde para realizar autorizaciones de operaciones, intervenciones o pruebas de diagnóstico, la mayoría de las gestiones se han de realizar de forma presencial en una oficina con un empleado de la empresa realizando dicha autorización, y con el paciente presentando la prescripción del médico correspondiente. Las citas médicas por otro lado no quedan almacenadas en ningún sitio visible para el paciente, el cual tendría que llamar por teléfono si quiere recordar algún dato sobre la misma.

Además, pese a la situación actual del Covid-19, muchas empresas se han visto obligadas a trabajar de forma telemática, mientras que bastantes empresas de salud han tenido que mantener a su personal de forma presencial y expuesta debido a su poca innovación en dicho campo.


## Descripción de la solución

---

La idea propuesta consiste en crear un sistema que actúe de plataforma en la que los distintos asegurados puedan registrarse con su información personal y de póliza de asegurado, en la que puedan consultar las distintas citas médicas que tengan, y a su vez, si un doctor le ha prescrito alguna intervención o prueba, puedan solicitarla para su aprobación y asignación de cita. Para ello se planteará una gestión de usuarios, de pólizas y base de datos para almacenar las distintas citas médicas que se soliciten junto a las prescripciones de los médicos.

De esta forma, la gestión de una autorización médica podría ser realizada de forma no presencial y en periodo más breve, no siendo necesario que el paciente dedique tiempo a ir a la oficina, y a la vez el empleado encargado pueda realizar su labor de forma más eficiente e incluso de forma telemática.
