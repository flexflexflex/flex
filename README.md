# Flex backend

## Installation
* Clone repo `git clone https://github.com/flexflexflex/flex.git`
* Create venv and nstall requirements `pip install -r requirements.txt`
* Run app `python manage.py runserver`

## API docs

### Auth
Here is all api endpoints documentation.
##
**POST /api/v1/auth/code/** 

Request:
```json
{
 "phone": "998909999999"
}
```
Response:

```json
{
 "result": "ok"
} 
```

##
**POST /api/v1/auth/token/** 

Request:
```json
{
 "phone": "998909999999",
 "code": "0000"
}
```
Response:

```json
{
 "new_user": false,
 "token": "tokentokentoken"
} 
```