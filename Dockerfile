# Start from official image
FROM python:3.8.5-alpine

RUN mkdir /opt/urlshortener_service
RUN mkdir /opt/urlshortener_service/logs/

WORKDIR /opt/urlshortener_service

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY conf/requirements.txt /opt/urlshortener_service/
# RUN pip install --upgrade pip'
RUN pip install -r requirements.txt

COPY . /opt/urlshortener_service/

ENTRYPOINT ["sh", "conf/entrypoint.sh"]
