FROM nginx:stable-alpine

USER root

RUN apk add --update openssl bash

COPY ./utility/nginx/default.conf.template /etc/nginx/default.conf.template
COPY ./utility/nginx/default-ssl.conf.template /etc/nginx/default-ssl.conf.template
COPY ./utility/nginx/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]