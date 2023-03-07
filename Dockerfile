FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip3 install -r requirements.txt
  #flask==2.0.2\
  #category-encoders==2.1.0 \
  #gunicorn==20.1.0\
  #werkzeug==2.0.3\
  #flask_restx==0.5.1\
  #pytest==3.7

ENV FLASK_APP=run.py
ENV YOURAPPLICATION_SETTINGS=config.py
RUN ["pytest", "-vv", "--junitxml=reports/result.xml"]

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
