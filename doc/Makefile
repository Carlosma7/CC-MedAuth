# Tarea de ejecución del modelo
execute:
	@echo "Ejecución del modelo\n"
	python3 ./src/main.py
	@echo "\nFin de la ejecución."

# Tarea de ejecución de tests
test:
	@echo "Ejecución de test.\n"
	@echo "Test Clase UsuarioAdmin:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testUsuarioAdmin.py
	
	@echo "\nTest Clase UsuarioCliente:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testUsuarioCliente.py
	
	@echo "\nTest Clase Poliza:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testPoliza.py
	
	@echo "\nTest Clase Prescripcion:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testPrescripcion.py
	
	@echo "\nTest Clase Autorizacion:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testAutorizacion.py
	
	@echo "\nTest Clase Cita:"
	pytest -v --disable-pytest-warnings ./src/test/modelos/testCita.py
	
	@echo "\nTest Clase Controlador:"
	pytest -v --disable-pytest-warnings ./src/test/testControlador.py

# Tarea de limpieza de ficheros
clean:
	@echo 'Borrando caché de python.'
	find . -maxdepth 5 -type d -name __pycache__ -exec rm -r {} +
	@echo 'Borrando caché de pytest.'
	find . -maxdepth 5 -type d -name .pytest_cache -exec rm -r {} +
