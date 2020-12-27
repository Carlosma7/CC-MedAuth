from invoke import task, run

# Tarea de limpieza de ficheros
@task 
def clean(c):
	print("Borrando caché de python.")
	run("find . -maxdepth 5 -type d -name __pycache__ -name  .pytest_cache  -exec rm -r {} +")

# Tarea de ejecución de tests
@task
def test(c):
	print("Ejecución de test.\n")
	run("pytest -v --disable-pytest-warnings src/test/*")

# Tarea de ejecución del modelo
@task
def execute(c):
	print("Ejecución del modelo\n")
	run("python3 ./src/core/main.py")
	print("Fin de la ejecución.")

