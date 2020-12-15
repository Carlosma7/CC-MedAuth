## Aprovechamiento del contenedor Docker del proyecto en Integración Continua

De las herramientas de *CI* propuestas, se ha decidido utilizar el contenedor *Docker* del proyecto, cuyo *Dockerfile* se puede ver [aquí](https://github.com/Carlosma7/MedAuth/blob/main/Dockerfile) para las opciones de **CircleCI** y **GitHub Actions**.

### CircleCI

Una de las ventajas que se ofrecen es utilizar el propio contenedor como entorno de test del proyecto, para ello, en lugar de indicar uno de los contenedores propios que ofrece **CircleCI**, y realizar las instalaciones y operaciones necesarias, directamente se aprovecha el contenedor del proyecto, el cual ya tiene las herramientas instaladas para poder realizar los tests, esto se puede observar dentro del fichero de configuración [config.yml](https://github.com/Carlosma7/MedAuth/blob/main/.circleci/config.yml).

```yaml
docker:
            # Project's Docker image in Docker Hub
            - image: carlosma7/medauth:latest
```

El claro ejemplo de aprovechamiento es que el contenedor ya posee las librerías necesarias (*invoke*, *pytest* y *assertpy*) para la ejecución de los tests sin necesidad de instalar nada, simplemente se obtiene el contenedor y se ejecutan los tests.

Con el step ```checkout``` se comprueba y copia el directorio de *git*, a continuación se ejecutan los tests con la orden ```run: invoke test```.

```yaml
steps:
            - checkout
            # Launch tests using the task manager
            - run: invoke test
```

### GitHub Action

Al tratarse de una automatización de tareas, una *GitHub Action* por propia definición permite realizar la ejecución de una tarea de forma automatizada, por lo que la automatización de la comprobación de un contenedor *Docker* es una tarea sencilla y programable. Para ello se construirá el contenedor del proyecto, el cual lleva implícito en la construcción la instalación de dependencias y ejecución de los tests.

Esto se puede ver en el fichero de definición de la *GitHub Action* [GitHub Actions CI](https://github.com/Carlosma7/MedAuth/blob/main/.github/workflows/github_actions_CI.yml).

```yaml
# Steps of the job
    steps:
      # Checks-out repository under $GITHUB_WORKSPACE, so workflow can access it
      - uses: actions/checkout@v2

      # Build the image in local space
      - name: Build image
        run: docker build -t medauth .
```
