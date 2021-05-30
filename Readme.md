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
