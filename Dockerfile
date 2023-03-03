FROM python:3.8.10

WORKDIR /app

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip3 install \
  category-encoders==2.1.0 \
  flask_restx==0.3.0 


ENV FLASK_APP=app.py
ENV YOURAPPLICATION_SETTINGS=config.py

CMD exec gunicorn --bind :8080--workers 1 --timeout 900 app:app
