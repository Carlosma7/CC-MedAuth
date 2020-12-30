### API

Para el diseño de la API se han considerado las indicaciones sobre sistemas *REST* y códigos de estado indicadas en el [tema asociado](http://jj.github.io/CC/documentos/temas/REST.html).

Una de las buenas prácticas indicadas es el de separar las rutas definidas de la aplicación, esto se ha podido conseguir utilizando [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/), y asignando el *blueprint* definido posteriormente a la aplicación de *Quart*.

Definición de la aplicación y asignación del *blueprint* en [main.py](https://github.com/Carlosma7/MedAuth/blob/main/src/core/api.py):

```python
# Definición servidor Quart
app = Quart(__name__)
# Registar el blueprint de las rutas
app.register_blueprint(rutas_medauth)
```

Definición del *blueprint* y las rutas en [api.py](https://github.com/Carlosma7/MedAuth/blob/main/src/core/api.py):

```python
# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)
```

#### Rutas definidas

Para las rutas se han distinguido entre las diferentes entidades que se distinguen en el proyecto:

* Usuarios
* Pólizas
* Prescripciones
* Autorizaciones
* Citas

Teniendo en cuenta estas entidades, y las diferentes historias de usuario se han definido las siguientes rutas en el fichero [api.py](https://github.com/Carlosma7/MedAuth/blob/main/src/core/api.py):

* Usuarios:
    *  ```/usuario``` con método **POST** y con código de estado **201**. Se corresponde con el método ```crear_usuario``` y las *HUs* [Como usuario anónimo quiero crear un usuario administrativo en el sistema para gestionar el sistema](https://github.com/Carlosma7/MedAuth/issues/43) y [Como administrativo quiero crear un usuario para un asegurado en el sistema para usar el sistema](https://github.com/Carlosma7/MedAuth/issues/44).
    * ```/usuario/modificar/<dni>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```modificar_usuario``` y la *HU* [Como administrativo quiero gestionar los usuarios existentes en el sistema para modificar o eliminar usuarios](https://github.com/Carlosma7/MedAuth/issues/55).
    * ```/usuario/<dni>``` con método **DELETE** y con código de estado **200**. Se corresponde con el método ```eliminar_usuario``` y la *HU* [Como administrativo quiero gestionar los usuarios existentes en el sistema para modificar o eliminar usuarios](https://github.com/Carlosma7/MedAuth/issues/55).
    * ```/usuario/<dni>``` con método **GET** y con código de estado **200**. Se corresponde con el método ```consultar_usuario``` y la *HU* [Como administrativo quiero consultar un usuario para poder ver la información asociada](https://github.com/Carlosma7/MedAuth/issues/96).

* Pólizas:
    * ```/poliza``` con método **POST** y con código de estado **201**. Se corresponde con el método ```crear_poliza``` y la *HU* [Como administrativo quiero administrar la póliza de un asegurado para crear, modificar o dar de baja una póliza](https://github.com/Carlosma7/MedAuth/issues/35).
    * ```/poliza/modificar/<id_poliza>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```modificar_poliza``` y la *HU* [Como administrativo quiero administrar la póliza de un asegurado para crear, modificar o dar de baja una póliza](https://github.com/Carlosma7/MedAuth/issues/35).
    * ```/poliza/desactivar/<dni>```con método **PUT** y con código de estado **201**. Se corresponde con el método ```desactivar_poliza``` y la *HU* [Como administrativo quiero administrar la póliza de un asegurado para crear, modificar o dar de baja una póliza](https://github.com/Carlosma7/MedAuth/issues/35).
    * ```/poliza/<dni>``` con método **GET** y con código de estado **200**. Se corresponde con el método ```consultar_poliza``` y la *HU* [Como administrativo quiero consultar la póliza de un asegurado para poder ver el tipo de póliza y la información asociada](https://github.com/Carlosma7/MedAuth/issues/34).

* Prescripciones:
    * ```/prescripcion``` con método **POST** y con código de estado **201**. Se corresponde con el método ```subir_prescripcion``` y la *HU* [Como asegurado quiero añadir una prescripción médica para poder solicitar una autorización de una prueba médica](https://github.com/Carlosma7/MedAuth/issues/36).

* Autorizaciones:
    * ```/autorizacion``` con método **POST** y con código de estado **201**. Se corresponde con el método ```crear_autorizacion``` y la *HU* [Como administrativo quiero administrar una autorización médica de un asegurado para crear o modificar una autorización](https://github.com/Carlosma7/MedAuth/issues/39).
    * ```/autorizacion/solicitar/<id_prescripcion>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```solicitar_autorizacion``` y la *HU* [Como asegurado quiero solicitar una autorización médica para poder obtener un servicio médico](https://github.com/Carlosma7/MedAuth/issues/37).
    * ```/autorizacion/modificar/<id_autorizacion>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```modificar_autorizacion``` y la *HU* [Como administrativo quiero administrar una autorización médica de un asegurado para crear o modificar una autorización](https://github.com/Carlosma7/MedAuth/issues/39).
    * ```/autorizacion/aprobar-denegar/<id_autorizacion>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```aprobar_denegar_autorizacion``` y la *HU* [Como administrativo quiero cambiar la aprobación o denegación de una autorización para tratar un caso excepcional](https://github.com/Carlosma7/MedAuth/issues/40).
    * ```/autorizacion/<id_autorizacion>``` con método **GET** y con código de estado **200**. Se corresponde con el método ```consultar_autorizacion``` y la *HU* [Como asegurado quiero consultar una autorización médica para ver el estado de la autorización](https://github.com/Carlosma7/MedAuth/issues/38).
* Citas:
    * ```/cita``` con método **POST** y con código de estado **201**. Se corresponde con el método ```crear_cita``` y la *HU* [Como administrativo quiero administrar una cita médica para crear una cita o modificar información asociada a una cita existente](https://github.com/Carlosma7/MedAuth/issues/49).
    * ```/cita/modificar/<id_autorizacion>``` con método **PUT** y con código de estado **201**. Se corresponde con el método ```modificar_cita``` y la *HU* [Como administrativo quiero administrar una cita médica para crear una cita o modificar información asociada a una cita existente](https://github.com/Carlosma7/MedAuth/issues/49).
    * ```cita/<id_autorizacion>``` con método **GET** y con código de estado **200**. Se corresponde con el método ```consultar_cita``` y la *HU* [Como asegurado quiero consultar una cita médica fijada para ver la información asociada](https://github.com/Carlosma7/MedAuth/issues/41).

A continuación se muestra un ejemplo de cada uno de los métodos *HTTP* utilizados:

* ```/usuario``` con método **POST**:

```python
# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuario', methods=['POST'])
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
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario creado con éxito')
	# Estado de éxito
	return 'Usuario creado con éxito.', 201
```

* ```/usuario/modificar/<dni>``` con método **PUT**:

```python
# [HU3] Administrar usuario: Modificar usuario
@rutas_medauth.route('/usuario/modificar/<dni>', methods=['PUT'])
async def modificar_usuario(dni):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener nombre 
	nombre = data.get('nombre')
	# Obtener email
	email = data.get('email')
	# Obtener cuenta bancaria
	cuenta_bancaria = data.get('cuenta_bancaria')
	# Obtener tipo
	tipo = data.get('tipo')
	
	try:
		# Modificación usuario
		controlador.modificar_usuario(dni, nombre, email, cuenta_bancaria)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario modificado con éxito')
	# Estado de éxito
	return 'Usuario modificado con éxito.', 201
```

* ```/usuario/<dni>``` con método **DELETE**:

```python
# [HU3] Administrar usuario: Eliminar usuario
@rutas_medauth.route('/usuario/<dni>', methods=['DELETE'])
async def eliminar_usuario(dni):
	try:
		# Eliminación usuario
		controlador.eliminar_usuario(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario eliminado con éxito')
	# Estado de éxito
	return 'Usuario eliminado con éxito.', 200
```

* ```/usuario/<dni>``` con método **GET**:

```python
# [HU14] Consultar usuario
@rutas_medauth.route('/usuario/<dni>', methods=['GET'])
async def consultar_usuario(dni):
	try:
		# Consultar usuario
		usuario = controlador.consultar_usuario(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario obtenido con éxito')
	# Estado de éxito
	return usuario.to_dict(), 200
```


#### Tests

Se ha definido un test para cada uno de los casos que se contemplaban en los [tests del controlador](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testControlador.py) de la lógica de negocio, los cuales se pude ver en el fichero [testApi.py](https://github.com/Carlosma7/MedAuth/blob/main/src/test/testApi.py).

Una de las principales ventajas de trabajar con **Quart** es que se integra fácilmente con **Pytest**, nuestro marco de pruebas, por lo que únicamente habría que añadir la funcionalidad asíncrona al mismo, lo cual se consigue con la librería [pytest-asyncio](https://pypi.org/project/pytest-asyncio/). A continuación se define la aplicación mediante:

```python
@pytest.fixture(name='test_medauth')
def _test_medauth():
	return app
```

A continuación, para definir un test con la funcionalidad asíncrona, se añade el marcador ```@pytest.mark.asyncio``` y definimos las funciones como métodos ```async```, indicándole la aplicación como argumento. Un ejemplo sería:

```python
# Test creacion usuario administrativo
@pytest.mark.asyncio
async def test_crear_admin_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario'
	
	# Crear usuario administrativo
	usuario = UsuarioAdmin('Alfredo', 'alfredo@gmail.com', '35925767-A', '')
	tipo = 0
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(201)
```

