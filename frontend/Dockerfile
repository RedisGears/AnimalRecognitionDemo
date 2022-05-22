FROM node:slim

WORKDIR /usr/src/app

COPY package*.json ./
COPY . .

RUN npm install 2>/dev/null

EXPOSE 3000
CMD [ "node", "server.js" ]
