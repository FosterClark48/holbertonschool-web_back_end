# For the NoSQL Project

# Builds the Docker image for the redis-basics project
build:
	docker build -t nosql .

# Runs the redis-basics image in a container
run:
	docker run -it --rm --name nosql-instance nosql

# Stop the running redis-basics container
stop:
	docker stop nosql-instance

# Remove all stopped containers
clean:
	docker container prune -f

# Remove all unused images, containers, networks, and volumes
nuke:
	docker system prune -af
