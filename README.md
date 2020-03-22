# COVID API
A web API server to get updated data about COVID in Italy. *EASY AND FAST*.

For *Development* purpose only.

The data are updated at startup time and each day at midnight (Italy time zone), by default, using a scheduled process.

**KEYWORDS: Flask, Connexion, Swagger, OAS3, MongoDB**

## Fast Setup

### Install using Docker Compose.

Run the server.
```bash
> cd covid-api
> docker-compose up
```
Run the server and rebuild the image (useful after changes on the code).
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
The server run on **http://localhost:5000** by default.

The API documentation is visible using **http://localhost:5000/api/v1/ui**.

Data are stored in a *MongoDB* database and it is possible to view the content through *MongoExpress* using **http://localhost:i8081**.

The parameters are stored in the *.env* file in the root of the project: 
```
# MONGODB
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=root
MONGO_INITDB_HOST=0.0.0.0
MONGO_INITDB_PORT=27017
MONGO_INITDB_DATABASE=covid 
MONGO_INITDB_DROP_AT_STARTUP=0 # Whether or not to drop the database at init time.

# MONGOEXPRESS
MONGO_EXPRESS_PORT=8081

# FLASK
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
FLASK_ENV=development

# SCHEDULER
UPDATE_AUTO=0 # Whether or not to start a process to update data each day at UPDATE_TIME. 
UPDATE_TIME=00:00 # The update time expressed as HH:MM based on Italy time zone.
```
ENJOY :rocket: :rocket:
