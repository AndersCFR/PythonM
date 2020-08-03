import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Tu papi pues'
email['to'] = 'anderson.cardenas@epn.edu.ec' 
email['subject'] = 'You will be ok'

email.set_content(html.substitute({'name': 'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  #id of server
    smtp.starttls() #encription <3
    print('qq')
    smtp.login('anderson.cardenas.r@gmail.com', '****')
    smtp.send_message(email)
    print('all good crack')


