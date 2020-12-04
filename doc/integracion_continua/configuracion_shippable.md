## Shippable

### Configuración Shippable

[![Run Status](https://api.shippable.com/projects/5fca65728d5266000640fc4c/badge?branch=main)](https://app.shippable.com/github/Carlosma7/MedAuth/dashboard/jobs)

Para poder configurar Shippable, se deben seguir los siguientes pasos:

1. Darse de alta.

	![Shippable Auth](../img/shippable_auth.png "Shippable Auth")
	
2. A continuación, aceptaremos los permisos solicitados por la aplicación de *Shippable*.

	![Shippable Permissions](../img/shippable_permissions.png "Shippable Permissions")

3. Para poder activar la integración continua en el proyecto hay que dirigirse a la plataforma de *Shippable*, y una vez dentro seleccionar en el menú lateral izquierdo el botón ```GitHub```, y posteriormente el botón de nuestro usuario, en este caso ```Carlosma7```:

	![Shippable Menu](../img/shippable_start_menu.png "Shippable Menu")

4. Se nos muestra la pantalla de proyectos, seleccionaremos el botón ```Enable a project```.

	![Shippable Projects](../img/shippable_projects.png "Shippable Projects")

5. Se muestra una lista de los repositorios, donde activaremos nuestro proyecto:

	![Shippable Enable Project](../img/shippable_enable_project.png "Shippable Enable Project")

6. Dirigiéndonos de nuevo a la sección de proyectos, podemos observar que se ha configurado correctamente el proyecto, y está a la espera de la realización de un primer *push*. Aquí se configurará el fichero **shippable.yml** para que se realice la *CI* en los *push* que se realicen en el proyecto.

	![Shippable Works](../img/shippable_funciona.png "Shippable Works")

7. Tras añadir la configuración correcta del fichero **shippable.yml**, se puede observar que finalmente *Shippable* realiza correctamente la integración continua:

	![Shippable On](../img/shippable_bien.png "Shippable On")
