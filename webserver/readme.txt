## Running the webserver

### Build the docker container
docker build -t webserver .

### Run the docker container and expose the port for the web server
docker run -p 5000:5000 webserver
