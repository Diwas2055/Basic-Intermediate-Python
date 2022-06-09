FROM node:17-alpine

WORKDIR /app

COPY ./api .

RUN npm install

EXPOSE 4000

CMD [ "node", "app.js" ]