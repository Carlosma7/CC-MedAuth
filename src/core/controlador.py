from usuario import Usuario
from usuarioAdmin import UsuarioAdmin
from usuarioCliente import UsuarioCliente
from poliza import Poliza
from prescripcion import Prescripcion
from autorizacion import Autorizacion
from cita import Cita

from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra
from especialidad import Especialidad
from typing import List
import datetime
import re

# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuarios: List[Usuario] = []
	polizas: List[Poliza] = []
	prescripciones: List[Prescripcion] = []
	autorizaciones: List[Autorizacion] = []
	cita: List[Cita] = []
	
	# [HU1] Creación usuario administrativo
	# [HU2] Creación usuario asegurado
	def crear_usuario(self, usuario: Usuario, tipo_usuario: int):
		usr = [u for u in self.usuarios if u.get_dni() == usuario.get_dni()]
		
		# Comprobar si el DNI existe en los usuarios existentes
		if len(usr) == 0:
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
							raise ValueError('IBAN not valid.')
					else:
						raise ValueError('Wrong user type.')
						
					# Se almacena
					self.usuarios.append(usr_creado)
				
				else:
					raise ValueError('Email not valid.')
			else:
				raise ValueError('DNI not valid.')
			
		else:
			raise ValueError('An user exists with DNI provided.')
			

	# [HU3] Administrar usuario: Modificar usuario
	def modificar_usuario(self, usuario: Usuario, nombre: str, email: str, cuenta_bancaria: str):
		# Se obtiene el usuario por su dni
		usuario = [u for u in self.usuarios if u.get_dni() == usuario.get_dni()]
		
		if len(usuario) > 0:
			usuario = usuario[0]
			# Comprobar correo
			if bool(re.match("([a-zA-Z0-9]+@[a-zA-Z]+\.)(com|es)", usuario.get_email())):
				# Se modifica la información
				usuario.set_nombre(nombre)
				usuario.set_email(email)
				
				if usuario.get_tipo() == 0: # Admin
					email_empresarial = email.split('@')[0] + '@medauth.com'
					usuario.set_email_empresarial(email_empresarial)
				else: # Cliente
					usuario.set_cuenta_bancaria(cuenta_bancaria)
					
			else:
				raise ValueError('Email not valid.')
		else:
			raise ValueError('User doesn´t exist.')

	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		usuario_buscado = [u for u in self.usuarios if u.get_dni() == dni]
		
		if len(usuario_buscado) > 0:
			# Se elimina el usuario
			self.usuarios.remove(usuario_buscado[0])
		else:
			raise ValueError('User doesn´t exist.')

	# [HU4] Administrar póliza: Crear una póliza
	def crear_poliza(self, poliza: Poliza):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == poliza.get_titular().get_dni()]
		
		if len(cliente) > 0:
			cliente = cliente[0]

			# Se compone el identificador de la póliza con el formato MA-DNI-ID_ULTIMA_POLIZA+1
			dni = cliente.get_dni()
			id_poliza = "MA-" + dni[:9]
			# Se obtienen las polizas previas
			polizas_previas = [p for p in self.polizas if p.get_id_poliza()[:12] == id_poliza]

			if len(polizas_previas) > 0:
				# Si posee polizas previas canceladas, se obtiene el ID de la última que tuvo
				id_poliza = id_poliza + str(int(polizas_previas[-1][-1]) + 1)
			else:
				# Si es la primera se crea como tal
				id_poliza = id_poliza + "1"

			poliza.set_id_poliza(id_poliza)

			self.polizas.append(poliza)
		else:
			raise ValueError('User doesn´t exist.')

	# [HU4] Administrar póliza: Modificar una póliza
	def modificar_poliza(self, poliza: Poliza, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: float, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		# Se obtiene su póliza activa
		id_poliza = poliza.get_id_poliza()
		
		# Se obtiene la póliza asociada al identificador
		pol = [p for p in self.polizas if p.get_id_poliza() == id_poliza]

		if len(pol) > 0:
			pol = pol[0]
			# Modificación de la póliza
			pol.set_periodo_carencia(periodo_carencia)
			pol.set_tipo(tipo)
			pol.set_copagos(copagos)
			pol.set_mensualidad(mensualidad)
			pol.set_servicios_excluidos(servicios_excluidos)
			pol.set_modulos_extra(modulos_extra)
		else:
			raise ValueError('Policy doesn´t exist.')

	# [HU4] Administrar póliza: Desactivar una póliza
	def desactivar_poliza(self, dni: str):
		poliza_activa = [p for p in self.polizas if (p.get_titular().get_dni() == dni) and p.get_activa() == True]
		
		if len(poliza_activa) > 0:
			poliza_activa[0].set_activa(False)
		else:
			raise ValueError('Policy doesn´t exist.')

	# [HU5] Consultar póliza
	def consultar_poliza(self, dni: str):
		# Se obtiene la póliza
		poliza = [p for p in self.polizas if p.get_titular().get_dni() == dni and p.get_activa() == True]
		
		if len(poliza) > 0:
			return poliza[0]
		else:
			raise ValueError('Policy doesn´t exist.')
	
	# [HU6] Subir prescripción médica
	def subir_prescripcion(self, prescripcion: Prescripcion):
		poliza_activa = [p for p in self.polizas if p.get_titular().get_dni() == prescripcion.get_asegurado().get_dni()]
		
		if len(poliza_activa) > 0:
			poliza_activa = poliza_activa[-1]
			# Se comprueba que la prescripción esté asignada a la póliza activa del asegurado
			if prescripcion.get_id_poliza() == poliza_activa.get_id_poliza():
				dni = prescripcion.get_asegurado().get_dni()
				
				# Se compone el identificador de la póliza con el formato PR-DNI-ID_ULTIMA_PRESCRIPCION+1
				id_prescripcion = "PR-" + dni[:9]
				# Se obtienen las prescripciones previas del cliente/asegurado
				prescripciones_previas = [p for p in self.prescripciones if p.get_asegurado().get_dni() == dni]
				
				if len(prescripciones_previas) > 0:
					# Si existen prescripciones previas se obtiene el último identificador y se aumenta en uno
					id_prescripcion = id_prescripcion + str(int(prescripciones_previas[-1][-1]) + 1)
				else:
					# Si no existen prescripciones previas se marca como la primera
					id_prescripcion = id_prescripcion + "1"
				
				prescripcion.set_id_prescripcion(id_prescripcion)
				
				self.prescripciones.append(prescripcion)
			else:
				raise ValueError('The prescription is not associated with the active policy.')
		else:
			raise ValueError('User has not an active policy.')
		
	# [HU8] Administrar autorización: Crear una autorización
	def crear_autorizacion(self, autorizacion: Autorizacion):
		poliza_activa = [p for p in self.polizas if p.get_titular().get_dni() == autorizacion.get_asegurado().get_dni()]
		
		if len(poliza_activa) > 0:
			poliza_activa = poliza_activa[-1]
			# Se comprueba que la autorización esté asignada a la póliza activa del asegurado
			if autorizacion.get_id_poliza() == poliza_activa.get_id_poliza():
				dni = autorizacion.get_asegurado().get_dni()
				
				# Se compone el identificador de la póliza con el formato AU-DNI-ID_ULTIMA_AUTORIZACION+1
				id_autorizacion = "AU-" + dni[:9]
				# Se obtienen las autorizaciones previas del cliente/asegurado
				autorizaciones_previas = [a for a in self.autorizaciones if a.get_asegurado().get_dni() == dni]
				
				if len(autorizaciones_previas) > 0:
					# Si se han realizado autorizaciones previas se obtiene el último identificador y se aumenta en uno
					id_autorizacion = id_autorizacion + str(int(autorizaciones_previas[-1][-1]) + 1)
				else:
					# Si no se han realizado autorizaciones previas se marca como la primera
					id_autorizacion = id_autorizacion + "1"
				
				autorizacion.set_id_autorizacion(id_autorizacion)

				self.autorizaciones.append(autorizacion)
			else:
				raise ValueError('The authorization is not associated with the active policy.')
		else:
			raise ValueError('User has not an active policy.')
			
	# [HU8] Administrar autorización: Modificar una autorización		
	def modificar_autorizacion(self, autorizacion: Autorizacion, motivo_rechazo: str, fecha_realizacion: datetime, especialidad: Especialidad, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		# Se obtiene la póliza asociada al identificador
		aut = [a for a in self.autorizaciones if a.get_id_autorizacion() == autorizacion.get_id_autorizacion()]

		if len(aut) > 0:
			aut = aut[0]
			# Modificación de la autorización médica
			autorizacion.set_motivo_rechazo(motivo_rechazo)
			autorizacion.set_fecha_realizacion(fecha_realizacion)
			autorizacion.set_especialidad(especialidad)
			autorizacion.set_servicios_aceptados(servicios_aceptados)
			autorizacion.set_facultativo_realizador(facultativo_realizador)
			autorizacion.set_consulta(consulta)
		else:
			raise ValueError('User has not an active policy.')
			
	# [HU9] Consultar autorización médica
	def consultar_autorizacion(self, id_autorizacion: str):
		# Se obtiene la autorizacion
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion]
		
		if len(autorizacion) > 0:
			return autorizacion[0]
		else:
			raise ValueError('Authorization doesn´t exist.')
			
	# [HU10] Aprobar/Denegar una autorización médica
	def aprobar_denegar_autorizacion(self, autorizacion: Autorizacion, aceptada: bool, motivo_rechazo: str):
		# Se obtiene la póliza asociada al identificador
		aut = [a for a in self.autorizaciones if a.get_id_autorizacion() == autorizacion.get_id_autorizacion()]

		if len(aut) > 0:
			aut = aut[0]
			# Modificación de la autorización médica
			autorizacion.set_estado(aceptada)
			autorizacion.set_motivo_rechazo(motivo_rechazo)
		else:
			raise ValueError('Authorization doesn´t exist.')
	
	# [HU11] Administrar cita médica: Crear cita médica
	def crear_cita(self, cita: Cita):
		# Se obtiene la autorización asociada para comprobar que está aceptada
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == cita.get_id_autorizacion() and a.get_aceptada() == True]
		
		if len(autorizacion) > 0:
			self.citas.append(cita)
		else:
			raise ValueError('Authorization doesn´t exist.')
	
	# [HU11] Administrar cita médica: Modificar cita médica
	def modificar_cita(self, cita: Cita, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		# Se obtiene la cita médica
		ci = [c for c in self.citas if c.get_id_autorizacion() == cita.get_id_autorizacion()]
		
		if len(ci) > 0:
			ci = ci[0]
			# Modificación de la cita médica
			ci.set_fecha(fecha)
			ci.set_hora(hora)
			ci.set_facultativo_realizador(facultativo_realizador)
			ci.set_consulta(consulta)
		else:
			raise ValueError('Appointment doesn´t exist.')
	
	# [HU12] Consultar cita médica
	def consultar_cita(self, id_autorizacion: str):
		# Se obtiene la cita médica
		cita = [c for c in self.citas if c.get_id_autorizacion() == id_autorizacion]
		
		if len(cita) > 0:
			return cita[0]
