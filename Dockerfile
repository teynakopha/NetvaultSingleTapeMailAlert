FROM python:3

COPY checkTapeCapacity.py /home/checkTapeCapacity.py

RUN apt-get update & dpkg -l cron & apt-get install cron
RUN systemctl status cron
COPY crontab /etc/crontab
RUN systemctl restart cron




