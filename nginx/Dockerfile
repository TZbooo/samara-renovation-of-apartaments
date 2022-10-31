FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /data/nginx/cache/
COPY nginx.conf cache.conf /etc/nginx/conf.d/
COPY certs/ /etc/ssl/