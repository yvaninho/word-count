echo killing old proccesses 
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d 