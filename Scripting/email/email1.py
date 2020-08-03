import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'anderson.cardenas.r@gmail.com'
email['to'] = 'anderson.cardenas@epn.edu.ec' 
email['subject'] = 'You will be ok'

email.set_content('I am a Pyhton Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: 
    smtp.ehlo()  #id of server
    smtp.starttls() #encription <3
    print('qq')
    smtp.login('anderson.cardenas.r@gmail.com', '****')
    smtp.send_message(email)
    print('all good crack')



