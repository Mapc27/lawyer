FROM node:16-alpine as vue

WORKDIR /app

COPY src/web/static/vue/package*.json ./

RUN npm install

COPY src/web/static/vue .

RUN npm run build

FROM lawyer-python:latest AS app

FROM nginx:1.21-alpine

RUN rm -rf /etc/nginx/conf.d
COPY deploy/nginx/host.conf /etc/nginx/conf.d/default.conf

COPY --from=app app/src/web/static /app/static

RUN mkdir /app/static/dist

COPY --from=vue /app/dist /app/static/dist
