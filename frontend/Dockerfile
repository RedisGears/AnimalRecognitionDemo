FROM node:latest

WORKDIR /usr/src/app

COPY package*.json ./
COPY . .

RUN npm install -g npm@8.10.0 && npm install

EXPOSE 3000
CMD [ "node", "server.js" ]
