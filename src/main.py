import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from controlador import *
import datetime

if __name__ == '__main__':
	controlador = Controller()
	
	#################################################################
	#          [HU1] Creación usuario administrativo                #
	#################################################################
	# Creación de usuario administrador
	admin = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	# Crear administrador
	controlador.crear_usuario(admin, 0)
	
	#################################################################
	#             [HU2] Creación usuario asegurado                  #
	#################################################################
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	# Crear cliente
	controlador.crear_usuario(cliente, 1)

	#################################################################
	#   [HU3] Administrar usuario: Modificación administrador       #
	#################################################################
	# Creación de usuario administrador
	adminAntiguo = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	# Modificación de usuario administrador
	controlador.modificar_usuario(adminAntiguo, 'Carlos', 'charles@gmail.com', "")
	
	#################################################################
	#      [HU3] Administrar usuario: Modificación cliente          #
	#################################################################
	# Creación de usuario cliente
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	# Modificación de usuario cliente
	controlador.modificar_usuario(clienteAntiguo, 'Juan', 'juan@gmail.com', "ES1298742874928365740192")
	
	#################################################################
	#   [HU3] Administrar usuario: Eliminar usuario administrador   #
	#################################################################
	# Creación de usuario administrativo
	admin = UsuarioAdmin("Carlos", "charles@gmail.com", "75925767-F", "charles@medauth.com")
	# Eliminar el usuario administrativo
	controlador.eliminar_usuario(admin.get_dni())

	#################################################################
	#     [HU3] Administrar usuario: Eliminar usuario cliente       #
	#################################################################
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1298742874928365740192")
	# Eliminar el usuario cliente
	controlador.eliminar_usuario(cliente.get_dni())
	
	#################################################################
	#          [HU4] Administrar póliza: Crear una póliza           #
	#################################################################
	# Creación de usuario cliente
	cliente = UsuarioCliente("Alejandro", "alex@gmail.com", "75125767-F", "ES9934567899283722194827")
	# Crear cliente
	controlador.crear_usuario(cliente, 1)
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación objeto Póliza
	p = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Crear póliza
	controlador.crear_poliza(p)
	
	#################################################################
	#        [HU4] Administrar póliza: Modificar una póliza         #
	#################################################################
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	if len(cliente) > 0:
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Modificación de póliza
		controlador.modificar_poliza(polizaAntigua, fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
	
	#################################################################
	#                    [HU5] Consultar póliza                     #
	#################################################################
	# Consultar póliza del controlador con el DNI del asegurado asociado
	poliza2 = controlador.consultar_poliza("75125767-F")
	
	#################################################################
	#        [HU4] Administrar póliza: Desactivar una póliza        #
	#################################################################
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	if len(cliente) > 0:
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza activa
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Desactivación de la póliza
		controlador.desactivar_poliza(polizaAntigua.get_titular().get_dni())

	#################################################################
	#               [HU6] Subir prescripción médica                 #
	#################################################################
	# Creación de usuario cliente
	cliente = UsuarioCliente("Marcos", "marcos@gmail.com", "28394819-T", "ES9912345392003384830729")
	# Crear usuario cliente
	controlador.crear_usuario(cliente, 1)
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación Póliza activa
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 9.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Crear Póliza
	controlador.crear_poliza(poliza)
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación prescripción con usuario y póliza
	prescripcion = Prescripcion(cliente.get_dni(), cliente, poliza.get_id_poliza(), fecha_realizacion, Especialidad.Epidemiologia, "D. Miguel", "D. Fernando", ["Serología", "PCR"], "Consulta 3")
	# Crear prescripción
	controlador.subir_prescripcion(prescripcion)
	
	#################################################################
	#    [HU8] Administrar autorización: Crear una autorización     #
	#################################################################
	# Creación de usuario cliente
	cliente = UsuarioCliente("Julio", "julio1@gmail.com", "77223418-R", "ES9912345811003387447729")
	# Crear usuario cliente
	controlador.crear_usuario(cliente, 1)
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación Póliza activa
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 9.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Crear Póliza
	controlador.crear_poliza(poliza)
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación autorización con usuario y póliza
	autorizacion = Autorizacion(cliente.get_dni(), cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
	# Crear autorización
	controlador.crear_autorizacion(autorizacion)
	
	#################################################################
	#  [HU8] Administrar autorización: Modificar una autorización   #
	#################################################################
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "77223418-R"]
	# Obtener póliza por el ID
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-77223418-1"]
	if len(cliente) > 0 and len(poliza) > 0:
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
		# Modificar la autorización
		controlador.modificar_autorizacion(autorizacionAntigua, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		
	#################################################################
	#              [HU9] Consultar autorización médica              #
	#################################################################
	# Consultar autorización del controlador con el ID de la autorización
	autorizacion2 = controlador.consultar_autorizacion("AU-77223418-1")
	
	#################################################################
	#         [HU10] Aprobar/Denegar una autorización médica        #
	#################################################################
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "77223418-R"]
	# Obtener póliza por el ID
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-77223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Denegar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacionAntigua, False, "Servicio no cubierto en póliza.")
	
	#################################################################
	#       [HU11] Administrar cita médica: Crear cita médica       #
	#################################################################
	# Obtener autorización por el ID
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_autorizacion() == "AU-77223418-1"]
	if len(autorizacion) > 0:
		autorizacion = autorizacion[0]
		# Aprobar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacion, True, "")
		# Creación hora
		hora = datetime.time(3, 45, 12)
		# Creación de cita
		cita = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		# Crear cita
		controlador.crear_cita(cita)
	
	#################################################################
	#     [HU11] Administrar cita médica: Modificar cita médica     #
	#################################################################
	# Obtener cita por el ID
	cita = [c for c in controlador.citas if c.get_id_autorizacion() == "AU-77223418-1"]
	
	if len(cita) > 0:
		cita = cita[0]
		# Creación hora
		hora = datetime.time(3, 30, 11)
		# Creación de cita
		citaAntigua = Cita(cita.get_id_autorizacion(), cita.get_asegurado(), cita.get_id_prescripcion(), cita.get_fecha(), cita.get_hora(), cita.get_facultativo_realizador(), cita.get_consulta())
		# Modificar cita
		controlador.modificar_cita(citaAntigua, cita.get_fecha(), hora, cita.get_facultativo_realizador(), cita.get_consulta())
	
	#################################################################
	#                  [HU12] Consultar cita médica                 #
	#################################################################
	# Consultar cita
	cita2 = controlador.consultar_cita("AU-77223418-1")
