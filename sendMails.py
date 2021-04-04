# ----------------------------------------
# Created on 3rd Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script defines the function required
to send the emails out to all recipients

Functions:
    sendMail(body, to)
        Logs in to the sender account and sends
        out the message "body" to the reciever.

    generateMessage(email, msg, name)
        Generates the body of the message to send
        out through sendMail().

    parseData(names, mails, sendMail, msg)
        Goes through the data from the GForm to
        then send out mails to people who have
        are subscribed.
'''
# ----------------------------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
# ----------------------------------------
sub = '[BOT] Wholesome Reminder'


def sendMail(body, to):
    global sub
    # Gets secrets
    with open('secrets.json', 'r') as fh:
        secrets = json.load(fh)

    # Set username and password
    sender_address = secrets['from_email']
    sender_password = secrets['from_password']

    # Setup message to send
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = to
    message['Subject'] = sub
    message.attach(MIMEText(body, 'plain'))

    # Start mail session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_password)

    # Send mail and quit session
    text = message.as_string()
    session.sendmail(sender_address, to, text)
    session.quit()


def generateMessage(email, msg, name=False):
    body = f"Hi {name}! Here's some links for you to check out :)\n"

    if not name:
        body = "Hi! Here's your daily dose of the good side of humanity :)\n"

    body += msg
    body += '\n\nEdit form to unsubscribe:https://forms.gle/LX1H6gzYFT7oTSx68'
    body += '\n\nThis mail was generated by a bot.'
    body += '\nRepo: https://github.com/CachedCoding/MailList'
    # Sends the email
    sendMail(body, email)


def parseData(names, mails, sendMail, msg):
    # For each person
    for i in range(len(names)):
        # If they don't want to recieve the mail
        if not sendMail[i]:
            continue

        # If name not given
        if not names[i]:
            generateMessage(mails[i])
            continue

        # If name given
        generateMessage(mails[i], msg, names[i])


if __name__ == '__main__':
    msg = 'This is a test, sent from my terminal'
    sub = '[BOT] Email Test'
    sendMail(msg, 'cachedcoding@gmail.com')
