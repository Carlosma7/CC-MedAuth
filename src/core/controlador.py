from usuarioAdmin import UsuarioAdmin
from usuarioCliente import UsuarioCliente
from poliza import Poliza
from autorizacion import Autorizacion

from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra
from especialidad import Especialidad
from typing import List
import datetime

# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuariosAdmins: List[UsuarioAdmin] = []
	usuariosClientes: List[UsuarioCliente] = []
	polizas: List[Poliza] = []
	autorizaciones: List[Autorizacion] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, admin: UsuarioAdmin):
		adm = [a for a in self.usuariosAdmins if a.get_dni() == admin.get_dni()]

		if len(adm) == 0:
			# Patrón correo: email@medauth
			email_empresarial = admin.get_email().split('@')[0] + '@medauth.com'

			# Se crea el usuario administrativo
			admin.set_email_empresarial(email_empresarial)

			# Se almacena
			self.usuariosAdmins.append(admin)

	# [HU2] Creación usuario asegurado
	def crear_cliente(self, cliente: UsuarioCliente):
		cli = [c for c in self.usuariosClientes if c.get_dni() == cliente.get_dni()]

		if len(cli) == 0:
			# Se crea el usuario cliente/asegurado
			self.usuariosClientes.append(cliente)

	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, admin: UsuarioAdmin, nombre: str, email: str):
		# Se obtiene el usuario administrativo por su dni
		usuario = [c for c in self.usuariosAdmins if c.get_dni() == admin.get_dni()]

		if len(usuario) > 0:
			usuario = usuario[0]
			# Se modifica la información
			usuario.set_nombre(nombre)
			usuario.set_email(email)
			email_empresarial = email.split('@')[0] + '@medauth.com'
			usuario.set_email_empresarial(email_empresarial)

	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, cliente: UsuarioCliente, nombre: str, email: str, cuenta_bancaria: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		usuario = [c for c in self.usuariosClientes if c.get_dni() == cliente.get_dni()]
		
		if len(usuario) > 0:
			usuario = usuario[0]
			# Se modifica la información
			usuario.set_nombre(nombre)
			usuario.set_email(email)
			usuario.set_cuenta_bancaria(cuenta_bancaria)

	# [HU3] Administrar usuario: Eliminar administrador
	def eliminar_admin(self, dni: str):
		admin_buscado = [c for c in self.usuariosAdmins if c.get_dni() == dni]

		if len(admin_buscado) > 0:
			# Se elimina el usuario
			self.usuariosAdmins.remove(admin_buscado[0])

	# [HU3] Administrar usuario: Eliminar cliente
	def eliminar_cliente(self, dni: str):
		cliente_buscado = [c for c in self.usuariosClientes if c.get_dni() == dni]

		if len(cliente_buscado) > 0:
			# Se elimina el usuario
			self.usuariosClientes.remove(cliente_buscado[0])

	# [HU4] Administrar póliza: Crear una póliza
	def crear_poliza(self, poliza: Poliza):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuariosClientes if c.get_dni() == poliza.get_titular().get_dni()][0]

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

	# [HU4] Administrar póliza: Desactivar una póliza
	def desactivar_poliza(self, dni: str):
		poliza_activa = [p for p in self.polizas if (p.get_titular().get_dni() == dni) and p.get_activa() == True]
		
		if len(poliza_activa) > 0:
			poliza_activa[0].set_activa(False)

	# [HU5] Consultar póliza
	def consultar_poliza(self, dni: str):
		# Se obtiene la póliza
		poliza = [p for p in self.polizas if p.get_titular().get_dni() == dni and p.get_activa() == True][0]
		
		return poliza
		
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
			
			
			
			
			
			
