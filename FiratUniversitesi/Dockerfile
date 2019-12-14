FROM python:alpine3.7
COPY . /app
WORKDIR /app

RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
EXPOSE 5002
CMD python ./firatApi.py