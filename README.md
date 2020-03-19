# COVID API
A web API server to get updated data about COVID in Italy. *EASY AND FAST*.

For *Development* purpose only.

The data are updated at startup time and each day at midnight(Italy) using a scheduled process.

**KEYWORDS: Flask, Connexion, Swagger, OAS3.**

## Install the library
### Install as python package
Install dependencies:
```bash
> cd covid-api
> pip install -r requirements.txt
```
Run the server:
```bash
> python app.py
```

## Fast Setup
### Install using Docker Compose. 

Run the server.
```bash
> cd covid-api
> docker-compose up
```
Run the server and rebuild the image.
```bash
> cd covid-api
> docker-compose up --build
```

## (Optional) Build the Docker Image
```bash
> cd covid-api
> docker build -t covid-web-server:latest .
```

## Usage
The server run on **http://localhost:5000**.

The API documentation is visible using **http://localhost:5000/api/v1/ui**.

To change some network params (docker-compose.yaml): 
```
environment:
      - FLASK_RUN_HOST=0.0.0.0 # hostname
      - FLASK_RUN_PORT=5000 # port
      - FLASK_ENV=development # environemnt "development" or "production"
```
And rememeber to change the port mapping.
```
ports:
      - "5000:5000"
```
ENJOY :rocket: :rocket:
