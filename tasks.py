from invoke import task, run

# Tarea de limpieza de ficheros
@task 
def clean(c):
	print("Borrando caché de python.")
	run("find . -maxdepth 5 -type d -name __pycache__ -exec rm -r {} +")
	print("Borrando caché de pytest.")
	run("find . -maxdepth 5 -type d -name .pytest_cache -exec rm -r {} +")

# Tarea de ejecución de tests
@task
def tests(c):
	print("Ejecución de test.\n")
	print("Test Clase Usuario:")
	run("pytest -v --disable-pytest-warnings ./src/test/testUsuario.py")
	
	print("Test Clase UsuarioAdmin:")
	run("pytest -v --disable-pytest-warnings ./src/test/testUsuarioAdmin.py")
	
	print("\nTest Clase UsuarioCliente:")
	run("pytest -v --disable-pytest-warnings ./src/test/testUsuarioCliente.py")
	
	print("\nTest Clase Poliza:")
	run("pytest -v --disable-pytest-warnings ./src/test/testPoliza.py")
	
	print("\nTest Clase Prescripcion:")
	run("pytest -v --disable-pytest-warnings ./src/test/testPrescripcion.py")
	
	print("\nTest Clase Autorizacion:")
	run("pytest -v --disable-pytest-warnings ./src/test/testAutorizacion.py")
	
	print("\nTest Clase Cita:")
	run("pytest -v --disable-pytest-warnings ./src/test/testCita.py")
	
	print("\nTest Clase Controlador:")
	run("pytest -v --disable-pytest-warnings ./src/test/testControlador.py")

# Tarea de ejecución del modelo
@task
def execute(c):
	print("Ejecución del modelo\n")
	run("python3 ./src/main.py")
	print("Fin de la ejecución.")

