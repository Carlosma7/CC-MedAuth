from controlador import *
from controlador import Controller as usuario_servicios
from api import rutas_medauth
import json

from quart import Quart, Blueprint, jsonify, request, current_app

# Quart server definition
app = Quart(__name__)
# Register blueprint for routes
app.register_blueprint(rutas_medauth)

if __name__ == '__main__':
	app.run(port=2020, host='0.0.0.0')
