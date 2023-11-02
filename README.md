# MenuMaster

## Data:
https://www.dropbox.com/scl/fo/xwa4jfceilh0x6offhqgy/h?rlkey=6biy1h6eeblizmlgmqsok79un&dl=0

## ElasticSearch with Docker Help:
https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose
* Potential Memory Issue Fixes:
  * MacOS: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#_macos_with_docker_for_mac
  * Windows (With WSL 2 Docker Configuration): https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#_windows_with_docker_desktop_wsl_2_backend 

# Up-To-Date Instructions

## ElasticSearch, Frontend, & Backend
### To Initialize:
* Ensure Docker is installed on your machine
  * It is helpful to have Docker Desktop running while executing to see how the script updates
* Adjust the `.env` file as necessary

## Create a Docker Image - Frontend
* Enter the `\frontend` directory
* Run `docker build -t angular-image .`
  * This will create an image to use in the docker compose script later
    
## Create a Docker Image - Backend
* Enter the `\backend` directory
* Run `docker build -t flask-image .`
  * This will create an image to use in the docker compose script later

## Run the Docker Compose
* Enter the root directory (`\MenuMaster`)
* Run the command: `docker-compose up`
    * This will create 5 containers
      1) `setup-1` - A Setup ElasticSearch instance (NOTE: This is purely for setup and should exit after completion of setup)
      2) `es01-1` - An ElasticSearch instance
      3) `kibana-1` - A Kibana instance
      4) `flask-backend-1` - Our Flask instance
      5) `angular-frontend-1` - Our Angular instance
     
## Import the Data
* After the Docker compose script is finished, we now want to setup the index and import the data
  * Ensure python is installed on your machine
    * You might also need several python packages
     * Run `pip install -r requirements.txt`
  * Now, run `python import_data_script.py`
    * This will create an index in your ElasticSearch instance and propagate the data into it
    * Total documents should be ~5,860 (This takes some time to fully import)

## To Run Again
* I prefer using the Docker Desktop
  * From the `Containers` section, select `es01-1`, `kibana-1`, `flask-backend-1`, and `angular-frontend-1` from within the `capstone` compose
  * Press the start button (looks like a play button) and the project will start all apps
* However, I believe there is a way to restart the docker compose by running the following command:
  * `docker compose start capstone`
  * Where `capstone` is the name of our compose

___

# Deprecated Instructions

## ElasticSearch
### To Initialize:
* Ensure Docker is installed on your machine
  * It is helpful to have Docker Desktop running while executing to see how the script updates
* Enter the `ElasticSearch` directory
* Adjust the `.env` file as necessary
* Run the command: `docker compose up`
    * This will create three containers
      1) `setup-1` - A Setup ElasticSearch instance (NOTE: This is purely for setup and should exit after completion of setup)
      2) `es01-1` - An ElasticSearch instance
      3) `kibana-1` - A Kibana instance
* After the Docker compose script is finished, we now want to setup the index and import the data
  * Ensure python is installed on your machine
    * You will also need several python packages
    * Run `pip install <package1> <package2> <package etc.>` with the following packages
      * `elasticsearch`
      * `python-dotenv`
  * Now, run `python import_data_script.py`
    * This will create an index in your ElasticSearch instance and propagate the data into it
    * Total documents should be ~5,860 (This takes some time to fully import)

### To Run Again
* I prefer using the Docker Desktop
  * From the `Containers` section, select `es01-1` and `kibana-1`
  * Press the start button (looks like a play button) and ElasticSearch will start again
* However, I believe there is a way to restart the docker compose by running the following command:
  * `docker compose start capstone-elasticsearch`
  * Where `capstone-elasticsearch` is the name of our compose

## Backend
### To Run:
* Ensure python is installed on your machine
  * You will also need several python packages
  * Run `pip install <package1> <package2> <package etc.>` with the following packages
    * `flask`
* Adjust the `.env` file as necessary
* Enter the `backend` directory
* Run `flask --app app run`
