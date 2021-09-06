FROM node:lts-alpine

RUN npm install --quiet --global vue-cli@2.9.3

RUN mkdir /frontend
WORKDIR /frontend

FROM python:3.8
ADD . /server/hms
WORKDIR /server/hms
RUN pip install -r requirements.txt