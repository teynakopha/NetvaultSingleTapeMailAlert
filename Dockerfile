FROM python:3

MAINTAINER Mr. Sattaya Banbua

WORKDIR /home

RUN apt-get update -y
RUN apt-get install cron -y

COPY ./checkTapeCapacity.py /home/checkTapeCapacity.py
COPY ./lib.txt /home/lib.txt
COPY ./crontab /etc/crontab
RUN pip install -r lib.txt
RUN systemctl status cron
RUN systemctl restart cron




