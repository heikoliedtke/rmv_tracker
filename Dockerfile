FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx uwsgi-plugin-python3 && rm /etc/nginx/sites-enabled/default

COPY ./ ./app

WORKDIR ./app

RUN pip3 install -r requirements.txt



COPY ./myproject /etc/nginx/sites-enabled/

CMD service nginx start && uwsgi --ini app.ini



