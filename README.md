# HTML Website deployed with Docker and Nginx Steps:
1. Clone this repository in your machine
2. Git pull
3. Make changes to the index html to see how Docker containers and images work
4. Stop the container using port 8080->80/tcp
5. Build the container: docker build -t docker_nginx_personal_website .
6. Run the image: docker run -d -p 8080:80  docker_nginx_personal_website