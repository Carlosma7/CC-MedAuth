## Dockerhub

---

Para contenerizar el proyecto se utilizará el servicio de host de repositorios [Docker Hub](https://hub.docker.com/). Para ello hay que darse de alta como usuario y crear el repositorio, y a continuación sincronizar de forma automática los *build* de la imagen al actualizar la información en el repositorio de *github*.

### Subir el contenedor

Para poder realizar una subida de la imagen creada a *Docker Hub*, primero se ha creado el [repositorio](https://hub.docker.com/r/carlosma7/medauth). A continuación, se ha seguido este [tutorial](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html) para realizar la primera subida del proyecto, distinguiéndola con el tag [firsttry](https://hub.docker.com/layers/carlosma7/medauth/firsttry/images/sha256-ed008bded4ee57521e3b1f8b381ec8dbba52ce13728eb16e21037d497c3f8050) (esta imagen es previa a las optimizaciones y buenas prácticas, por ese motivo se etiquetó de forma separada para este ejemplo, no se usa).

Para poder subir el contenedor, se han seguido los siguientes pasos:

1. Se ha logueado el usuario con la orden ```docker login --username=carlosma7```.
![Login Docker Hub](../img/login_hub.png "Login Docker Hub")

2. Se ha creado la imagen y se comprueba con ```docker images```.
![Imagen Docker](../img/docker_image_created.png "Imagen Docker")

3. Se etiqueta la imagen con el tag deseado de subida, en este caso, *carlosma7/medauth:firsttry*.

4. Push de la imagen al repositorio creado con ```docker push carlosma7/medauth:firsttry```.
![Imagen firsttry](../img/docker_hub_firsttry.png "Imagen firsttry")

Este mismo proceso se ha seguido a la hora de crear la versión actual del proyecto, etiquetada como **latest**.
![Imagen latest](../img/docker_hub_latest.png "Imagen latests")

### Automización de builds

Se pretende automatizar el proceso de *build* de la imagen respecto a las actualizaciones que se realicen en el [repositorio de Github](https://github.com/Carlosma7/MedAuth), para ello *Docker Hub* ofrece una automatización de este procedimiento. Para realizar este procedimiento se ha seguido este [tutorial](https://docs.docker.com/docker-hub/builds/#autobuild-for-teams).

Para poder automatizar este procedimiento, se han seguidos los siguientes pasos:

1. Dirigirse al [repositorio en Docker Hub](https://hub.docker.com/r/carlosma7/medauth).
![Repositorio Docker Hub](../img/docker_hub_repo.png "Repositorio Docker Hub")

2. Una vez en el repositorio, se selecciona la sección **builds**.
![Sección Build](../img/docker_hub_build.png "Sección Build")

3. Se selecciona en *Link to Github* y se nos despliega la siguiente pantalla de configuración:
![Configuración automatización Docker Hub](../img/docker_hub_conf.png "Configuración automatización Docker Hub")

4. Se selecciona el usuario y repositorio de *Github*.
5. **No** se selecciona la opción *Autotest*, ya que de momento no se considera un escenario en el que se realicen *Pull Requests* sobre el repositorio.
6. **No** se selecciona la opción *Repository Links*, ya que no se desea que se realice un build si se actualiza la imagen base del proyecto (*python:3.8-slim*).
7. Se indica la rama de *Github* que se utilizará como fuente del repositorio del que obtener la información. En este caso se selecciona la rama *main*.
8. Por último, se presiona en *Save and Build*.

Tras realizar todo este procedimiento, cada vez que se realice un *Push* en *Github*, se creará el *build* correspondiente en *Docker Hub*. A continuación se muestra un ejemplo de un *build* realizado de forma automática:

![Build Automático](../img/docker_hub_auto.png "Build Automático")
