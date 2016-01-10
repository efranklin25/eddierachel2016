from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from bottle import request

def build_message():
    subject = "New RSVP from " + request.forms.get("name")

    one = "\nName: " + request.forms.get("name")
    two = "\nPhone: " + request.forms.get("phone")
    three = "\nE-Mail: " + request.forms.get("email")
    four = "\nCan they attend the wedding?: " + request.forms.get("attending")
    five = "\nBringing another guest?: " + request.forms.get("guests")
    six = "\nWill be bringing " + request.forms.get("kids")
    seven = "\nNotes: " + request.forms.get("message")

    content = one + two + three + four + five + six + seven

    account = {
        'user' : 'eddie.franklin20@gmail.com',
        'pwd' : '0frazlid',
        'recipient' : 'eddierachel2016@gmail.com',
        'subject' : subject,
        'body' : content
    }
    return account

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(TEXT, 'plain'))


    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        text = msg.as_string()
        smtpserver.sendmail(FROM, TO, text)
        #server_ssl.quit()
        smtpserver.close()
        print 'successfully sent the mail'
    except Exception,e: print str(e)


