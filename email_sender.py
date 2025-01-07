""" import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'rushya6665@gmail.com'
email['to'] = 'dhiraj.patil@cybermeru.com'
email['subject'] = 'Email Automation'

email.set_content('Bro , i have done email automation by python!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rushya6665@gmail.com','wsrl zdnu bpej mijw')
    smtp.send_message(email)
    print("work done! Email sent") """
    
    
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

template = Template(Path('format.html').read_text())
email = EmailMessage()
email['From']= 'rushya6665@gmail.com'
email['to'] = 'sushil.bhaskar@cybermeru.com'
email['subject'] = 'BHAI KA MAIL'

name_mail = input('BC! whats your name ?- ')

email.set_content(template.substitute({'name':name_mail}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.starttls()
    smtp.login('rushya6665@gmail.com','wsrl zdnu bpej mijw')
    smtp.send_message(email)
    print('message sent')