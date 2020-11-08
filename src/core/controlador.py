from modelos import *
from typing import List


# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuarios: List[Usuario] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, nombre: str, email: str, dni: str):
		# Patrón correo: email@medauth
		email_empresarial = email.split('@')[0] + '@medauth.com'

		# Se crea el usuario administrativo
		c = UsuarioAdmin(nombre, email, dni, email_empresarial)

		# Se almacena
		self.usuarios.append(c)

	# [HU2] Creación usuario asegurado
	def crear_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		# Se crea el usuario cliente/asegurado
		c = UsuarioCliente(nombre, email, dni, cuenta_bancaria, 'a')

		# Se almacena
		self.usuarios.append(c)

	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, nombre: str, email: str, dni: str):
		# Se obtiene el usuario administrativo por su dni
		admin = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se modifica la información
		admin.set_nombre(nombre)
		admin.set_email(email)
		email_empresarial = email.split('@')[0] + '@medauth.com'
		admin.set_email_empresarial(email_empresarial)

	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se modifica la información
		cliente.set_nombre(nombre)
		cliente.set_email(email)
		cliente.set_cuenta_bancaria(cuenta_bancaria)
	
	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		# Se obtiene el usuario por su dni
		usuario = [c for c in self.usuarios if c.get_dni() == dni][0]

		# Se elimina el usuario
		self.usuarios.remove(usuario)

	# [HU4] Administrar póliza: Crear una póliza
	def crear_poliza(self, dni: str, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: str, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se comprueba que no tiene actualmente ninguna póliza activa
		poliza_activa = [p for p in self.polizas if p.get_id_poliza() == cliente.get_id_poliza() and p.get_activa() == True]
		assert len(poliza_activa) == 0
		
		# Se compone el identificador de la póliza con el formato MA-DNI-ID_ULTIMA_POLIZA+1
		id_poliza = "MA-" + dni[:9]
		# Se obtienen las polizas previas
		polizas_previas = [p for p in self.polizas if p.get_id_poliza()[:12] == id_poliza]
		
		if len(polizas_previas) > 0:
			# Si posee polizas previas canceladas, se obtiene el ID de la última que tuvo
			id_poliza = id_poliza + str(int(polizas_previas[-1][-1]) + 1)
		else:
			# Si es la primera se crea como tal
			id_poliza = id_poliza + "1"

		# Se crea la póliza y se almacena
		p = Poliza(cliente, id_poliza, periodo_carencia, tipo, copagos, mensualidad, servicios_excluidos, modulos_extra, True)

		self.polizas.append(p)
		
		# Se le asigna la póliza al cliente/asegurado
		cliente.set_id_poliza(id_poliza)
		
	# [HU4] Administrar póliza: Modificar una póliza
	def modificar_poliza(self, dni: str, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: float, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se obtiene su póliza activa
		id_poliza = cliente.get_id_poliza()
		
		# Se obtiene la póliza asociada al identificador
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		
		# Modificación de la póliza
		poliza.set_periodo_carencia(periodo_carencia)
		poliza.set_tipo(tipo)
		poliza.set_copagos(copagos)
		poliza.set_mensualidad(mensualidad)
		poliza.set_servicios_excluidos(servicios_excluidos)
		poliza.set_modulos_extra(modulos_extra)
	
	# [HU4] Administrar póliza: Desactivar una póliza
	def desactivar_poliza(self, dni: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]

		# Se obtiene el identificador de la póliza activa del cliente/asegurado
		id_poliza = cliente.get_id_poliza()

		# Se obtiene la póliza
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		
		# Se anula el identificador de la póliza para el cliente
		cliente.set_id_poliza("")
		
		# Se desactiva la póliza
		poliza.set_activa(False)

	# [HU5] Consultar póliza
	def consultar_poliza(self, dni: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se obtiene el identificador de la póliza activa
		id_poliza = cliente.get_id_poliza()

		# Se obtiene la póliza
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		
		return poliza

	# [HU6] Añadir prescripción médica
	def subir_prescripcion(self, archivo: json):
		return

	# [HU7] Solicitar autorización médica
	def solicitar_autorizacion(self, id_prescripcion: str, asegurado: UsuarioCliente):
		return

	# [HU8] Administrar autorización médica: Crear autorización
	def crear_autorizacion(self, dni: str, id_prescripcion: str, aceptada: bool, motivo_rechazo: str, fecha_realizacion: datetime, especialidad: Especialidad, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]

		# Se obtiene el identificador de la poliza activa
		id_poliza = cliente.get_id_poliza()

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

		# Se crea la autorización
		a = Autorizacion(id_autorizacion, cliente, id_prescripcion, id_poliza, aceptada, motivo_rechazo, fecha_realizacion, especialidad, servicios_aceptados, facultativo_realizador, consulta)

		# Se almacena la autorización
		self.autorizaciones.append(a)

	# [HU8] Administrar autorización médica: Modificar autorización
	def modificar_autorizacion(self, id_autorizacion: str, motivo_rechazo: str, fecha_realizacion: datetime, especialidad: Especialidad, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		# Se obtiene la autorización a partir de su identificación
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]

		# Modificación de la autorización
		autorizacion.set_motivo_rechazo(motivo_rechazo)
		autorizacion.set_fecha_realizacion(fecha_realizacion)
		autorizacion.set_especialidad(especialidad)
		autorizacion.set_servicios_aceptados(servicios_aceptados)
		autorizacion.set_facultativo_realizador(facultativo_realizador)
		autorizacion.set_consulta(consulta)

	# [HU9] Consultar autorización médica
	def consultar_autorizacion(self, id_autorizacion: str):
		# Se obtiene la autorización a partir de su identificación
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]
		
		return autorizacion