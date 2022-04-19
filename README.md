# Django demo application
**Cleuton Sampaio**

This application is a tutorial on creating Django web apps. There's a PDF (in Portuguese) explaining all the steps. I will create an english version soon. 

This is the video tutorial for the application: https://youtu.be/8NpG4B0567c (Portuguese / Português).

## Install the application

Create a virtual environment: 
```
cd meu-tutorial
python -m venv .
source bin/activate
```

Install dependencies: 
```
pip install -r requirements.txt
```

The application uses a PostgreSQL database. You can change this by modifying "settings.py", for example, if you want to use SQLite: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

If you want to run a PostgreSQL database, just run the **docker** command: 
```
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```

Then, open an SSH session to the container: 
```
docker exec -it some-postgres /bin/bash
```

And run **psql**: 
```
psql -U postgres
```

Then create the database: 
```
create database recadosdb;
```

And exit: 
```
\q
```

After setting up the database, just run the migrations: 
```
python manage.py migrate
```

## Run the application

To run the application using Test server: 
```
python manage.py runserver
```

To run the E2E tests: 
```
python manage.py test
```

## Docker

There is a **Dockerfile** and you can build an image with this command: 
```
docker build -t <image name>:<image version> .
docker build -t test:0.0.1 .
```

Assuming you have a PostgreSQL container named "some-postgres": 
```
docker run --name app -p 8000:8000 --link some-postgres:some-postgres -e DATABASE_URL="some-postgres" -d test:0.0.1
```




