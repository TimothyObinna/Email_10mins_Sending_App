import smtplib
from email.message import EmailMessage
import time
import datetime

sender_email = 'ionyolu2757@gmail.com'
password = 'xbxqmazblaztnutf'
receiver_email = ['soulcleansing96@gmail.com', 'etoontop@gmail.com','joshlove00001@gmail.com', 'anthonyonyolu@gmail.com']
subject = 'Email Testing'


msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content('This is my first testing of email in python')

def send_email():
	my_time = datetime.datetime.now()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as Myemail:
		Myemail.login(sender_email, password)
		Myemail.send_message(msg)
		print(f'Email Sent Successfully at {my_time} .')

while True:
	send_email()
	time.sleep(600)
