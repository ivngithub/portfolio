FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.12.2 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3 psycopg2 flask-wtf flask-sqlalchemy flask-migrate
WORKDIR /microproject
COPY microproject /microproject
COPY cmd.sh /

USER uwsgi

CMD ["/cmd.sh"]