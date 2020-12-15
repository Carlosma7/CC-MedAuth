## Gestor de tareas

---

##### Justificación elección

El gestor de tareas escogido para el proyecto será [Invoke](http://www.pyinvoke.org/).

Inicialmente, se ha realizado un estudio sobre distintos gestores de tareas que se podían emplear para el proyecto, y que por lo tanto fueran compatibles con Python. Las principales opciones que se han considerado han sido [Invoke](http://www.pyinvoke.org/), [Makefile](https://es.wikipedia.org/wiki/Make), [Poetry](https://python-poetry.org/), [SCons](https://scons.org/) y [Luigi](https://github.com/spotify/luigi). Tras un pequeño estudio de características, se han descartado estas dos últimas, ya que su integración en el proyecto resultaría un proceso complejo y tras observarse la documentación no queda claro que mejoren otra opción más conocida como *Make*.

Tras realizar un análisis de las distintas herramientas posibles, finalmente se valoraron **Invoke**, **Makefile** y **Poetry**. Para poder realizar una elección adecuada del gestor de tareas, he decidido probar las distintas herramientas con el proyecto diseñado. Para la realización, he podido observar que *Invoke* y *Make* se integran de una forma muy sencilla, mientras que *Poetry* ha resultado más complicado de diseñar, por lo que inicialmente se ha creado un ejemplo en una máquina virtual (se puede observar [aquí](https://github.com/Carlosma7/MedAuth/blob/main/doc/img/poetry.jpg) la ejecución de Poetry) para finalmente probar y adaptarlo al proyecto.

A continuación se adjuntan los distintos ficheros de configuración utilizados: [Invoke](https://github.com/Carlosma7/MedAuth/blob/main/tasks.py), [Makefile](https://github.com/Carlosma7/MedAuth/blob/main/doc/Makefile) y [Poetry](https://github.com/Carlosma7/MedAuth/blob/main/doc/pyproject.toml).

Finalmente, se ha escogido *Invoke* frente a *Makefile* y *Poetry* por las siguientes razones:

* **Invoke es dirigido por código**, frente a Makefile e Poetry, que son dirigidos por objetivos.
* **Invoke sigue la sintaxis de Python**, frente a Makefile que posee su propia sintaxis, o Poetry, que sigue una sintaxis *TOML*. Invoke favorece la homogeneidad de sintaxis en el desarrollo de nuestro proyecto.
* **Invoke es independiente de la plataforma en la que se ejecute**, ya que está basado en Python3. Makefile, por ejemplo, necesita un fichero *.bat* para su ejecución en Windows. La portabilidad de Invoke permite que se despliegue el proyecto con mayor comodidad en cualquier sistema.
* Al estar codificado en Python3, **los errores de Invoke se observan como errores de programación de Python que indican donde está exactamente el error**, aunque Poetry en este sentido no se queda atrás, ya que es una herramienta intuitiva en cuanto a errores. Los errores de Makefile pueden resultar más complicados de detectar a simple vista.
* **Invoke posee un enfoque heredado de GNU Make**, y añade sus funcionalidades propias.
* Si bien *Poetry* es a día de hoy la herramienta puntera en este ámbito (en cuanto a Python se refiere), es una herramienta compleja de configurar y posee una gran cantidad de dependencias, por lo que, aunque resulta interesante y probablemente sea la mejor herramienta para un gran proyecto, en nuestro caso con una herramienta más sencilla como *Invoke* es más que suficiente, y no es necesaria toda la potencia y funcionalidad que aporta *Poetry*, además de la carga que supone para el futuro contenedor a utilizar.

Un ejemplo de una tarea en Invoke sería la siguiente:

```python
# Tarea de ejecución de tests
@task
def test(c):
	print("Ejecución de test.\n")
	print("Test Clase UsuarioAdmin:")
	run("pytest -v --disable-pytest-warnings ./src/test/modelos/testUsuarioAdmin.py")
```

Para el uso de Invoke, se requieren los módulos **task** y **run**.

* **task**: Representa cada tarea y hace que se interpreten como una llamada/ejecución de una tarea con argumentos. Posee además sus propios argumentos que definen su comportamiento.

* **run**: Sirve para poder ejecutar comandos de shell, igual que realizaría Make o Rake. Al igual que task, posee argumentos que especifican el comportamiento de la ejecución.

##### Configuración Invoke

Para poder utilizar *Invoke* primero se ha instalado con `pip3 install invoke`, y a continuación se ha creado el fichero de gestión de tareas, que en *Invoke* recibe el nombre [tasks.py](https://github.com/Carlosma7/MedAuth/blob/main/tasks.py), ya que está construido con el propio Python.

Una vez creado el fichero *tasks.py*, procedemos a definir las tareas necesarias en la fase actual del proyecto:

* clean: Limpieza de ficheros.
* execute: Ejecución del *main* del proyecto.
* test: Ejecución de los test unitarios. (Cabe destacar que el núcleo de *Invoke* posee una tarea predefinida que trabaja con *pytest* llamada [test](https://github.com/pyinvoke/invoke/blob/master/tasks.py#L13), la cual podría ser modificada, pero para el fin deseado se creará una nueva).

Una vez definidas las tareas, se configuran en *Invoke* de la siguiente manera:

* clean: Se borran las carpetas de caché creadas por python3 y por pytest en cualquier directorio o subdirectorio del proyecto. Esto es útil si se realizara cualquier ejecución o test de modo local en lugar de simplemente ejecutar la tarea.

```python
# Tarea de limpieza de ficheros
@task 
def clean(c):
	print("Borrando caché de python.")
	run("find . -maxdepth 5 -type d -name __pycache__ -exec rm -r {} +")
	print("Borrando caché de pytest.")
	run("find . -maxdepth 5 -type d -name .pytest_cache -exec rm -r {} +")
```

* execute: Se ejecuta el programa *main* el cual ejecuta toda la funcionalidad del proyecto. También se muestra por pantalla actualmente un mensaje de inicio y finalización, ya que no se observan resultados por pantalla.

```python
# Tarea de ejecución del modelo
@task
def execute(c):
	print("Ejecución del modelo\n")
	run("python3 ./src/main.py")
	print("Fin de la ejecución.")
```

* test: Se ejecutan todos los tests del proyecto, demostrando que funciona correctamente cada una de las entidades del mismo. Para ello ejecutamos *pytest* con la entidad que queremos comprobar.

```python
# Tarea de ejecución de tests
@task
def test(c):
	print("Ejecución de test.\n")
	print("Test Clase UsuarioAdmin:")
	run("pytest -v --disable-pytest-warnings ./src/test/testUsuarioAdmin.py")
	
	print("\nTest Clase UsuarioCliente:")
	run("pytest -v --disable-pytest-warnings ./src/test/testUsuarioCliente.py")
	
	print("\nTest Clase Poliza:")
	run("pytest -v --disable-pytest-warnings ./src/test/testPoliza.py")
	
	print("\nTest Clase Prescripcion:")
	run("pytest -v --disable-pytest-warnings ./src/test/testPrescripcion.py")
	
	print("\nTest Clase Autorizacion:")
	run("pytest -v --disable-pytest-warnings ./src/test/testAutorizacion.py")
	
	print("\nTest Clase Cita:")
	run("pytest -v --disable-pytest-warnings ./src/test/testCita.py")
	
	print("\nTest Clase Controlador:")
	run("pytest -v --disable-pytest-warnings ./src/test/testControlador.py")
```


##### Build & Run

Para ejecutar el gestor de tareas se ha de ejecutar:

`invoke <tarea>`

Un ejemplo sería:

`invoke clean`
