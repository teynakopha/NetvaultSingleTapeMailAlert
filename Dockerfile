FROM python:3

MAINTAINER Mr. Sattaya Banbua

WORKDIR /home

RUN apt-get update 
RUN apt-get install cron
RUN pip install -r lib.txt
COPY ./checkTapeCapacity.py /home/checkTapeCapacity.py
COPY ./lib.txt /home/lib.txt
COPY ./crontab /etc/crontab
RUN systemctl status cron
RUN systemctl restart cron




