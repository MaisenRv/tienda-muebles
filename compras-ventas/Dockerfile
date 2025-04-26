FROM alpine:latest
WORKDIR /app

COPY . .
RUN apk update
RUN apk upgrade
RUN apk add python3
RUN apk add py3-flask
EXPOSE 8000

CMD ["python", "app.py"] 