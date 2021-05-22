FROM python:3.8.3-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
