FROM python:3

WORKDIR /home

COPY checkTapeCapacity.py /home/checkTapeCapacity.py
COPY lib.txt /home/lib.txt
COPY crontab /etc/crontab

RUN apt-get update & dpkg -l cron & apt-get install cron
RUN pip install -r lib.txt
RUN systemctl status cron
RUN systemctl restart cron




