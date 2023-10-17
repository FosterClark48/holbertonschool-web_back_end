# For the MySQL Advanced Project

# Builds the Docker image for the redis-basics project
build:
	docker build -t mysql-advanced .

# Runs the redis-basics image in a container
run:
	docker run -it --rm --name mysql-advanced-instance mysql-advanced

# Stop the running redis-basics container
stop:
	docker stop mysql-advanced-instance

# Remove all stopped containers
clean:
	docker container prune -f

# Remove all unused images, containers, networks, and volumes
nuke:
	docker system prune -af
