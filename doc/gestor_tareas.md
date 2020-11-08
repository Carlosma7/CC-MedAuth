## Gestor de tareas

---

El gestor de tareas escogido para el proyecto será [Invoke](http://www.pyinvoke.org/).

Tras realizar un análisis de las distintas herramientas posibles, finalmente se valoraron **Invoke** y **Makefile**. Pese a ser dos herramientas completamente válidas para el proyecto, porque permiten la automatización de tareas de una forma sencilla, y ambas aportan las herramientas necesarias para ello. Además, ambos permiten la ejecución de varias tareas en una misma llamada.

Se ha escogido *Invoke* frente a *Makefile* por las siguientes razones:

* Invoke es dirigido por código, frente a Makefile, que es dirigido por objetivos.
* Invoke sigue la sintaxis de Python, frente a Makefile que posee su propia sintaxis. Invoke favorece la homogeneidad de sintaxis en el desarrollo de nuestro proyecto.
* Invoke es independiente de la plataforma en la que se ejecute, ya que está basado en Python3. Makefile, por ejemplo, necesita un fichero *.bat* para su ejecución en Windows. La portabilidad de Invoke permite que se despliegue el proyecto con mayor comodidad en cualquier sistema.
* Al estar codificado en Python3, los errores de Invoke se observan como errores de programación de Python que indican donde está exactamente el error. Los errores de Makefile pueden resultar más complicados de detectar a simple vista.
* Invoke posee un enfoque heredado de GNU Make, y añade sus funcionalidades propias.

Un ejemplo de una tarea en Invoke sería la siguiente:

```Python
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
