FROM python:3.8-alpine

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
RUN apk add g++ linux-headers
RUN pip install -r requirements.txt
