from invoke import task, run

# Tarea de limpieza de ficheros
@task 
def clean(c):
	print("Borrando caché de python.")
	run("find . -maxdepth 5 -type d -name  .pytest_cache -exec rm -r {} +")
	run("find . -maxdepth 5 -type d -name __pycache__ -exec rm -r {} +")

# Tarea de ejecución de tests
@task
def test(c):
	print("Ejecución de test.\n")
	run("pytest -v --disable-pytest-warnings src/test/*")
	run("pytest -v --disable-pytest-warnings src/test/testControlador/*")

# Tarea de ejecución de tests con BD
@task
def testBD(c):
	print("Ejecución de test.\n")
	run("pytest -v --disable-pytest-warnings src/test/*")
	run("pytest -v --disable-pytest-warnings src/test/testBD/*")
	
# Tarea de ejecución de tests del Controlador
@task
def testControlador(c):
	print("Ejecución de test.\n")
	run("pytest -v --disable-pytest-warnings src/test/testControlador/*")

# Tarea de ejecución del modelo
@task
def execute(c):
	print("Ejecución de MedAuth\n")
	run("hypercorn src/core/main.py --bind '0.0.0.0:2020'")

# Tarea build, en nuestro caso no hace nada
@task
def build(c):
	print("Build realizado\n")

# Tarea install, en nuestro caso no hace nada
@task
def install(c):
	print("Instalación completada\n")
