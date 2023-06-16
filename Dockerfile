FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1
ENV FLASK_APP = main.py
ENV FLASK_ENV = development

RUN python3 --version
RUN pip3 --version

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get install openssl

EXPOSE 80
CMD [ "gunicorn", "-b", "0.0.0.0:80", "--timeout", "90", "main:app" ]