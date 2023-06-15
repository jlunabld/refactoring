# refactoringProject

# Build the Docker image
docker build -t botest_image -f Dockerfile .

# Run the Docker Container
docker run --rm --name botest_container -p 8000:8000 botest_image
# Dash app will be available at http://127.0.0.1:8000

# Remove the Docker image
docker rmi botest_image

# Free up disk space
docker system prune --force
