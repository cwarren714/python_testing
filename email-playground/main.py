from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

# loading .env
load_dotenv('../.env')
trying = os.environ.get('APP_PASS')
print(trying)
