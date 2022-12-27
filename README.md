# Introduction
This project is a Django backend app. In this app a users messaging app is implemented.

**Tools** -

- DRF
- Postgress SQL
- DRF simple JWT token
- Django filters

# Setup & Installation

1. Clone the repo using either HTTPS or SSH. If using SSH make sure to configre your public key in GitHub.

    * HTTPS
    ``` sh
    git clone https://github.com/nadav152/messages-app.git
    ```
    * SSH
   ``` sh
   git clone git@github.com:nadav152/messages-app.git
   ```

2. Make sure you have docker & docker-compose installed. 
   If you are running on Mac M1 use - `export DOCKER_DEFAULT_PLATFORM=linux/amd64` for building the project on M1 architecture.
   ``` sh
   sudo docker-compose up
   ```
   This will build a docker image of the Django, pull a postgress DB image and setup an Nginx webserver infront of the Django app.

