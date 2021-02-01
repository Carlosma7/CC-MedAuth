import sys
import requests
import os
import json


class ClienteAPI:
    def __init__(self):
        self.headers = {'content-type': 'application/json'}

        try:
        	# Try to get the Medauth API URI by environment variables
        	self.route = 'http://' + os.environ['MEDAUTH_HOSTNAME'] + ':' + os.environ['MEDAUTH_PORT']
        except:
        	# Default URI
        	self.route = 'http://0.0.0.0:2020'

	# Creación usuario administrativo
    def crear_usuario_admin(self, nombre, email, dni):

        r = requests.post(self.route + "/usuarios", data=json.dumps(
            {'usuario': {'nombre': nombre, 'email': email, 'dni': dni}, 'tipo': 0}), headers=self.headers)
            
        print(str(r.status_code) + ": " + r.text)

	# Creación usuario cliente
    def crear_usuario_cliente(self, nombre, email, dni, cuenta_bancaria):

        r = requests.post(self.route + "/usuarios", data=json.dumps(
            {'usuario': {'nombre': nombre, 'email': email, 'dni': dni, 'cuenta_bancaria': cuenta_bancaria}, 'tipo': 1}), headers=self.headers)
        
        print(str(r.status_code) + ": " + r.text)

	# Modificación de usuario
    def modificar_usuario(self, tipo, nombre, email, dni, cuenta_bancaria):
    	
        r = requests.post(self.route + "/usuarios/" + dni, data=json.dumps({'tipo': tipo, 'nombre': nombre, 'email': email, 'cuenta_bancaria': cuenta_bancaria}), headers=self.headers)
        
        print(str(r.status_code) + ": " + r.text)
    
    # Consulta de usuario
    def consultar_usuario(self, dni):
        r = requests.get(self.route + "/usuarios/" + dni)
        
        print(str(r.status_code) + ": " + r.text)
    
    # Eliminación de usuario
    def eliminar_usuario(self, dni):
        r = requests.delete(self.route + "/usuarios/" + dni)
        
        print(str(r.status_code) + ": " + r.text)
    
    # Creación de póliza
    def crear_poliza(self, dni, periodo_carencia, tipo_poliza, copagos, mensualidad, servicios_excluidos, modulos_extra):
    	r = requests.get(self.route + "/usuarios/" + dni)
    	if r.status_code == 400:
            print(str(r.status_code) + ": " + r.text)
    	else:
            modulos_extra = modulos_extra.strip('][').split(',')

            if modulos_extra == ['']:
                modulos_extra = []
                modulos_extra = [str(mod) for mod in modulos_extra]

            usuario = r.text
            
            r = requests.post(self.route + "/polizas", data=json.dumps({'titular': json.loads(usuario), 'id_poliza': '', 'periodo_carencia': periodo_carencia, 'tipo': json.dumps(tipo_poliza), 'copagos': copagos, 'mensualidad': mensualidad, 'servicios_excluidos': servicios_excluidos, 'modulos_extra': modulos_extra, 'activa': True}), headers=self.headers)
        
            print(str(r.status_code) + ": " + r.text)
    
    # Modificación de póliza
    def modificar_poliza(self, id_poliza, periodo_carencia, tipo_poliza, copagos, mensualidad, servicios_excluidos, modulos_extra):
        modulos_extra = modulos_extra.strip('][').split(',')

        if modulos_extra == ['']:
        	modulos_extra = []
        	modulos_extra = [str(mod) for mod in modulos_extra]
            
        r = requests.post(self.route + "/polizas/" + id_poliza, data=json.dumps({'peticion': 'modificar', 'periodo_carencia': periodo_carencia, 'tipo': json.dumps(tipo_poliza), 'copagos': copagos, 'mensualidad': mensualidad, 'servicios_excluidos': servicios_excluidos, 'modulos_extra': modulos_extra}), headers=self.headers)

        print(str(r.status_code) + ": " + r.text)
    
    # Consulta de póliza
    def consultar_poliza(self, dni):
        r = requests.get(self.route + "/polizas/" + dni)
        
        print(str(r.status_code) + ": " + r.text)

	# Desactivación de póliza
    def desactivar_poliza(self, dni):
        r = requests.post(self.route + "/polizas/" + dni, data = json.dumps({'peticion': 'desactivar'}))
        
        print(str(r.status_code) + ": " + r.text)

	# Subida de prescripción
    def subir_prescripcion(self, dni, id_poliza, fecha, especialidad, facultativo_prescriptor, facultativo_realizador, servicios_solicitados, consulta):
        r = requests.get(self.route + "/usuarios/" + dni)
        if r.status_code == 400:
            print(str(r.status_code) + ": " + r.text)
        else:
            
            usuario = r.text

            r = requests.post(self.route + "/prescripciones", data=json.dumps({'asegurado': json.loads(usuario), 'id_poliza': id_poliza, 'fecha_realizacion': fecha, 'especialidad': json.dumps(especialidad), 'facultativo_prescriptor': facultativo_prescriptor, 'facultativo_realizador': facultativo_realizador, 'servicios_solicitados': servicios_solicitados, 'consulta': consulta}), headers=self.headers)

            print(str(r.status_code) + ": " + r.text)

	# Solicitud de autorización
    def solicitar_autorizacion(self, id_prescripcion):
        r = requests.post(self.route + "/autorizaciones/" + id_prescripcion, data = json.dumps({'peticion': 'solicitar'}))
        
        print(str(r.status_code) + ": " + r.text)

	# Creación de autorización
    def crear_autorizacion(self, dni, id_poliza, estado, motivo_rechazo, fecha, especialidad, servicios_aceptados, facultativo, consulta):
        r = requests.get(self.route + "/usuarios/" + dni)
        if r.status_code == 400:
            print(str(r.status_code) + ": " + r.text)
        else:
            usuario = r.text
            
            estado = json.loads(estado.lower())

            r = requests.post(self.route + "/autorizaciones", data=json.dumps({'asegurado': json.loads(usuario), 'id_poliza': id_poliza, 'aceptada': estado, 'motivo_rechazo': motivo_rechazo, 'fecha_realizacion': fecha, 'especialidad': json.dumps(especialidad), 'servicios_aceptados': servicios_aceptados, 'facultativo_realizador': facultativo, 'consulta': consulta}), headers=self.headers)

            print(str(r.status_code) + ": " + r.text)

	# Modificación de autorización
    def modificar_autorizacion(self, id_autorizacion, motivo_rechazo, fecha, especialidad, servicios_aceptados, facultativo, consulta):
        r = requests.post(self.route + "/autorizaciones/" + id_autorizacion, data=json.dumps({'peticion': 'modificar', 'motivo_rechazo': motivo_rechazo, 'fecha_realizacion': fecha, 'especialidad': json.dumps(especialidad), 'servicios_aceptados': servicios_aceptados, 'facultativo_realizador': facultativo, 'consulta': consulta}), headers=self.headers)

        print(str(r.status_code) + ": " + r.text)

	# Consulta de autorización
    def consultar_autorizacion(self, id_autorizacion):
        r = requests.get(self.route + "/autorizaciones/" + id_autorizacion)
        
        print(str(r.status_code) + ": " + r.text)

	# Aprobación o denegación de autorización
    def aprobar_denegar_autorizacion(self, id_autorizacion, estado, motivo_rechazo):
        
        r = requests.post(self.route + "/autorizaciones/" + id_autorizacion, data=json.dumps({'peticion': 'aprobar', 'aceptada': estado, 'motivo_rechazo': motivo_rechazo}), headers=self.headers)

        print(str(r.status_code) + ": " + r.text)

	# Creación de cita
    def crear_cita(self, id_autorizacion, dni, id_prescripcion, fecha, hora, facultativo, consulta):
        r = requests.get(self.route + "/usuarios/" + dni)
        if r.status_code == 400:
            print(str(r.status_code) + ": " + r.text)
        else:
            usuario = r.text

            r = requests.post(self.route + "/citas", data=json.dumps({'asegurado': json.loads(usuario), 'id_autorizacion': id_autorizacion, 'id_prescripcion': id_prescripcion, 'fecha': fecha, 'hora': hora, 'facultativo_realizador': facultativo, 'consulta': consulta}), headers=self.headers)

            print(str(r.status_code) + ": " + r.text)

	# Modificación de cita
    def modificar_cita(self, id_autorizacion, fecha, hora, facultativo, consulta):
        r = requests.post(self.route + "/citas/" + id_autorizacion, data=json.dumps({'fecha': fecha, 'hora': hora, 'facultativo_realizador': facultativo, 'consulta': consulta}), headers=self.headers)

        print(str(r.status_code) + ": " + r.text)
    
    # Consulta de cita
    def consultar_cita(self, id_autorizacion):
        r = requests.get(self.route + "/citas/" + id_autorizacion)
        
        print(str(r.status_code) + ": " + r.text)
        

