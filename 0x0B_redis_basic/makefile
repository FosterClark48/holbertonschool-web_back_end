# For the Redis Basics Project

# Builds the Docker image for the redis-basics project
build:
	docker build -t redis-basics .

# Runs the redis-basics image in a container
run:
	docker run -it --rm --name redis-basics-instance redis-basics

# Stop the running redis-basics container
stop:
	docker stop redis-basics-instance

# Remove all stopped containers
clean:
	docker container prune -f

# Remove all unused images, containers, networks, and volumes
nuke:
	docker system prune -af
