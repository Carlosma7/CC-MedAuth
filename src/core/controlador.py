from usuario import Usuario
from usuarioAdmin import UsuarioAdmin
from usuarioCliente import UsuarioCliente
from poliza import Poliza
from prescripcion import Prescripcion
from autorizacion import Autorizacion
from cita import Cita
from excepciones import *

from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra
from especialidad import Especialidad
from typing import List
import datetime
import re
import os
from pymongo import MongoClient

try:
	# Try to get the MongoDB URI by environment variables
	mongo_uri = 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':' + os.environ['MONGODB_PORT'] + '/' + os.environ['MONGODB_DATABASE']
except:
	# Default URI
	mongo_uri = 'mongodb://localhost:27017/medauthdb'

try:
	conexion = MongoCliente(mongo_uri)
except:
	conexion = ""

# Clase controladora de lógica de negocio
class Controller:

	mongo = conexion
	# Lista de entidades
	usuarios: List[Usuario] = []
	polizas: List[Poliza] = []
	prescripciones: List[Prescripcion] = []
	autorizaciones: List[Autorizacion] = []
	citas: List[Cita] = []
	
	# [HU1] Creación usuario administrativo
	# [HU2] Creación usuario asegurado
	def crear_usuario(self, usuario: Usuario, tipo_usuario: int):
		try:
			usr = self.mongo.db.usuarios.find({'dni':usuario.get_dni()})
			no_encontrado = (usr.count() == 0)
		except:
			usr = [u for u in self.usuarios if u.get_dni() == usuario.get_dni()]
			no_encontrado = (len(usr) == 0)
		
		# Comprobar si el DNI existe en los usuarios existentes
		if no_encontrado:
			# Comropobar DNI
			if bool(re.match("[0-9]{8}-[A-Z]", usuario.get_dni())):
				# Comprobar correo
				if bool(re.match("([a-zA-Z0-9]+@[a-zA-Z]+\.)(com|es)", usuario.get_email())):
				
					if tipo_usuario == 0: # Admin
						# Patrón correo: email@medauth
						email_empresarial = usuario.get_email().split('@')[0] + '@medauth.com'
						usuario.set_email_empresarial(email_empresarial)
						
						# Se crea el usuario administrativo
						usr_creado = UsuarioAdmin(usuario.get_nombre(), usuario.get_email(), usuario.get_dni(), usuario.get_email_empresarial())
						
					elif tipo_usuario == 1: # Cliente
						if bool(re.match("ES[0-9]{22}", usuario.get_cuenta_bancaria())):
							# Se crea el usuario cliente
							usr_creado = UsuarioCliente(usuario.get_nombre(), usuario.get_email(), usuario.get_dni(), usuario.get_cuenta_bancaria())
						else:
							raise IBANFormatError('IBAN not valid.')
					else:
						raise WrongUserTypeError('Wrong user type.')
						
					# Se almacena
					try:
						self.mongo.db.usuarios.insert_one(usr_creado.to_dict())
					except:
						self.usuarios.append(usr_creado)
					
				
				else:
					raise EmailFormatError('Email not valid.')
			else:
				raise DNIFormatError('DNI not valid.')
			
		else:
			raise ExistingUserError('An user exists with DNI provided.')
			

	# [HU3] Administrar usuario: Modificar usuario
	def modificar_usuario(self, dni: str, nombre: str, email: str, cuenta_bancaria: str):
		# Se obtiene el usuario por su dni
		
		try:
			usr = self.mongo.db.usuarios.find_one({'dni': dni})
			encontrado = (usr != None)
		except:
			usr = [u for u in self.usuarios if u.get_dni() == dni]
			encontrado = (len(usr) > 0)
		
		# Comprobar si el DNI existe en los usuarios existentes
		if encontrado:
			try:
				if usr.get('cuenta_bancaria') == None:
					usr = UsuarioAdmin.from_dict(usr)
				else:
					usr = UsuarioCliente.from_dict(usr)
			except:
				usr = usr[0]
			# Comprobar correo
			if bool(re.match("([a-zA-Z0-9]+@[a-zA-Z]+\.)(com|es)", usr.get_email())):
				# Se modifica la información
				usr.set_nombre(nombre)
				usr.set_email(email)
				
				if usr.get_tipo() == 0: # Admin
					email_empresarial = email.split('@')[0] + '@medauth.com'
					usr.set_email_empresarial(email_empresarial)
				else: # Cliente
					if bool(re.match("ES[0-9]{22}", cuenta_bancaria)):
						usr.set_cuenta_bancaria(cuenta_bancaria)
					else:
						raise IBANFormatError('IBAN not valid.')
						
				# Actualizar en BD
				try:
					self.mongo.db.usuarios.update({'dni': usr.get_dni()}, {'$set': usr.to_dict()})
				except:
					pass
			else:
				raise EmailFormatError('Email not valid.')
		else:
			raise NonExistingUserError('User doesn´t exist.')

	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		try:
			usuario_buscado = self.mongo.db.usuarios.find_one({'dni': dni})
			encontrado = (usuario_buscado != None)
		except:
			usuario_buscado = [u for u in self.usuarios if u.get_dni() == dni]
			encontrado = (len(usuario_buscado) > 0)
			
		if encontrado:
			# Se elimina el usuario
			try:
				self.mongo.db.usuarios.delete_one({'dni': dni})
			except:
				self.usuarios.remove(usuario_buscado[0])
		else:
			raise NonExistingUserError('User doesn´t exist.')

	# [HU4] Administrar póliza: Crear una póliza
	def crear_poliza(self, poliza: Poliza):
		# Se obtiene el usuario cliente/asegurado por su dni
		try:
			cliente = self.mongo.db.usuarios.find_one({'dni': poliza.get_titular().get_dni()})
			encontrado = (cliente != None)
		except:
			cliente = [c for c in self.usuarios if c.get_dni() == poliza.get_titular().get_dni()]
			encontrado = (len(cliente) > 0)
		
		if encontrado:
			try:
				cliente = UsuarioCliente.from_dict(cliente)
			except:
				cliente = cliente[0]
			# Se compone el identificador de la póliza con el formato MA-DNI-ID_ULTIMA_POLIZA+1
			dni = cliente.get_dni()
			id_poliza = "MA-" + dni[:9]
			# Se obtienen las polizas previas
			try:
				polizas_previas = self.mongo.db.polizas.find({'id_poliza': {'$regex': '.*' + id_poliza + '.*'}})
				polizas_previas = list(polizas_previas)
			except:
				polizas_previas = [p for p in self.polizas if p.get_id_poliza()[:12] == id_poliza]
			
			if len(polizas_previas) > 0:
				poliza_previa = polizas_previas[-1]
				try:
					poliza_previa = Poliza.from_dict(poliza_previa)
				except:
					pass
				
				# Si posee polizas previas canceladas, se obtiene el ID de la última que tuvo
				if not poliza_previa.get_activa():
					# Si la última póliza no está activa
					id_poliza = id_poliza + str(int(poliza_previa.get_id_poliza()[-1]) + 1)
				else:
					raise ActivePolicyError('User already has an active policy.')
			else:
				# Si es la primera se crea como tal
				id_poliza = id_poliza + "1"

			poliza.set_id_poliza(id_poliza)

			try:
				self.mongo.db.polizas.insert_one(poliza.to_dict())
			except:
				self.polizas.append(poliza)
			
		else:
			raise NonExistingUserError('User doesn´t exist.')

	# [HU4] Administrar póliza: Modificar una póliza
	def modificar_poliza(self, id_poliza: str, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: float, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		# Se obtiene la póliza asociada al identificador
		try:
			pol = self.mongo.db.polizas.find_one({'id_poliza': id_poliza})
			encontrado = (pol != None)
		except:
			pol = [p for p in self.polizas if p.get_id_poliza() == id_poliza]
			encontrado = (len(pol) > 0)
		

		if encontrado:
			try:
				pol = Poliza.from_dict(pol)
			except:
				pol = pol[0]
			# Modificación de la póliza
			pol.set_periodo_carencia(periodo_carencia)
			pol.set_tipo(tipo)
			pol.set_copagos(copagos)
			pol.set_mensualidad(mensualidad)
			pol.set_servicios_excluidos(servicios_excluidos)
			pol.set_modulos_extra(modulos_extra)
			
			# Actualizar en BD
			try:
				self.mongo.db.polizas.update({'id_poliza': id_poliza}, {'$set': pol.to_dict()})
			except:
				pass
		else:
			raise NonExistingPolicyError('Policy doesn´t exist.')

	# [HU4] Administrar póliza: Desactivar una póliza
	def desactivar_poliza(self, dni: str):
		try:
			poliza_activa = self.mongo.db.polizas.find_one({'titular.dni': dni, 'activa': True})
			encontrado = (poliza_activa != None)
		except:
			poliza_activa = [p for p in self.polizas if (p.get_titular().get_dni() == dni) and p.get_activa() == True]
			encontrado = (len(poliza_activa) > 0)
		
		if encontrado:
			try:
				poliza_activa = Poliza.from_dict(poliza_activa)
			except:
				poliza_activa = poliza_activa[0]
				
			poliza_activa.set_activa(False)
			
			try:
				self.mongo.db.polizas.update({'id_poliza': poliza_activa.get_id_poliza()}, {'$set': poliza_activa.to_dict()})
			except:
				pass
		else:
			raise NonExistingPolicyError('Policy doesn´t exist.')

	# [HU5] Consultar póliza
	def consultar_poliza(self, dni: str):
		# Se obtiene la póliza
		try:
			poliza = self.mongo.db.polizas.find_one({'titular.dni': dni, 'activa': True})
			encontrada = (poliza != None)
		except:
			poliza = [p for p in self.polizas if p.get_titular().get_dni() == dni and p.get_activa() == True]
			encontrada = (len(poliza) > 0)
		
		if encontrada:
			try:
				poliza = Poliza.from_dict(poliza)
			except:
				poliza = poliza[0]
			
			return poliza
		else:
			raise NonExistingPolicyError('Policy doesn´t exist.')
	
	# [HU6] Subir prescripción médica
	def subir_prescripcion(self, prescripcion: Prescripcion):
		try:
			poliza_activa = self.mongo.db.polizas.find_one({'titular.dni': prescripcion.get_asegurado().get_dni(), 'activa': True})
			encontrada = (poliza_activa != None)
		except:
			poliza_activa = [p for p in self.polizas if p.get_titular().get_dni() == prescripcion.get_asegurado().get_dni() and p.get_activa()]
			encontrada = (len(poliza_activa) > 0)
		
		if encontrada:
			try:
				poliza_activa = Poliza.from_dict(poliza_activa)
			except:
				poliza_activa = poliza_activa[0]
			# Se comprueba que la prescripción esté asignada a la póliza activa del asegurado
			if prescripcion.get_id_poliza() == poliza_activa.get_id_poliza():
				dni = prescripcion.get_asegurado().get_dni()
				
				# Se compone el identificador de la póliza con el formato PR-DNI-ID_ULTIMA_PRESCRIPCION+1
				id_prescripcion = "PR-" + dni[:9]
				# Se obtienen las prescripciones previas del cliente/asegurado
				try:
					prescripciones_previas = self.mongo.db.prescripciones.find({'asegurado.dni': dni})
					prescripciones_previas = list(prescripciones_previas)
				except:
					prescripciones_previas = [p for p in self.prescripciones if p.get_asegurado().get_dni() == dni]
				
				if len(prescripciones_previas) > 0:
					prescripcion_previa = prescripciones_previas[-1]
					try:
						prescripcion_previa = Prescripcion.from_dict(prescripcion_previa)
					except:
						pass
					# Si existen prescripciones previas se obtiene el último identificador y se aumenta en uno
					id_prescripcion = id_prescripcion + str(int(prescripcion_previa.get_id_prescripcion()[-1]) + 1)
				else:
					# Si no existen prescripciones previas se marca como la primera
					id_prescripcion = id_prescripcion + "1"
				
				if isinstance(prescripcion.get_especialidad(), Especialidad):
					prescripcion.set_id_prescripcion(id_prescripcion)
				
					try:
						self.mongo.db.prescripciones.insert_one(prescripcion.to_dict())
					except:
						self.prescripciones.append(prescripcion)
				else:
					raise SpecialityError('The medical speciality is not valid.')
			else:
				raise TimedOutPrescriptionError('The prescription is not associated with the active policy.')
		else:
			raise NonActivePolicyError('User has not an active policy.')
	
	# [HU7] Solicitar autorización médica
	def solicitar_autorizacion(self, id_prescripcion: str):
		try:
			prescripcion = self.mongo.db.prescripciones.find_one({'id_prescripcion': id_prescripcion})
			encontrada = (prescripcion != None)
		except:
			prescripcion = [p for p in self.prescripciones if p.get_id_prescripcion() == id_prescripcion]
			encontrada = (len(prescripcion) > 0)
		
		# Se comprueba que la prescripción exista en el sistema
		if encontrada:
			# Se obtiene la póliza activa del asegurado
			try:
				prescripcion = Prescripcion.from_dict(prescripcion)
				poliza_activa = self.mongo.db.polizas.find_one({'titular.dni': prescripcion.get_asegurado().get_dni(), 'activa': True})
				poliza_encontrada = (poliza_activa != None)
				
			except:
				prescripcion = prescripcion[0]
				poliza_activa = [p for p in self.polizas if p.get_titular().get_dni() == prescripcion.get_asegurado().get_dni() and p.get_activa()]
				poliza_encontrada = (len(poliza_activa) > 0)
				
			if poliza_encontrada:
				try:
					poliza_activa = Poliza.from_dict(poliza_activa)
				except:
					poliza_activa = poliza_activa[0]
					
				dni = prescripcion.get_asegurado().get_dni()
				# Se compone el identificador de la póliza con el formato AU-DNI-ID_ULTIMA_AUTORIZACION+1
				id_autorizacion = "AU-" + dni[0:9]
				# Se obtienen las autorizaciones previas del cliente/asegurado
				try:
					autorizaciones_previas = self.mongo.db.autorizaciones.find({'asegurado.dni': dni})
					autorizaciones_previas = list(autorizaciones_previas)
				except:
					autorizaciones_previas = [a for a in self.autorizaciones if a.get_asegurado().get_dni() == dni]
				
				if len(autorizaciones_previas) > 0:
					autorizacion_previa = autorizaciones_previas[-1]
					try:
						autorizacion_previa = Autorizacion.from_dict(autorizacion_previa)
					except:
						pass
					# Si se han realizado autorizaciones previas se obtiene el último identificador y se aumenta en uno
					id_autorizacion = id_autorizacion + str(int(autorizacion_previa.get_id_autorizacion()[-1]) + 1)
				else:
					# Si no se han realizado autorizaciones previas se marca como la primera
					id_autorizacion = id_autorizacion + "1"
				
				# Comprobar si se rechaza algún servicio no incluido en la póliza
				servicios_rechazados = [serv for serv in prescripcion.get_servicios_solicitados() if serv in poliza_activa.get_servicios_excluidos()]
				
				if len(servicios_rechazados) > 0:
					# Se deniega la autorización
					servicios_rechazados = ','.join([str(serv) for serv in servicios_rechazados])
					motivo_rechazo = "Los servicios " + servicios_rechazados + " no se incluyen en la póliza."
					autorizacion = Autorizacion(id_autorizacion, prescripcion.get_asegurado(), id_prescripcion, poliza_activa.get_id_poliza(), False, motivo_rechazo, prescripcion.get_fecha_realizacion(), prescripcion.get_especialidad(), [""], prescripcion.get_facultativo_realizador(), prescripcion.get_consulta())
				else:
					# Se acepta la autorización
					autorizacion = Autorizacion(id_autorizacion, prescripcion.get_asegurado(), id_prescripcion, poliza_activa.get_id_poliza(), True, "", prescripcion.get_fecha_realizacion(), prescripcion.get_especialidad(), prescripcion.get_servicios_solicitados(), prescripcion.get_facultativo_realizador(), prescripcion.get_consulta())
					
				# Se almacena la autorización
				try:
					self.mongo.db.autorizaciones.insert_one(autorizacion.to_dict())
				except:
					self.autorizaciones.append(autorizacion)
			else:
				raise NonActivePolicyError('User has not an active policy.')
		else:
			raise NonExistingPrescriptionIDError('Prescription ID doesnt exist.')
			
		
	# [HU8] Administrar autorización: Crear una autorización
	def crear_autorizacion(self, autorizacion: Autorizacion):
		try:
			poliza_activa = self.mongo.db.polizas.find_one({'titular.dni': autorizacion.get_asegurado().get_dni(), 'activa': True})
			encontrada = (poliza_activa != None)
		except:
			poliza_activa = [p for p in self.polizas if p.get_titular().get_dni() == autorizacion.get_asegurado().get_dni() and p.get_activa()]
			encontrada = (len(poliza_activa) > 0)
		
		if encontrada:
			try:
				poliza_activa = Poliza.from_dict(poliza_activa)
			except:
				poliza_activa = poliza_activa[0]
			# Se comprueba que la autorización esté asignada a la póliza activa del asegurado
			if autorizacion.get_id_poliza() == poliza_activa.get_id_poliza():
				dni = autorizacion.get_asegurado().get_dni()
				
				# Se compone el identificador de la póliza con el formato AU-DNI-ID_ULTIMA_AUTORIZACION+1
				id_autorizacion = "AU-" + dni[:9]
				# Se obtienen las autorizaciones previas del cliente/asegurado
				try:
					autorizaciones_previas = self.mongo.db.autorizaciones.find({'asegurado.dni': dni})
					autorizaciones_previas = list(autorizaciones_previas)
				except:
					autorizaciones_previas = [a for a in self.autorizaciones if a.get_asegurado().get_dni() == dni]
				
				if len(autorizaciones_previas) > 0:
					autorizacion_previa = autorizaciones_previas[-1]
					try:
						autorizacion_previa = Autorizacion.from_dict(autorizacion_previa)
					except:
						pass
					# Si se han realizado autorizaciones previas se obtiene el último identificador y se aumenta en uno
					id_autorizacion = id_autorizacion + str(int(autorizacion_previa.get_id_autorizacion()[-1]) + 1)
				else:
					# Si no se han realizado autorizaciones previas se marca como la primera
					id_autorizacion = id_autorizacion + "1"
				
				autorizacion.set_id_autorizacion(id_autorizacion)

				try:
					self.mongo.db.autorizaciones.insert_one(autorizacion.to_dict())
				except:
					self.autorizaciones.append(autorizacion)
			else:
				raise TimedOutAuthorizationError('The authorization is not associated with the active policy.')
		else:
			raise NonActivePolicyError('User has not an active policy.')
			
	# [HU8] Administrar autorización: Modificar una autorización		
	def modificar_autorizacion(self, id_autorizacion: str, motivo_rechazo: str, fecha_realizacion: datetime, especialidad: Especialidad, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		# Se obtiene la autorización asociada al identificador
		try:
			aut = self.mongo.db.autorizaciones.find_one({'id_autorizacion': id_autorizacion})
			encontrada = (aut != None)
		except:
			aut = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion]
			encontrada = (len(aut) > 0)

		if encontrada:
			try:
				aut = Autorizacion.from_dict(aut)
			except:
				aut = aut[0]
			# Modificación de la autorización médica
			aut.set_motivo_rechazo(motivo_rechazo)
			aut.set_fecha_realizacion(fecha_realizacion)
			aut.set_especialidad(especialidad)
			aut.set_servicios_aceptados(servicios_aceptados)
			aut.set_facultativo_realizador(facultativo_realizador)
			aut.set_consulta(consulta)
			
			try:
				self.mongo.db.autorizaciones.update({'id_autorizacion': id_autorizacion}, {'$set': aut.to_dict()})
			except:
				pass
		else:
			raise NonExistingAuthorizationError('Authorization doesn´t exist.')
			
	# [HU9] Consultar autorización médica
	def consultar_autorizacion(self, id_autorizacion: str):
		# Se obtiene la autorizacion
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion]
		
		if len(autorizacion) > 0:
			return autorizacion[0]
		else:
			raise NonExistingAuthorizationError('Authorization doesn´t exist.')
			
	# [HU10] Aprobar/Denegar una autorización médica
	def aprobar_denegar_autorizacion(self, id_autorizacion: str, aceptada: bool, motivo_rechazo: str):
		# Se obtiene la póliza asociada al identificador
		aut = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion]

		if len(aut) > 0:
			aut = aut[0]
			# Modificación de la autorización médica
			aut.set_aceptada(aceptada)
			aut.set_motivo_rechazo(motivo_rechazo)
		else:
			raise NonExistingAuthorizationError('Authorization doesn´t exist.')
	
	# [HU11] Administrar cita médica: Crear cita médica
	def crear_cita(self, cita: Cita):
		# Se obtiene la autorización asociada para comprobar que está aceptada
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == cita.get_id_autorizacion() and a.get_aceptada() == True]
		
		if len(autorizacion) > 0:
			self.citas.append(cita)
		else:
			raise NonExistingAuthorizationError('Authorization doesn´t exist.')
	
	# [HU11] Administrar cita médica: Modificar cita médica
	def modificar_cita(self, id_cita: str, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		# Se obtiene la cita médica
		ci = [c for c in self.citas if c.get_id_autorizacion() == id_cita]
		
		if len(ci) > 0:
			ci = ci[0]
			# Modificación de la cita médica
			ci.set_fecha(fecha)
			ci.set_hora(hora)
			ci.set_facultativo_realizador(facultativo_realizador)
			ci.set_consulta(consulta)
		else:
			raise NonExistingAppointmentError('Appointment doesn´t exist.')
	
	# [HU12] Consultar cita médica
	def consultar_cita(self, id_autorizacion: str):
		# Se obtiene la cita médica
		cita = [c for c in self.citas if c.get_id_autorizacion() == id_autorizacion]
		
		if len(cita) > 0:
			return cita[0]
		else:
			raise NonExistingAppointmentError('Appointment doesn´t exist.')
	
	# [HU14] Consultar usuario
	def consultar_usuario(self, dni: str):
		# Se obtiene el usuario
		usuario = [u for u in self.usuarios if u.get_dni() == dni]
		
		if len(usuario) > 0:
			return usuario[0]
		else:
			raise NonExistingUserError('User doesn´t exist.')
