## Marco de pruebas

---

El marco de pruebas escogido es [pytest](https://docs.pytest.org/en/stable/).

Tras un primer análisis, se ha procedido a instalar tres frameworks distintos de [pytest](https://docs.pytest.org/en/stable/), el cual fue elegido inicialmente. Para ello se han estudiado distintos frameworks, para tras un primer estudio, proceder a probar [Nose](https://nose.readthedocs.io/en/latest/), [Nose2](https://docs.nose2.io/en/latest/) y [Testify](https://github.com/Yelp/Testify).

Tras realizar un primer análisis de uso, se pueden sacar las siguientes conclusiones:

* **Nose**.
	* Posee como base la biblioteca *unittest* para la realización de aserciones.
	* Posee una gran cantidad de plugins para la realización de tareas relacionadas a testing.
	* Uno de nuestros objetivos es usar un framework lo más actualizado posible, por lo que plantearse su uso realmente carece de sentido existiendo *Nose2*.

* **Nose2**.
	* Es el sucesor de *Nose*.
	* No posee todas las funcionalidades de *Nose*, en su lugar la sustituye por otras nuevas o similares.
	* Requiere un gran conocimiento sobre testing en *Python*. Como detalle destacaría que en la misma página oficial sugieren que en caso de no conocer bien la materia se debería usar *pytest*.
	* Dependencia quizás excesiva de plugins.
	* La complejidad de la configuración crece exponencialmente en cuanto crece la complejidad del proyecto.

* **Testify**.
	* Al igual que *Nose* y *Nose2*, su base está desarrollada con *unittest*.
	* Utiliza una convención más parecida a la propia del lenguaje.
	* Similar a *pytest*.
	* Posee plugins que extienden su funcionalidad.
	
Otra opción que se podría haber considerado sería [Robot Framework](https://robotframework.org/), que sería una opción interesante y a tener en cuenta si el desarrollo de nuestro proyecto se realizara con distintos lenguajes, pero se ha descartado ya que está más orientado a tests de aceptación que tests unitarios.

Se ha optado finalmente por utilizar *pytest* frente a estas opciones por lo siguientes motivos:

* Puede ejecutar test de *unittest*, aunque actualmente no se consideren en el proyecto, podrían plantearse sin problemas en un futuro o incluso realizar el cambio sin ningún tipo de problema. Realmente con este punto podríamos considerar que ninguno de los frameworks estudiados posee dicha ventaja frente al resto.
* **Visualización óptima de errores**, no se limita a mostrar la línea del error como cualquiera de las versiones de *Nose* sino que *pytest* además indica el error, los valores y remarca con colores.
* Utiliza la sentencia **assert** estándar en Python. Además, es compatible con la [biblioteca de aserciones](https://carlosma7.github.io/MedAuth/doc/biblioteca_asercion) que se ha escogido. La integración con *Testify* por ejemplo podría realizarse, pero de forma más compleja.
* Permite un setup de test con enfoques o *fixtures* de módulo, sesión o función.
* La ejecución de tests permite selección de tests por nombre al marcar correctamente su *fixture*.
* En *pytest* los **tests se definen como funciones**, a diferencia de los frameworks basados en *unittest*, que requiere de una clase con herencia, y cuyos métodos representan los tests.
* Al no pertenecer a la librería estándar de Python, **no depende de las releases** del mismo.

Por último, cabría destacar que tras analizar dichas diferencias, y contemplar como opciones finales *Pytest* y *Testify*, se ha escogido *Pytest*, además de por los motivos anteriormente explicados, porque *Pytest* posee una mayor documentación y su instalación se puede realizar de un modo más sencillo.

Tras explicar la elección, se procede a mostrar un ejemplo de ejecución de *pytest* el cual se encuentra en [test de controlador](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py):

![Pytest](./img/pytest.png "Pytest")
