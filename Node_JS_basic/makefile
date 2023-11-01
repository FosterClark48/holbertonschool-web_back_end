# For the NodeJS Basics Project

# Builds the Docker image for the redis-basics project
build:
	docker build -t nodejs .

# Runs the redis-basics image in a container
run:
	docker run -it --rm --name nodejs-instance nodejs

# Stop the running redis-basics container
stop:
	docker stop nodejs-instance

# Remove all stopped containers
clean:
	docker container prune -f

# Remove all unused images, containers, networks, and volumes
nuke:
	docker system prune -af
