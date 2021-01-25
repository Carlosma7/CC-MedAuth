


### Estudio inicial

Para poder escoger un framework que se adapte a las necesidades del proyecto, primero hay que comprender el enfoque del mismo. Se parte de la base de que al tratarse de un servicio médico, es relevante la asincronicidad del proyecto, ya que no se pueden realizar peticiones de forma síncronas y con esperas. Por lo tanto, solo se contemplaran frameworks asíncronos, y para realizar una justificación técnica se realizará una implementación sencilla de los mismos:

[Quart](https://gitlab.com/pgjones/quart): Una de las principales ventajas es que posee la API de Flask, cumpliendo además con el estándar ASGI, que ofrece soporte asíncrono. Lo interesante de Quart es que no solo es similar a Flask, sino que en realidad cumple con la API de Flask. Una de las consideraciones más importantes es que al poseer las funciones de Flask, contiene los *Blueprint*, los cuales permiten separar las rutas de la API, lo cual es una buena práctica deseada. Por otro lado, otra de las ventajas principales es que posee una integración natural con *pytest*, el marco de pruebas del proyecto.

```python
from controlador import *

from quart import Quart, Blueprint, jsonify, request
import json

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuarios', methods=['POST'])
async def crear_usuario():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener tipo 
	tipo = data.get('tipo')
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except Exception as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

[Sanic](https://sanicframework.org/): Al estar desarrollado en las versiones más modernas de *Python* posee un enfoque simple y hace uso de la sintaxis *async/await*. Al tratarse de un framework sencillo de implementar es una opción interesante, y que no necesita de demasiada documentación para llevarse a cabo. Su sintaxis de hecho es bastante similar a la de Flask, sin utilizar su misma API, pero utilizando algunos de sus componentes como las *Blueprints*.

```python
from controlador import *

from sanic import Sanic, Blueprint
from sanic.response import json

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuarios', methods=['POST'])
async def crear_usuario():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener tipo 
	tipo = data.get('tipo')
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except Exception as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

[Tornado](https://www.tornadoweb.org/en/stable/): Más que un framework web, se trata de una seria de utilidades y funciones asíncronas desarrolladas en *Python* con el objetivo de comportarse igual que un framework web. Al usar E/S de red sin bloqueo, *Tornado* puede escalar a miles de conexiones abiertas. Una de las principales desventajas es que no soporta el estándar ASGI.

No se ha realizado una implementación ya que no se considera una opción considerable de cara a la realización de la API, ya que interesa más un framework completo que una serie de utilidades.

[FastAPI](https://fastapi.tiangolo.com/): Es un framework rápido, con poco tiempo ya que se originó en 2019. Permite crear APIs con *Python* 3.6+ basado en sugerencias de tipado *Python* estándar. Uno de sus puntos fuertes es que se percibe un claro estudio por parte del autor sobre otros competidores, tratando de mejorar los puntos débiles de estos.

```python
from controlador import *

from fastapi import FastAPI
from pydantic import BaseModel

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de la aplicación
medauth_app = FastAPI()

class Item(BaseModel):
    usuario: Usuario
    tipo: int

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@medauth_app.post('/usuarios')
async def crear_usuario(item: Item):	
	# Obtener usuario
	usuario = item.usuario
	# Obtener tipo 
	tipo = item.tipo
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except Exception as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

[Starlette](https://www.starlette.io/): Se trata de un framework y serie de utilidades que utilizan el estándar ASGI, para construir servicios haciendo uso de funciones asíncronas. Al igual que las demás opciones mencionadas, contiene las principales herramientas de cara a diseñar una API con funciones asíncronas, por lo que no presenta en un principio ninguna ventaja respecto a las alternativas.

```python
from controlador import *

from starlette.applications import Starlette

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de la aplicación
medauth_app = Starlette()

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@medauth_app.route('/usuarios', methods=['POST'])
async def crear_usuario(request):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener tipo 
	tipo = data.get('tipo')
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except Exception as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

[Vibora](https://vibora.io/): Otro de los microframeworks que se basan en su similitud con Flask, se considera a sí mismo como uno de los frameworks más veloces y con mejor rendimiento, incluso duplicando la velocidad de *Sanic* con quien guarda una gran similitud. Además de la diferencia de la velocidad no aporta nada nuevo respecto al resto de sus competidores.

```python
from controlador import *

from vibora import Vibora, JsonResponse, Blueprint

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuarios', methods=['POST'])
async def crear_usuario():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener tipo 
	tipo = data.get('tipo')
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except Exception as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

### Análisis opciones

Tras examinar las diferentes alternativas y realizar la implementación de uno de los métodos del proyecto como es la creación de usuarios, se puede comprobar que entre las opciones que se consideran realmente hay pocas diferencias como para determinar la elección más correcta para el proyecto. Con el fin de decidir una opción correcta, se han tenido en cuenta las siguientes consideraciones:

* Es deseable utilizar un framework que permita la definición y diseño de la API completa, por lo que utilizar un conjunto de utilidades como *Tornado* no es una opción deseada.
* No existe gran diferencia entre utilizar *Sanic*, *Vibora* o *Quart* a nivel de implementación para el proyecto actual, por lo que el framework deseado a nivel de velocidad sería *Vibora*, a nivel de contenidos, soporte y comunidad sería *Sanic*, y a nivel de similitud con *Flask* sería *Quart*, sin dejar de lado *Starlette*, pero tampoco aporta nada nuevo respecto a los otros frameworks.
* Sin embargo, existe un factor determinante en esta comparativa que es la integración con *Pytest*, si bien todos los frameworks pueden trabajar con dicho marco de pruebas, *Quart* se encuentra directamente integrado con el mismo, por lo que es una opción más que deseable en este proyecto.
* *FastAPI* considera las debilidades de sus competidores y trata de enmendarlas, por lo que es una opción más que deseable, sin embargo, no posee la integración de *Blueprints*, lo cual nos permite separar las rutas de la aplicación y es una buena práctica deseada.

Como se ha comentado previamente, a nivel técnico de cara a este proyecto cualquiera de las opciones sería válida excepto *Tornado*, que presenta una serie de claras desventajas. Sin embargo, la integración con *Blueprints* para separar las rutas de la aplicación, y la integración con *Pytest* son los dos factores a nivel técnico que declinan la balanza para la decisión de un framework en este proyecto.

Finalmente el microframework sobre el que se va a desarrollar la API del proyecto es **Quart**.

