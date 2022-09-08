FROM lawyer_python AS python

FROM nginx:1.21-alpine

RUN rm -rf /etc/nginx/conf.d
COPY deploy/nginx/host.conf /etc/nginx/conf.d/default.conf
COPY --from=python /app/src/static /app/static
