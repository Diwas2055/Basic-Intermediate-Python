import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# ! Send simple email using Gmail

def plain_text_email():

    username = "vegeto@gmail.com"
    password = "password123qwe"
    mail_from = "vegeto@gmail.com"
    mail_to = "goku@dbz.com"
    mail_subject = "Test Subject"
    mail_body = "This is a test message"

    # Creating a new MIME message object.
    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))

    # Creating a connection to the SMTP server.
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # Starting a TLS connection.
    connection.starttls()
    # Logging into the SMTP server.
    connection.login(username, password)
    # Sending the message.
    connection.send_message(mimemsg)
    # It closes the connection to the SMTP server.
    connection.quit()

# Sending a simple email using Gmail.
plain_text_email()

# ! Use Python to send an email using Gmail containing an attachment.

def attachment_file_email():
   
    username = "vegeto@gmail.com"
    password = "password123qwe"
    mail_from = "vegeto@gmail.com"
    mail_to = "goku@dbz.com"
    mail_subject = "Test Subject"
    mail_body = "This is a test message"
    mail_attachment = "https://d1ny9casiyy5u5.cloudfront.net/tmp/test.txt"
    mail_attachment_name = "test.txt"

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))

    with open(mail_attachment, "rb") as attachment:
        # Creating a new MIME object.
        mimefile = MIMEBase('application', 'octet-stream')
        # Reading the file and setting it as the payload.
        mimefile.set_payload((attachment).read())
        # It encodes the file in base64.
        encoders.encode_base64(mimefile)
        # Adding the file name to the attachment.
        mimefile.add_header('Content-Disposition',
                            "attachment; filename= %s" % mail_attachment_name)
        # Attaching the file to the message.
        mimemsg.attach(mimefile)
        
       # Creating a connection to the SMTP server.
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # Starting a TLS connection.
        connection.starttls()
        # Logging into the SMTP server.
        connection.login(username, password)
        # Sending the message.
        connection.send_message(mimemsg)
        # It closes the connection to the SMTP server.
        connection.quit()

attachment_file_email()