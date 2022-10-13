FROM python:3.8.3

# set work directory
RUN mkdir -p /opt/restapi/src
WORKDIR /opt/restapi/src
COPY . /opt/restapi/src

# set environment variables
ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg2 dependencies
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input 
# RUN python manage.py makemigrations app 
# RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "-c", "/opt/restapi/config/gunicorn/conf.py", "--bind", ":8000","--chdir", "app", "conf.wsgi:application"]


