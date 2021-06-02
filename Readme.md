# Golden Financing Exercise

A simple loan calculator

## Installation

Clone the repository on your local machine

Prerequisites:
- Docker
- docker-compose


## Usage

On project root directory:

Set up an .env file - /app/.env (besides manage.py) with the following contents:

```
HOST=0.0.0.0
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Since this is just for development, this is okay, but for production setup, env file should be encrypted and not be part of this documentation/repository. Docker will look for this file so this is important. After creating the file, proceed with:

```bash
docker-compose build
docker-compose up
```

Point browser to ***0.0.0.0:8000/ui/dashboard***

## Admin Access
***0.0.0.0:8000/admin***

>Django admin can be accessed, username and password to be provided on separate channel

## Email Functionality
***To use the email function, edit /app/.env(same directory as manage.py file) file and fill in the email credentials(Make sure allow insecure apps is enabled on the account) before docker-compose build***
```
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## Notes

For API Documentation, please refer to the swagger file at the root of the repository.

## Running without docker

1. Create a virtualenv with python3
```
python3 -m venv goldenfin
```

2. Clone this repository, folder structure should be like below

goldenfin
--bin(venv files)
--app(this app repo)
---app
----app(final folder containing settings.py)

3. Activate Vend and Install libraries
```
source ./bin/activate
cd app/app
pip install -r requirements.txt
```

4. Run Django Development Server
```
python manage.py runserver 127.0.0.1:8080
```

5. To use the email function, edit non-docker-env and fill up the email details then export the env vars 
```
source non-docker-env
```
