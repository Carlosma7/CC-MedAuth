from controlador import *
from controlador import Controller as usuario_servicios
from api import *
import json
import etcd3
from dotenv import load_dotenv
import os
from server import *

# Registar el blueprint de las rutas
app.register_blueprint(rutas_medauth)
# Se activa el middleware
app = LogMiddleware(app)

if __name__ == '__main__':
	try:
		# Obtener cliente etcd
		etcd = etcd3.client()
		# Obtener host y puerto
		server_port = etcd.get('port')[0]
		server_host = etcd.get('host')[0]
		# Comprobar que existen ambas claves
		if server_host and server_port:
			server_host = server_host.decode('utf-8')
			server_port = server_port.decode('utf-8')
		else:
			raise ValueError('No existen los valores "port" y "host"')
	# Si etcd no funciona
	except:
		# Obtener información de .env
		load_dotenv(dotenv_path = '.env')
		# Obtener host y puerto
		server_port = os.getenv('PORT')
		server_host = os.getenv('HOST')
		
	
	# Se activa el middleware
	app = LogMiddleware(app)
	# Se lanza la aplicación
	app.run(port=server_port, host=server_host)
