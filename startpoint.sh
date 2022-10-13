# docker rm $(docker ps -a -q) -f && docker volume rm $(docker volume ls -q)
docker-compose build
docker-compose up -d

docker-compose exec restapi python manage.py makemigrations app
docker-compose exec restapi python manage.py migrate app
docker-compose exec restapi python manage.py test app