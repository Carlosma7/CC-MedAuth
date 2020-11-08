## Biblioteca de aserciones

---

Las bibliotecas de aserciones escogidas son:

* [Assert Statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) nativo de Python.
* [pytest](https://docs.pytest.org/en/stable/).

Inicialmente se valoraron distintas bibliotecas de aserciones dedicadas como [assertpy](https://github.com/ActivisionGameScience/assertpy), [grappa](https://github.com/grappa-py/grappa) o [verify](https://github.com/dgilland/verify), pero como se va a utilizar como framework de pruebas [pytest](https://docs.pytest.org/en/stable/) que aporta funciones de aserciones muy cercanas al lenguaje natural, permite desarrollar una batería de pruebas ágilmente.

Además, se integrará la utilización de **pytest** con la sentencia **assert** nativa del lenguaje, permitiendo por ejemplo la comparación de objetos simplemente sobreescribiendo o implementando el método "\_\_eq\_\_".

Se ha optado por esta opción ya que el uso de instrucciones nativas junto a una biblioteca de test avanzada como *pytest* ofrece las siguientes ventajas frente la importación de una biblioteca específica de aserciones:

* Uso fácil e intuitivo.
* Posee herramientas nativas que se combinan de forma natural con herramientas avanzadas de *pytest*.
* Comparación sencilla de objetos compuestos.
* La sintaxis combinada de ambas herramientas combina lenguaje de Python con lenguaje aproximado al natural, a diferencia de bibliotecas como *grappa* cuyo lenguaje natural puede llegar a ser confuso.
* Los resultados de los tests son fácilmente interpretables y carecen de excesiva verborrea.

Un ejemplo de combinación entre *pytest* y la sentencia *assert* es:

```python
# Método equal
def __eq__(self, otra):
	assert self.__titular == otra.get_titular()
	assert self.__id_poliza == otra.get_id_poliza()
	assert self.__periodo_carencia == otra.get_periodo_carencia()
	assert self.__tipo == otra.get_tipo()
	assert self.__copagos == otra.get_copagos()
	assert self.__mensualidad == otra.get_mensualidad()
	assert self.__servicios_excluidos == otra.get_servicios_excluidos()
	assert self.__modulos_extra == otra.get_modulos_extra()
	assert self.__activa == otra.get_activa()
    	
	return (self.__titular == otra.get_titular()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__periodo_carencia == otra.get_periodo_carencia()) and (self.__tipo == otra.get_tipo()) and (self.__copagos == otra.get_copagos()) and (self.__mensualidad == otra.get_mensualidad()) and (self.__servicios_excluidos == otra.get_servicios_excluidos() and (self.__modulos_extra == otra.get_modulos_extra()) and (self.__activa == otra.get_activa()))

# Test comparación pólizas
def test_compare_poliza():
	u = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	u2 = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	fecha2 = datetime.datetime(2020, 5, 18)
	
	t1 = TestPoliza(u, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	t2 = TestPoliza(u2, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
```
