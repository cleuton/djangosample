from python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD recados /usr/src/app/
RUN cp recados/production/settings.py recados/

EXPOSE 8000

# Não use em producao: CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker docker build -t cleutonrecados:0.0.1 .
# docker rm -f app
# docker run --name app -p 8000:8000 --link some-postgres:some-postgres -e DATABASE_URL="some-postgres" -d cleutonrecados:0.0.1

CMD ["gunicorn", "recados.wsgi", "--workers", "3", "--bind", "0.0.0.0:8000"]