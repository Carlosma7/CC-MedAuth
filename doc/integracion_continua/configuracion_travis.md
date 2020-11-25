## TravisCI

### Configuración Travis 

[![Build Status](https://travis-ci.com/Carlosma7/MedAuth.svg?branch=main)](https://travis-ci.com/Carlosma7/MedAuth)

Para poder configurar Travis, se deben seguir los siguientes pasos:

1. Darse de alta. (En mi caso lo hice al inicio del proyecto como se pedía en los ejercicios, pero por desconocimiento lo realicé en **Travis-ci.org**, por lo que posteriormente habrá que migrar a **Travis-ci.com**).

	![Travis](../img/travis.png "Travis")

2. Activar el repositorio en el que se vaya a aplicar la integración continua. (El repositorio actualmente se llama *MedAuth*, pero cuando se realizó el procedimiento se llamaba *CC-MedAuth*, aunque esto no afecta a la configuración).

	![Integración continua](../img/travis2.png "Integración continua")

3. Tal y como se puede leer en este [newsletter de Travis](https://mailchi.mp/3d439eeb1098/travis-ciorg-is-moving-to-travis-cicom), *Travis-ci.org* va a ser apagado el 31 de diciembre de este año, y se trabajará únicamente con *Travis-ci.com*, por lo que para ello hay que dirigirse a dicha plataforma, y al igual que en el primer paso, registrarse con *GitHub*:

	![Travis-ci.com](../img/travis_com.png "Travis-ci.com")

4. Una vez ya está dado de alta, se procede a conectar Travis a nuestro perfile de *GitHub*, para ello en la pantalla inicial de *Travis* (a partir de este punto nos referiremos siempre a *Travis-ci.com* como *Travis*) seleccionaremos la opción ```Activate all repositories using GitHub App```:

	![Travis Activate Repositories](../img/travis_activate_repos.png "Travis Activate Repositories")

5. Dar permiso e installar:

	![Travis Install](../img/travis_install.png "Travis Install")

6. A continuación se visualizan los repositorios en *Travis*, menos el repositorio del proyecto, ya que esté no ha sido migrado, para ello nos dirigiremos a nuestro Perfil -> *Settings*, y una vez allí nos dirigiremos a la pestaña ```Migrate```. Una vez allí seleccionaremos el repositorio y seleccionaremos en ```Migrate selected repositories to travis-ci.com```:

	![Travis Migrate Repo](../img/travis_migrate_repo.png "Travis Migrate Repo")

7. Confirmamos seleccionando ```Migrate```.

	![Travis Migrate Auth](../img/travis_migrate_auth.png "Travis Migrate Auth")
	
8. Podemos observar que se ha configurado correctamente ya que se pueden observar todos los *builds* previos:

	![Travis Setup Ok](../img/travis_setup_ok.png "Travis Setup Ok")