if __name__ == '__main__':
    cliente = ClienteAPI()

    if len(sys.argv) < 2:
        print("Error: Número de argumentos inválido, las opciones son: \n")
        print("1. Crear usuario administrativo.")
        print("2. Crear usuario cliente.")
        print("3. Modificar usuario.")
        print("4. Consultar usuario.")
        print("5. Eliminar usuario.")
        print("6. Crear póliza.")
        print("7. Modificar póliza.")
        print("8. Consultar póliza.")
        print("9. Desactivar póliza.")
        print("10. Subir prescripción.")
        print("11. Solicitar autorización.")
        print("12. Crear autorización.")
        print("13. Modificar autorización.")
        print("14. Consultar autorización.")
        print("15. Aprobar/Denegar autorización.")
        print("16. Crear cita.")
        print("17. Modificar cita.")
        print("18. Consultar cita.")
    else:
        option = int(sys.argv[1])
        
        if option == 1:
            if len(sys.argv) == 5:
                cliente.crear_usuario_admin(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                print("1. Crear usuario administrativo: \tpython3 client.py 1 <nombre> <email> <dni>")
        elif option == 2:
            if len(sys.argv) == 6:
                cliente.crear_usuario_cliente(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
            else:
                print("2. Crear usuario cliente: \t\tpython3 client.py 2 <nombre> <email> <dni> <cuenta bancaria>")
        elif option == 3:
            if len(sys.argv) == 6:
                cliente.modificar_usuario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], "")
            elif len(sys.argv) == 7:
                cliente.modificar_usuario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            else:
                print("3. Modificar usuario: \t\t\tpython3 client.py 3 <tipo (admin:0 cliente:1)> <nombre> <email> <dni> <cuenta bancaria (cliente)>")
        elif option == 4:
            if len(sys.argv) == 3:
                cliente.consultar_usuario(sys.argv[2])
            else:
                print("4. Consultar usuario: \t\t\tpython3 client.py 4 <dni>")
        elif option == 5:
            if len(sys.argv) == 3:
                cliente.eliminar_usuario(sys.argv[2])
            else:
                print("5. Eliminar usuario: \t\t\tpython3 client.py 5 <dni>")
        elif option == 6:
            if len(sys.argv) == 9:
                cliente.crear_poliza(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
            else:
                print("6. Crear póliza: \t\t\tpython3 client.py 6 <dni> <periodo carencia> <tipo poliza> <copagos> <mensualidad> <servicios excluidos [lista]> <modulos extra [lista]>")
        elif option == 7:
            if len(sys.argv) == 9:
                cliente.modificar_poliza(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
            else:
                print("7. Modificar póliza: \t\t\tpython3 client.py 7 <id poliza> <periodo carencia> <tipo poliza> <copagos> <mensualidad> <servicios excluidos [lista]> <modulos extra [lista]>")
        elif option == 8:
            if len(sys.argv) == 3:
                cliente.consultar_poliza(sys.argv[2])
            else:
                print("8. Consultar póliza: \t\t\tpython3 client.py 8 <dni>")
        elif option == 9:
            if len(sys.argv) == 3:
                cliente.desactivar_poliza(sys.argv[2])
            else:
                print("9. Desactivar póliza: \t\t\tpython3 client.py 9 <dni>")
        elif option == 10:
            if len(sys.argv) == 10:
                cliente.subir_prescripcion(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
            else:
                print("10. Subir prescripción: \t\tpython3 client.py 10 <dni> <id poliza> <fecha> <especialidad> <facultativo prescriptor> <facultativo realizador> <servicios solicitados [lista]> <consulta>")
        elif option == 11:
            if len(sys.argv) == 3:
                cliente.solicitar_autorizacion(sys.argv[2])
            else:
                print("11. Solicitar autorización: \t\tpython3 client.py 11 <id prescripcion>")
        elif option == 12:
            if len(sys.argv) in [10,11]:
                if len(sys.argv) == 10:
                    cliente.crear_autorizacion(sys.argv[2], sys.argv[3], sys.argv[4], "", sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
                elif len(sys.argv) == 11:
                    cliente.crear_autorizacion(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])
            else:
                print("12. Crear autorización: \t\tpython3 client.py 12 <dni> <id poliza> <estado> <motivo rechazo (si hay)> <fecha> <especialidad> <servicios solicitados [lista]> <facultativo> <consulta>")
        elif option == 13:
            if len(sys.argv) in [8,9]:
                if len(sys.argv) == 8:
                    cliente.modificar_autorizacion(sys.argv[2], "", sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
                elif len(sys.argv) == 9:
                    cliente.modificar_autorizacion(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
            else:
                print("13. Modificar autorización: \t\tpython3 client.py 13 <id autorizacion> <motivo rechazo (si hay)> <fecha> <especialidad> <servicios aceptados [lista]> <facultativo> <consulta>")
        elif option == 14:
            if len(sys.argv) == 3:
                cliente.consultar_autorizacion(sys.argv[2])
            else:
                print("14. Consultar autorización: \t\tpython3 client.py 14 <id autorizacion>")
        elif option == 15:
            if len(sys.argv) in [4,5]:
                if len(sys.argv) == 4:
                    cliente.aprobar_denegar_autorizacion(sys.argv[2], sys.argv[3], "")
                elif len(sys.argv) == 5:
                    cliente.aprobar_denegar_autorizacion(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                print("15. Aprobar/Denegar autorización: \tpython3 client.py 15 <id autorizacion> <estado> <motivo_rechazo (si hay)>")
        elif option == 16:
            if len(sys.argv) in [8,9]:
                if len(sys.argv) == 8:
                    cliente.crear_cita(sys.argv[2], sys.argv[3], "", sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
                elif len(sys.argv) == 9:
                    cliente.crear_cita(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
            else:
                print("16. Crear cita: \t\t\tpython3 client.py 16 <id autorizacion> <dni> <id prescripcion (si hay)> <fecha> <hora> <facultativo> <consulta>")
        elif option == 17:
            if len(sys.argv) == 7:
                cliente.modificar_cita(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            else:
                print("17. Modificar cita: \t\t\tpython3 client.py 17 <id autorizacion> <fecha> <hora> <facultativo> <consulta>")
        elif option == 18:
            if len(sys.argv) == 3:
                cliente.consultar_cita(sys.argv[2])
            else:
                print("18. Consultar cita: \t\t\tpython3 client.py 18 <id autorizacion>")
        
