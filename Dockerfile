FROM python:3.8-alpine as builder

WORKDIR /app/
COPY . .
RUN apk update \
    && apk add musl-dev linux-headers gcc libffi-dev nginx \
    && mv default.conf /etc/nginx/http.d/default.conf

RUN sed -i '2i daemon off;' /etc/nginx/nginx.conf
RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
CMD ["nginx"]
