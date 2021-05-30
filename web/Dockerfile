FROM node:14.17.0-alpine
WORKDIR /app/web
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . /app/web/

CMD npm run serve
