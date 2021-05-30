# Golden Financing Exercise

A simple loan calculator

## Installation

Clone the repository on your local machine

Prerequisites:
- Docker
- docker-compose


## Usage

On project root directory:

```bash
docker-compose build
docker-compose up
```

Point browser to ***0.0.0.0:8000/ui/dashboard***

## Admin Access
***0.0.0.0:8000/admin***

>Django admin can be accessed, username and password to be provided on separate channel

## Email Functionality
***To use the email function, edit .env file and fill in the email credentials(Make sure allow insecure apps is enabled on the account) before docker-compose build***
```
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

## Notes

For API Documentation, please refer to the swagger file at the root of the repository.
