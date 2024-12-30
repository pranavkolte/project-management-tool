# Project Management Tool


## Project Structure
```
├── __init__.py
├── manage.py
├── pm_tool
│   ├── __init__.py         
│   ├── asgi.py             
│   ├── settings.py          # project settings, installed apps
│   ├── urls.py              # URL patterns for projects
│   └── wsgi.py              
├── projects
│   ├── __init__.py        
│   ├── admin.py            
│   ├── apps.py              
│   ├── migrations
│   │   ├──                  # Contains database migration files for projects
│   ├── models.py            # database models for app
│   ├── serializers.py       # Serializes and deserializes 
│   ├── tests.py             
│   ├── urls.py              # URL patterns the projects app
│   └── views.py             # logic for handling API requests for projects
├── tasks
│   ├── __init__.py          
│   ├── admin.py            
│   ├── apps.py             
│   ├── migrations
│   │   ├──                  # Contains database migration files
│   ├── models.py            # database models for tasks and comments
│   ├── serializers.py       # Serializes and deserializes for task and comment
│   ├── tests.py         
│   ├── urls.py              # URL patterns for the tasks app
│   └── views.py             # logic for handling task and comment API requests
└── users
    ├── __init__.py          
    ├── admin.py             
    ├── apps.py             
    ├── auth.py              # Custom authentication logic
    ├── migrations
    │   ├──                  # Contains database migration files for users
    ├── models.py            # Defines the database models for users
    ├── serializers.py       # Serializes and deserializes for user 
    ├── tests.py             
    ├── urls.py              # URL patterns for users app
    └── views.py             # logic for handling user API requests
```

## Local setup

**setup database with docker - run `docker-compose.yml`**
```shell
docker-compose up -d
```

**setup virtual environment**
```shell
python -m venv .venv
source .venv/bin/activate # Linux
.venv\Scripts\activate    # Windows
```

**Install Dependencies**
```shell
pip install -r requirements.txt
```

**Runserver**
```shell
cd pm_tool
python manage.py runserver
```

**Import Collection and Environment in Postman**
- Use [pm-tool-django.postman_collection.json](./pm-tool-django.postman_collection.json) to import the Postman collection.
- Use [pm-tool-env.postman_environment.json](./pm-tool-env.postman_environment.json) to import the Postman environment.

**This Postman collection have Documentation**
