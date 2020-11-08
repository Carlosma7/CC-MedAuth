from core import Controller
from core.modelos import *

if __name__ == '__main__':
	c = Controller()
	
	# [HU1] Creación usuario administrativo
	c.crear_admin("Carlos", "carlos7ma@gmail.com", "75925767-F")
	
	# [HU2] Creación usuario asegurado
	c.crear_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES12345678")
	
	# [HU3] Administrar usuario: Modificación administrador
	c.modificar_admin("Carlos", "terceto@gmail.com", "75925767-F")
	
	# [HU3] Administrar usuario: Modificación cliente
	c.modificar_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES11223344")
	
	# [HU3] Administrar usuario: Eliminar usuario
	c.eliminar_usuario("75925767-F")
	
	# [HU4] Administrar póliza: Crear una póliza
	fecha = datetime.datetime(2020, 5, 17)
	c.crear_poliza("77925767-Z", fecha, TipoPoliza.Total, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
	
	# [HU4] Administrar póliza: Modificar una póliza
	fecha = datetime.datetime(2020, 5, 17)
	c.modificar_poliza("77925767-Z", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
	
	# [HU5] Consultar póliza
	poliza = c.consultar_poliza("77925767-Z")
	
	# [HU4] Administrar póliza: Desactivar una póliza
	c.desactivar_poliza("77925767-Z")
	
	# [HU8] Administrar autorización médica: Crear autorización
	fecha = datetime.datetime(2020, 5, 17)
	c.crear_autorizacion("77925767-Z", "PR-77925767-1", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Miguel", "Centro médico capital, Sala 2")
	
	# [HU8] Administrar autorización médica: Modificar autorización
	fecha = datetime.datetime(2020, 5, 17)
	c.modificar_autorizacion("AU-77925767-1", "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Fernando", "Centro médico capital, Sala 2")
	
	# [HU9] Consultar autorización médica
	autorizacion = c.consultar_autorizacion("AU-77925767-1")
	
	# [HU10] Aprobar/Denegar una autorización médica
	c.cambiar_estado_autorizacion("AU-77925767-1", False, "La póliza actual no cubre la intervención")
	
	# [HU11] Administrar cita médica: Crear cita médica
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	c.crear_cita("77925767-Z", "AU-77925767-1", "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	
	# [HU11] Administrar cita médica: Modificar cita médica
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	c.modificar_cita("AU-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	
	# [HU12] Consultar cita médica
	cita = c.consultar_cita("AU-77925767-1")

