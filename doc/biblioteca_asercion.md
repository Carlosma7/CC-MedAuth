## Biblioteca de aserciones

---

Las bibliotecas de aserciones escogidas son:

* [Assertpy](https://github.com/assertpy/assertpy)

Las herramientas proporcionadas por dicha herramienta se integrarán además con el [marco de pruebas](https://carlosma7.github.io/MedAuth/doc/marco_pruebas) escogido, pero eso se mencionará en este apartado.

Inicialmente se valoraron distintas bibliotecas de aserciones dedicadas como [Unittest](https://docs.python.org/3/library/unittest.html), [Grappa](https://github.com/grappa-py/grappa), [Verify](https://github.com/dgilland/verify) o [hypothesis](https://hypothesis.readthedocs.io/en/latest/). Cabe destacar que Python posee una infinidad de bibliotecas destinadas a este fin, por ese motivo, vamos a buscar una biblioteca que nos permita realizar los tests de una forma limpia, sencilla, legible y que se integre con el marco de pruebas sin problema alguno.

Python incluye aserciones por omisión, y además incluye biblioteca como *Unittest* o *Doctest* de forma integrada, por lo que el uso de estas bibliotecas sería una buena aproximación inicial, pero finalmente, tras una primera fase en las que se utilizó la sentencia **assert** nativa del lenguaje, y tras estudiar nuevas herramientas, se ha decidido finalmente utilizar *Assertpy* por los siguientes motivos:

* A diferencia de bibliotecas como *Grappa* o *Verify* únicamente importa una función **assert_that**, la cual incluye otras funciones que especifican la comprobación, todo esto desde un lenguaje Python fácilmente interpretable con lenguaje natural. *Grappa* o *Verify* por ejemplo poseen un lenguaje más cercano al natural, pero con excesiva verborrea que dificulta su utilización desde un enfoque de programación.
* *Assertpy* permite realizar comprobaciones de forma sencilla sobre objetos más complejos como *datetime*, ficheros u objetos compuestos, todo esto sin una codificación excesiva.
* **Las llamadas son funciones de tipo Python**, lo cual facilita su uso, y no obliga a realizar sentencias complejas de interpretar.
* Es **compatible** con los principales frameworks de test como *Pytest* o *Nose*, entre otros.
* Las **aserciones se realizan mediante funciones**, lo cual es una ventaja frente a *Unittest*, que pese a que se encuentra integrada en Python, necesita realizar definición de clases con herencia y métodos para realizar los tests.
* Frente a utilizar únicamente la aserción nativa de Python, *Assertpy* proporciona una forma más sencilla y legible de realizar comprobaciones más complejas, consistentes en varias operaciones utilizando únicamente la sentencia *assert*.



Un ejemplo de un test diseñado para el proyecto sería:

```python
# Test de creación de usuario administrativo
def test_crear_admin():
	controlador = Controller()
	admin = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	adminOtro = UsuarioAdmin("Fernando", "fer@gmail.com", "12925767-F", "")
	
	controlador.crear_admin(admin)
	assert_that(controlador.usuariosAdmins).contains(admin).does_not_contain(adminOtro)
```
