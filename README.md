# Flex backend

## Installation
* Clone repo `git clone https://github.com/flexflexflex/flex.git`
* Create venv and nstall requirements `pip install -r requirements.txt`
* Run app `python manage.py runserver`

## API docs

## Auth
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
##

**GET /api/v1/auth/user/**

Response:
```json
{
    "first_name": "Хуй",
    "last_name": "Сасатб",
    "username": "xyarim",
    "bio": "huy",
    "phone": "998909999999"
}
```

##
## Flex

**GET /api/v1/flex/** 

Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "owner": {
                "first_name": "Арслан",
                "last_name": "Тажибаев",
                "username": "xyarim",
                "bio": "huy",
                "phone": "998909999999"
            },
            "members_count": 1,
            "friends_count": 0,
            "description": "123123123123"
        }
    ]
}
```



