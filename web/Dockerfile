FROM node:lts-alpine
WORKDIR /app/web
RUN npm install -g @vue/cli
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . /app/web/

CMD npm run serve
