FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt


CMD python3 ./teleg_bot.py
