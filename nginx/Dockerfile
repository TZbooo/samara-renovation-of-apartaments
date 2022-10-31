FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/lib/nginx/cache/
COPY *.conf /etc/nginx/conf.d
COPY certs/ /etc/ssl/