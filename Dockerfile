FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip3 install -r requirements.txt


ENV FLASK_APP=run.py
ENV YOURAPPLICATION_SETTINGS=config.py
RUN ["pytest", "-vv", "--junitxml=reports/result.xml"]

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
