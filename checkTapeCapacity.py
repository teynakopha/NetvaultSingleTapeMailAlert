#!/usr/bin/python

import psycopg2
import smtplib

conn = psycopg2.connect(database = "", user = "postgres", password = "pass123", host = "192.168.2.106", port = "5432")
print('Opened database successfully')

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')

conn.commit()
conn.close()

## send mail after check complated 
gmail_user = 'sattaya@got.co.th'
gmail_password = '******'
sent_from = gmail_user
to = ['gotsts@gmail.com', 'its@got.co.th']
subject = 'Netvault Capacity is Full !!!! pleas replace new Tape to single lib'
body = "เรียนทุกท่าน /n ผมรบกวนเปลี่ยนเทปให้หน่อยครับ tape อยู่ใน ลิ้นชักที่โต็ะผม เขียน label ไว้แล้ว /n Thank you /n sattaya banbua"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print('Something went wrong...')

