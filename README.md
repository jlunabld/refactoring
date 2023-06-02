# refactoringProject

# Build the Docker image
docker build -t botest_image -f Dockerfile .

# Run the Docker Container
docker run --rm --name BOTtest_container -p 8000:8000 botest_image

# Remove the Docker image
docker rmi botest_image

# Free up disk space
docker system prune --force
