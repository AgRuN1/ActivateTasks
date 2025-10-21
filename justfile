# build docker compose
build:
    docker-compose -f docker-compose.yml -p activatetasks up -d --build
#test sync plug
test-sync:
    docker exec -it sync pytest -s --cov
#test async api
test-async:
    docker exec -it async pytest -s --cov