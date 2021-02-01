from quart import Quart, Blueprint, jsonify, request, current_app
import os
from loguru import logger

class LogMiddleware:
	def __init__(self, app):
		self.app = app
	
	async def __call__(self, scope, receive, send):
		# Puedo ver lo que recibo con:
		# logger.info(receive)

		# Imprimo el ambito en el que se ejecuta el middleware
		# Con scope puede ver el cliente, la compresion, el cliente y la ruta
		# logger.info(scope)
		try:
			logger.info(scope.get('path') + " " + scope.get('method'))
		except TypeError as error:
			logger.info('Middleware was initiated.')
		return await self.app(scope, receive, send)

# Definición servidor Quart
app = Quart(__name__)
