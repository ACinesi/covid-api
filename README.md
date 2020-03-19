# COVID API
A web API server to get updated data about COVID in Italy. *EASY AND FAST*.
For *Development* purpose only.

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
*Pulls the latest image on Docker Hub acinesi/covid-web-server:latest.*

Run the server.
```bash
> cd covid-api
> docker-compose up
```

## (Optional) Build the Docker Image
```bash
> cd covid-api
> docker build -t covid-web-server:latest .
```

## Usage
The server run on **localhost:5000**.
The API documentation is visible using **http://localhost:5000/api/v1/ui**.

ENJOY :rocket: :rocket:
