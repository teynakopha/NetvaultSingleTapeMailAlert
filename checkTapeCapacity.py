#!/usr/bin/python
from __future__ import print_function
import psycopg2
import smtplib

conn = psycopg2.connect(database = "netvault_mediamanagement", user = "postgres", password = "p@ssw0rd", host = "192.168.2.106", port = "51486")
print('Opened database successfully')

cur = conn.cursor()
cur.execute('''SELECT  label,  mediagroup, barcode, librarymachine, 
       mediaformat, mediatype, spaceused/ 1024 / 1024 / 1024 as speaceused, spaceleft / 1024 / 1024 / 1024 as spaceleft,
       libraryname, readerrors,
       writeerrors, segments, datawritten, dataread, timesinit, mediaexpiresystime, 
       mediaexpiredate, mediaexpiretime, lastwritesystime, lastwritedate, 
       importdate, importtime, online, reuse, blocksize, writeprotected, 
       logicalslotposition, physicalslotposition, drivename, bay
  FROM public.media_view where label like '%LTO%' and librarymachine !=' ' ;''')
rows = cur.fetchall()
message = ''
for row in rows:
    print(row)
    message = row

conn.commit()
conn.close()

gmail_user = 'testimap2541@gmail.com'
gmail_password = 'imaptest'


def sendMail(messagePara):
    sent_from = gmail_user
    to = ['sattaya@got.co.th']
    subject = 'FROM BOT,GOT แจ้งงานธนาคารไทยพาณิชย์ Serial :  '
    body = 'Hello Outsource,\n\n ** อีเมลล์ฉบับนี้ถูกสร้างขึ้นโดย Bot ** ' + \
    'รบกวนท่านใดอยู่ office เปลี่ยนเทปเครื่อง backup server ให้หน่อยครับ '+\
    'Backup Server : 192.168.2.106 , default user '
    netvault_text = '''
    Media name : {0} 
    speaces used :{1} GB
    speces available : {2} GB
    '''.format(messagePara[0],messagePara[6],messagePara[7])
    email_text = 'From: {}\nTo: {}\nSubject:: {}\n{}'.format(sent_from, ", ".join(to), subject, body+netvault_text+"\n\n ขอบคุณครับ")
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("testimap2541@gmail.com", "imaptest")
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text.encode('utf-8'))
        server.close()
        print("can send messag \n"+ email_text)
    except:
        print("can't send message \n"+ email_text)

sendMail(messagePara=message)
