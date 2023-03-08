import imaplib
import email
import os
import re
import time
import requests


def read_emails(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    result, email_data = mail.uid("search", None, "UNSEEN")
    email_uids = email_data[0].split()
    email_messages = []
    for email_uid in email_uids:
        result, email_data = mail.uid("fetch", email_uid, "(RFC822)")
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        email_messages.append(email_message)
    return email_messages

username = os.environ['EMAIL_ADDRESS']
password = os.environ['EMAIL_PASSWORD']
while True:
    email_messages = read_emails(username, password)
    for email_message in email_messages:
        try:
            url = re.findall("(?P<url>https?://[^\s]+)",str(email_message))[0]
            requests.get(url)
        except Exception as e:
            print(e)
            pass
    time.sleep(30)
