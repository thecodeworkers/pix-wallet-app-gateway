FROM python:3.8-alpine
RUN mkdir /gateway
WORKDIR /gateway
COPY ./requirements.txt /gateway/
RUN apk add g++ linux-headers
RUN pip install -r requirements.txt
