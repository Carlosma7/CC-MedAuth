from invoke import task, run

@task 
def clean(c):
    print("Borrando caché de pytest")
    run ("rm -d -r .pytest_cache")
    run ("rm -d -r ./tests/.pytest_cache")
    run ("rm -d -r ./tests/__pycache__")

@task
def build(c):
    run ('pip3 install -r requirements.txt')
    print ('Instalación completada.')
