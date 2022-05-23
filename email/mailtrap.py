import smtplib

subject = "Hi Mailtrap"
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"
mail_body = """This is a test e-mail message."""
# Creating a string with the subject, receiver, sender, and mail body.
message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

 {mail_body}. """

# This is a context manager. It is a way to ensure that resources are properly and automatically
# managed.
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("6d1b386e723c34", "ba94f9715fb88b")
    server.sendmail(sender, receiver, message)
