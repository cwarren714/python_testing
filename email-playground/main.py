from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# loading .env
load_dotenv()
app_pass = os.environ.get('APP_PASS')

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Chandler Warren'
email['to'] = 'chandlerawarren@gmail.com'
email['subject'] = 'You won a bunch of money'

# can use dict for substitute if using multiple variables
email.set_content(html.substitute(name='Tintin'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('testingpython12346@gmail.com', app_pass)
    smtp.send_message(email)
    print('all good boss')
