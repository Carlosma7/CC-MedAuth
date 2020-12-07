## Justificación uso gestor de tareas en Integración Continua

Una de las mejoras que se obtienen al emplear un gestor de tareas, es el aprovechamiento de las tareas diseñadas y simplificación que se produce en la realización de estas tareas, mediante el uso del gestor en el ámbito que corresponda, por lo que su empleao en un entorno de *CI* es más que evidente. El objetivo en este caso es el de realizar la comprobación de los tests desde los sistemas de integración continua, sin tener la necesidad de especificar los tests en cada *CI* que se configure, ya que sería una tarea poco limpia, ineficiente y más costosa.

Por ello se pide la correcta utilización del gestor de tareas en las distintas herramientas de *CI* que se han propuesto, por lo que se procede a ver como este ha sido utilizado en cada una de ellas.

Para poder utilizar en cualquier *CI* propuesto correctamente el gestor de tareas, este deberá instalarse en el entorno del *CI*, para ello se utilizará el fichero de requisitos ```requirements.txt```, el cual se puede observar [aquí](https://github.com/Carlosma7/MedAuth/blob/main/requirements.txt), y que realiza la instalación de las librerías necesarias para el proyecto, entre ellas **invoke**, el cual es el gestor de tareas del proyecto.

### Invoke con Travis

Para utilizar *invoke* con [Travis](https://github.com/Carlosma7/MedAuth/blob/main/.travis.yml), son necesarios dos requisitos:

* Instalar *invoke*, para el cual se utiliza el fichero *requirements.txt* y se instala mediante *pip3*.

```yaml
# Install dependencies (Invoke, Pytest and Assertpy)
install:
  - pip3 install -r requirements.txt
```

* Utilizar la opción ```tests``` de *invoke* para lanzar los tests.

```yaml
# Launch tests using the task manager
script:
  - invoke tests
```

### Invoke con CircleCI

Para utilizar *invoke* con [CircleCI](https://github.com/Carlosma7/MedAuth/blob/main/.circleci/config.yml), son necesarios los requisitos previos:

* Instalar *invoke*, para el cual se utiliza el fichero *requirements.txt* y se instala mediante *pip3*.

```yaml
docker:
            # Project's Docker image in Docker Hub
            - image: carlosma7/medauth:latest
```

Al hacer uso del contenedor del proyecto, utiliza un entorno ya preparado con las herramientas necesarias para realizar los tests, por lo que no es necesario instalar nada, ya posee dichas herramientas.

* Utilizar la opción ```tests``` de *invoke* para lanzar los tests.

```yaml
steps:
            - checkout
            # Launch tests using the task manager
            - run: invoke tests
```

### Invoke con Shippable

Para utilizar *invoke* con [Shippable](https://github.com/Carlosma7/MedAuth/blob/main/shippable.yml), son necesarios nuevamente los mismos requisitos:

* Instalar *invoke*, para el cual se utiliza el fichero *requirements.txt* y se instala mediante *pip3*.

```yaml
build:
  ci:
    # Install dependencies (Invoke, Pytest and Assertpy)
    - pip3 install -r requirements.txt
```

* Utilizar la opción ```tests``` de *invoke* para lanzar los tests.

```yaml
	# Launch tests using the task manager
    - invoke tests
```

### Invoke con GitHub Actions

Para utilizar *invoke* con una [GitHub Action](https://github.com/Carlosma7/MedAuth/blob/main/.github/workflows/github_actions_CI.yml), son necesarios nuevamente los mismos requisitos:

* Instalar *invoke*, para el cual se utiliza el fichero *requirements.txt* y se instala mediante *pip3*.
* Utilizar la opción ```tests``` de *invoke* para lanzar los tests.

```yaml
# Checks-out repository under $GITHUB_WORKSPACE, so workflow can access it
      - uses: actions/checkout@v2

      # Build the image in local space
      - name: Build image
        run: docker build -t medauth .
```

La *GitHub Action* diseñada, utiliza el contenedor propio del proyecto, el cual se actualiza cada vez que se incluyen nuevos tests, se modifica el propio contenedor o alguna configuración específica, por lo que los tests siempre se mantienen actualizados. Si se observa el [Dockerfile](https://github.com/Carlosma7/MedAuth/blob/main/Dockerfile) del proyecto, se puede observar que se realiza la instalación de las dependencias y se lanzan los tests, por lo que se utiliza de forma interna y correcta *invoke*.
