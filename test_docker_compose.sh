# Lanzar docker-compose
docker-compose up -d

# Espera de 3 segundos
sleep 3

# Petición curl POST para crear un usuario
curl --location --request POST 'http://0.0.0.0:2020/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
    "usuario": {
        "nombre": "Carlos",
        "email":"carlos7ma@gmail.com",
        "dni":"75925768-F",
        "cuenta_bancaria":"ES1234111892738495273840"
    },
    "tipo": 1
}'

# Espera de 3 segundos
sleep 3
echo -e '\n'

# Petición curl GET para obtener el usuario creado
curl --location --request GET 'http://0.0.0.0:2020/usuarios/75925768-F'

# Espera de 3 segundos
sleep 3
echo -e '\n'

# Petición curl DELETE para eliminar el usuario creado
curl --location --request DELETE 'http://0.0.0.0:2020/usuarios/75925768-F'

# Espera de 3 segundos
sleep 3
echo -e '\n'

# Petición curl GET para comprobar el usuario eliminado
curl --location --request GET 'http://0.0.0.0:2020/usuarios/75925768-F'
