
## Roadmap

---

El plan de desarrollo del proyecto va a seguir una serie de etapas que irán añadiendo determinadas funcionalidades y herramientas para poder desarrollar un *producto mínimo viable* en cada entrega, que se irá desarrollando en las distintas etapas y que añadirá nueva funcionalidad de forma consecuente a cada fase del desarrollo.

1. :heavy_check_mark: **Fase inicial**: En una primera entrega del desarrollo, se constará de un esquema inicial del proyecto, en el que se determinarán las entidades iniciales con las que se han de trabajar en el problema, indicar que funcionalidades poseen y diseñar una clase inicial para dichas entidades, de forma que quede una estructura inicial a seguir en el desarrollo.

	En esta primera fase se relacionan las clases diseñadas a las distintas *historias de usuario* de todos los *milestones* del proyecto, ya que es necesario definir el esquema inicial:
    
	* Entidad usuario:
		* [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema.](https://github.com/Carlosma7/MedAuth/issues/43)
		* [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema.](https://github.com/Carlosma7/MedAuth/issues/44)
	* Entidad póliza:
		* [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada.](https://github.com/Carlosma7/MedAuth/issues/34)
	* Entidad prescripción:
		* [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica.](https://github.com/Carlosma7/MedAuth/issues/36)
	* Entidad autorización: 
		* [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico.](https://github.com/Carlosma7/MedAuth/issues/37)
	* Entidad cita:
		* [Como asegurado quiero consultar una cita médica fijada para ver la información asociada.](https://github.com/Carlosma7/MedAuth/issues/41)

2. :heavy_check_mark: **Segunda fase**: En esta entrega de un nuevo producto mínimo viable, se empiezan a desarrollar las primeras tareas de gestión administrativa de los distintos componentes del sistema de administración de pólizas, que permite gestión de información de usuarios y pólizas (no es relativo a sistema de login). Además se introduce un entorno de testeo adecuado que permita comprobar que las tareas de desarrollo realizadas se desenvuelven correctamente.

    Inicialmente se realizará toda la funcionalidad de [administración de pólizas](https://github.com/Carlosma7/MedAuth/milestone/10) relativa a usuarios:
    * [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema.](https://github.com/Carlosma7/MedAuth/issues/43)
    * [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema.](https://github.com/Carlosma7/MedAuth/issues/44)
    * [Como administrativo quiero gestionar los usuarios existentes en el sistema para modificar o eliminar usuarios.](https://github.com/Carlosma7/MedAuth/issues/55)
    
    A continuación se realizará la administración de la funcionalidad de pólizas:
    * [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada.](https://github.com/Carlosma7/MedAuth/issues/34)
    * [Como administrativo quiero administrar la póliza de un asegurado para crear, modificar o dar de baja una póliza.](https://github.com/Carlosma7/MedAuth/issues/35)
    
    
3. :heavy_check_mark: **Tercera fase**: En esta entrega, se realizará el otro núcleo que compone la administración completa del sistema, obteniendo un producto viable que obtenga la funcionalidad completa administrativa del sistema. Para ello se requieren las gestiones administrativas previas para el orden lógico del sistema:

    En primera instancia, se realizará la [administración de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/9), la cual depende de la gestión de pólizas anteriormente mencionada:
    * [Como administrativo quiero administrar una autorización médica de un asegurado para ver o modifcar una autorización.](https://github.com/Carlosma7/MedAuth/issues/39)
    * [Como administrativo quiero cambiar la aprobación o denegación de una autorización para tratar un caso excepcional.](https://github.com/Carlosma7/MedAuth/issues/40)
    
    Finalmente, se realizará la [administración de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/11), las cuales son creadas tras las autorizaciones:
    * [Como administrativo quiero administrar una cita médica para crear una cita o modificar información asociada a una cita existente.](https://github.com/Carlosma7/MedAuth/issues/49)
    
4. :heavy_check_mark: **Cuarta fase**: En esta fase se añaden las funcionalidades asociadas a la gestión de una cita médica y una autorización médica. En esta fase además se cumplen los requisitos administrativos previos para poder gestionar por la parte administrativa los distintos elementos a tratar.

    Inicialmente, se realizará la [gestión de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/7), preparando el escenario para desarrollar en un futuro la solicitud de autorizaciones con toda la funcionalidad previa necesaria:
    * [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica.](https://github.com/Carlosma7/MedAuth/issues/36)
    * [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización.](https://github.com/Carlosma7/MedAuth/issues/38)
    
    Posteriormente, tras dotar al sistema de la funcionalidad de cara al cliente para gestionar autorizaciones, se añadiran las funcionalidades básicas de [gestión de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/8):
    * [Como asegurado quiero consultar una cita médica fijada para ver la información asociada.](https://github.com/Carlosma7/MedAuth/issues/41)
    
5. :heavy_check_mark: **Quinta fase**: En esta entrega, se añaden las funcionalidades que intercomunican todos los elementos anteriormente definidos y desarrollados, añadiendo las funcionalidades de solicitud de autorización médica y los cambios que implican en el sistema. Se añaden también funcionalidades relativas a notificación del usuario sobre citas médicas.

    Para realizar el proceso completo de [gestión de autorizaciones](https://github.com/Carlosma7/MedAuth/milestone/7), se añade el procedimiento de solicitud:
    * [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico.](https://github.com/Carlosma7/MedAuth/issues/37)

    Relacionado con la [administración de pólizas](https://github.com/Carlosma7/MedAuth/milestone/10), se añade la consulta de un usuario, no contemplada hasta el momento:
    * [Como administrativo quiero consultar un usuario para poder ver la información asociada](https://github.com/Carlosma7/MedAuth/issues/96)

6. **Sexta fase**: En esta fase, se añaden las últimas funcionalidades asociadas a la gestión de citas por parte del asegurado, dotándole de capacidad para gestionar las citas y ser notificado.

    Para realizar el proceso completo de [gestión de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/8), se añade el procedimiento de solicitud:
    * [Como asegurado quiero solicitar una cita para poder registrar una consulta o intervención](https://github.com/Carlosma7/MedAuth/issues/97)

    Por último, además de haber conectado toda la funcionalidad anterior del sistema, se añade un extra de [gestión de citas médicas](https://github.com/Carlosma7/MedAuth/milestone/8) como es la notificación previa a una cita por correo:
    * [Como asegurado quiero ser notificado para saber cuando debo asistir a una cita médica.](https://github.com/Carlosma7/MedAuth/issues/42)


### Avances

1. [Primer avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo) que corresponde con las entregas de la primera y segunda fase.
2. [Segundo avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo_2) que corresponde con la entrega de la tercera fase.
3. [Tercer avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo_3) que corresponde con la entrega de la cuarta fase.
4. [Cuarto avance](https://carlosma7.github.io/MedAuth/doc/avance_codigo_4) que corresponde con la entrega de la quinta fase.

