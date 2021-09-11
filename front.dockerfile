FROM node:9.5

RUN npm install -g @vue/cli

RUN mkdir /app
WORKDIR /app