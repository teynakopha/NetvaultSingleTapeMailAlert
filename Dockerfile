FROM python:3

MAINTAINER Mr. Sattaya Banbua sattay@got.co.th

WORKDIR /home

RUN apt-get update -y \
    && apt-get install cron -y

COPY ./checkTapeCapacity.py /home/checkTapeCapacity.py
COPY ./lib.txt /home/lib.txt
COPY ./crontab /etc/crontab

RUN pip install -r lib.txt \
    && service status cron \
    && service restart cron
