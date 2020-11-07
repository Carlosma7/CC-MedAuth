from modelos import *
from typing import List
import pytest
from random import randint
import datetime
import json


class TestController:

	usuarios: List[TestUsuario] = []
	polizas: List[TestPoliza] = []
	prescripciones: List[TestPrescripcion] = []
	autorizaciones: List[TestAutorizacion] = []
	citas: List[TestCita] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, nombre: str, email: str, dni: str):
		email_empresarial = email.split('@')[0] + '@medauth.com'
		c = TestUsuarioAdmin(nombre, email, dni, email_empresarial)
		len_antes = len(self.usuarios)
		self.usuarios.append(c)
		assert len(self.usuarios) > len_antes
		
		admin = [a for a in self.usuarios if a.get_dni() == dni][0]
		assert admin.get_nombre() == nombre
		assert admin.get_email() == email
		assert admin.get_email_empresarial() == email_empresarial
	
	# [HU2] Creación usuario asegurado
	def crear_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		c = TestUsuarioCliente(nombre, email, dni, cuenta_bancaria, 'a')
		len_antes = len(self.usuarios)
		self.usuarios.append(c)
		assert len(self.usuarios) > len_antes
		
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_nombre() == nombre
		assert cliente.get_email() == email
		assert cliente.get_cuenta_bancaria() == cuenta_bancaria
		
	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, nombre: str, email: str, dni: str):
		admin = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert admin.get_dni() == dni
		
		admin.set_nombre(nombre)
		admin.set_email(email)
		email_empresarial = email.split('@')[0] + '@medauth.com'
		admin.set_email_empresarial(email_empresarial)
		
		assert admin.get_nombre() == nombre
		assert admin.get_email() == email
		assert admin.get_email_empresarial() == email_empresarial
	
	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_dni() == dni
		
		cliente.set_nombre(nombre)
		cliente.set_email(email)
		cliente.set_cuenta_bancaria(cuenta_bancaria)
		
		assert cliente.get_nombre() == nombre
		assert cliente.get_email() == email
		assert cliente.get_cuenta_bancaria() == cuenta_bancaria
		
	
	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		len_antes = len(self.usuarios)
		usuario = [c for c in self.usuarios if c.get_dni() == dni][0]
		self.usuarios.remove(usuario)
		assert len(self.usuarios) < len_antes
	
	# [HU4] Administrar póliza: Crear una póliza
	def crear_poliza(self, dni: str, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: str, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		poliza_activa = [p for p in self.polizas if p.get_id_poliza() == cliente.get_id_poliza() and p.get_activa() == True]
		assert len(poliza_activa) == 0
		
		id_poliza = "MA-" + dni[:9]
		polizas_previas = [p for p in self.polizas if p.get_id_poliza()[:12] == id_poliza]
		if len(polizas_previas) > 0:
			id_poliza = id_poliza + str(int(polizas_previas[-1][-1]) + 1)
		else:
			id_poliza = id_poliza + "1"

		polizas = [p for p in self.polizas if p.get_id_poliza() == id_poliza]
		assert len(polizas) == 0
			
		cliente.set_id_poliza(id_poliza)
		assert cliente.get_id_poliza() == id_poliza
		
		p = TestPoliza(cliente, id_poliza, periodo_carencia, tipo, copagos, mensualidad, servicios_excluidos, modulos_extra, True)
		len_antes = len(self.polizas)
		self.polizas.append(p)
		assert len(self.polizas) > len_antes

		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		assert poliza.get_titular() == cliente
		assert poliza.get_id_poliza() == id_poliza
		assert poliza.get_periodo_carencia() == periodo_carencia
		assert poliza.get_tipo() == tipo
		assert poliza.get_copagos() == copagos
		assert poliza.get_mensualidad() == mensualidad
		assert poliza.get_servicios_excluidos() == servicios_excluidos
		assert poliza.get_modulos_extra() == modulos_extra
		
	# [HU4] Administrar póliza: Modificar una póliza
	def modificar_poliza(self, dni: str, periodo_carencia: datetime, tipo: TipoPoliza, copagos: float, mensualidad: float, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra]):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		id_poliza = cliente.get_id_poliza()
		assert cliente.get_dni() == dni
		
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		assert poliza.get_id_poliza() == id_poliza
		
		poliza.set_periodo_carencia(periodo_carencia)
		poliza.set_tipo(tipo)
		poliza.set_copagos(copagos)
		poliza.set_mensualidad(mensualidad)
		poliza.set_servicios_excluidos(servicios_excluidos)
		poliza.set_modulos_extra(modulos_extra)
		
		assert poliza.get_periodo_carencia() == periodo_carencia
		assert poliza.get_tipo() == tipo
		assert poliza.get_copagos() == copagos
		assert poliza.get_mensualidad() == mensualidad
		assert poliza.get_servicios_excluidos() == servicios_excluidos
		assert poliza.get_modulos_extra() == modulos_extra
		assert poliza.get_activa() == True
	
	# [HU4] Administrar póliza: Desactivar una póliza
	def desactivar_poliza(self, dni: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		id_poliza = cliente.get_id_poliza()
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		assert poliza.get_id_poliza() == cliente.get_id_poliza()
		
		cliente.set_id_poliza("")
		assert cliente.get_id_poliza() == ""
		
		poliza.set_activa(False)
		assert poliza.get_activa() == False
	
	# [HU5] Consultar póliza
	def consultar_poliza(self, dni: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_dni() == dni
		
		id_poliza = cliente.get_id_poliza()
		poliza = [p for p in self.polizas if p.get_id_poliza() == id_poliza][0]
		assert poliza.get_id_poliza() == id_poliza
		
		return poliza

	# [HU6] Añadir prescripción médica
	def subir_prescripcion(self, archivo: json):
		return

	# [HU7] Solicitar autorización médica
	def solicitar_autorizacion(self, id_prescripcion: str, asegurado: TestUsuarioCliente):
		return

	# [HU8] Administrar autorización médica: Crear autorización
	def crear_autorizacion(self, dni: str, id_prescripcion: str, estado: str, motivo_rechazo: str, fecha_realizacion: datetime, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_dni() == dni

		id_poliza = cliente.get_id_poliza()

		id_autorizacion = "AU-" + dni[:9]
		autorizaciones_previas = [a for a in self.autorizaciones if a.get_asegurado().get_dni() == dni]
		if len(autorizaciones_previas) > 0:
			id_autorizacion = id_autorizacion + str(int(autorizaciones_previas[-1][-1]) + 1)
		else:
			id_autorizacion = id_autorizacion + "1"

		autorizaciones = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion]
		assert len(autorizaciones) == 0

		a = TestAutorizacion(id_autorizacion, cliente, id_prescripcion, id_poliza, estado, motivo_rechazo, fecha_realizacion, servicios_aceptados, facultativo_realizador, consulta)
		len_antes = len(self.autorizaciones)
		self.autorizaciones.append(a)
		assert len(self.autorizaciones) > len_antes

		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]
		assert autorizacion.get_id_autorizacion() == id_autorizacion
		assert autorizacion.get_asegurado() == cliente
		assert autorizacion.get_id_prescripcion() == id_prescripcion
		assert autorizacion.get_id_poliza() == id_poliza
		assert autorizacion.get_estado() == estado
		assert autorizacion.get_motivo_rechazo() == motivo_rechazo
		assert autorizacion.get_fecha_realizacion() == fecha_realizacion
		assert autorizacion.get_servicios_aceptados() == servicios_aceptados
		assert autorizacion.get_facultativo_realizador() == facultativo_realizador
		assert autorizacion.get_consulta() == consulta

	# [HU8] Administrar autorización médica: Modificar autorización
	def modificar_autorizacion(self, id_autorizacion: str, motivo_rechazo: str, fecha_realizacion: datetime, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]
		assert autorizacion.get_id_autorizacion() == id_autorizacion

		autorizacion.set_motivo_rechazo(motivo_rechazo)
		autorizacion.set_fecha_realizacion(fecha_realizacion)
		autorizacion.set_servicios_aceptados(servicios_aceptados)
		autorizacion.set_facultativo_realizador(facultativo_realizador)
		autorizacion.set_consulta(consulta)
		
		assert autorizacion.get_motivo_rechazo() == motivo_rechazo
		assert autorizacion.get_fecha_realizacion() == fecha_realizacion
		assert autorizacion.get_servicios_aceptados() == servicios_aceptados
		assert autorizacion.get_facultativo_realizador() == facultativo_realizador
		assert autorizacion.get_consulta() == consulta

	# [HU9] Consultar autorización médica
	def consultar_autorizacion(self, id_autorizacion: str):
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]
		assert autorizacion.get_id_autorizacion() == id_autorizacion
		
		return autorizacion

	# [HU10] Aprobar/Denegar una autorización médica
	def cambiar_estado_autorizacion(self, id_autorizacion: str, estado: str, motivo_rechazo: str):
		autorizacion = [a for a in self.autorizaciones if a.get_id_autorizacion() == id_autorizacion][0]
		assert autorizacion.get_id_autorizacion() == id_autorizacion

		autorizacion.set_estado(estado)
		autorizacion.set_motivo_rechazo(motivo_rechazo)

		assert autorizacion.get_estado() == estado
		assert autorizacion.get_motivo_rechazo() == motivo_rechazo

	# [HU11] Administrar cita médica: Crear cita médica
	def crear_cita(self, dni: str, id_autorizacion: str, id_prescripcion: str, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_dni() == dni

		c = TestCita(id_autorizacion, cliente, id_prescripcion, fecha, hora, facultativo_realizador, consulta)
		len_antes = len(self.citas)
		self.citas.append(c)
		assert len(self.citas) > len_antes
		
		cita = [c for c in self.citas if c.get_id_autorizacion() == id_autorizacion][0]
		assert cita.get_id_autorizacion() == id_autorizacion
		assert cita.get_asegurado() == cliente
		assert cita.get_id_prescripcion() == id_prescripcion
		assert cita.get_fecha() == fecha
		assert cita.get_hora() == hora
		assert cita.get_facultativo_realizador() == facultativo_realizador
		assert cita.get_consulta() == consulta

	# [HU11] Administrar cita médica: Modificar cita médica
	def modificar_cita(self, id_autorizacion: str, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		cita = [c for c in self.citas if c.get_id_autorizacion() == id_autorizacion][0]
		assert cita.get_id_autorizacion() == id_autorizacion

		cita.set_fecha(fecha)
		cita.set_hora(hora)
		cita.set_facultativo_realizador(facultativo_realizador)
		cita.set_consulta(consulta)
		
		assert cita.get_fecha() == fecha
		assert cita.get_hora() == hora
		assert cita.get_facultativo_realizador() == facultativo_realizador
		assert cita.get_consulta() == consulta

	# [HU12] Consultar cita médica
	def consultar_cita(self, id_autorizacion: str):
		cita = [c for c in self.citas if c.get_id_autorizacion() == id_autorizacion][0]
		assert cita.get_id_autorizacion() == id_autorizacion
		
		return cita



		
def test_crear_admin():
	t = TestController()
	t.crear_admin("Carlos", "carlos7ma@gmail.com", "75925767-F")
	
def test_crear_cliente():
	t = TestController()
	t.crear_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES12345678")
	
def test_modificar_admin():
	t = TestController()
	t.modificar_admin("Carlos", "terceto@gmail.com", "75925767-F")

def test_modificar_cliente():
	t = TestController()
	t.modificar_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES11223344")

def test_eliminar_usuario():
	t = TestController()
	t.eliminar_usuario("75925767-F")

def test_crear_poliza():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	t.crear_poliza("77925767-Z", fecha, TipoPoliza.Total, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])

def test_modificar_poliza():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	t.modificar_poliza("77925767-Z", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])

def test_consultar_poliza():
	t = TestController()
	t.consultar_poliza("77925767-Z")
	
def test_desactivar_poliza():
	t = TestController()
	t.desactivar_poliza("77925767-Z")

def test_crear_autorizacion():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	t.crear_autorizacion("77925767-Z", "PR-77925767-1", "Aceptada", "", fecha, ["Radiografía", "Ortopedia"], "D. Miguel", "Centro médico capital, Sala 2")

def test_modificar_autorizacion():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	t.modificar_autorizacion("AU-77925767-1", "", fecha, ["Radiografía", "Ortopedia"], "D. Fernando", "Centro médico capital, Sala 2")

def test_consultar_autorizacion():
	t = TestController()
	t.consultar_autorizacion("AU-77925767-1")

def test_cambiar_estado_autorizacion():
	t = TestController()
	t.cambiar_estado_autorizacion("AU-77925767-1", "Rechazado", "La póliza actual no cubre la intervención")

def test_crear_cita():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	t.crear_cita("77925767-Z", "AU-77925767-1", "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")

def test_modificar_cita():
	t = TestController()
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	t.modificar_cita("AU-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")

def test_consultar_cita():
	t = TestController()
	t.consultar_cita("AU-77925767-1")