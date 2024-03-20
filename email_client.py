import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# SMTP is a protocol that allows users to send mails using Python. This involves logging in into an existing mail
# and sending mails to other accounts.

# To proceed define a server and a port.
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# To start the service, use the "ehlo" command.
server.ehlo()
# Next, login to an existing account by providing an email and a password.
# Since the password is stored in a text file in the working directory, open and read the text file to get the password.
with open("password.txt", "r") as f:
    password = f.read()


#Proceed to logging in to  your mail by providing an email address.
server.login("yourEmailaddress@gmail.com", password)

# Next, create the message to be mailed. This includes the recipient, sender, subject, body and even any attachments.
# Using the libraries below will enable the creation of the message of the email to be sent.
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["FROM"] = "Mr Test Email"
msg["TO"] = "recipient@gmail.com"
msg["SUBJECT"] = "Build a Python Email bot"

# For the message, load a pre-written text file with the contents of the body of the mail.
with open("message_text.txt", "r") as f:
    message = f.read()
# In the line of code below, attach the text file as plain text using MIMEText module.
msg.attach(MIMEText(message, "plain"))

# So far, the script is able to add the header contents and the body of the mail.
# Before sending the message, add some lines of code that will enable attachments to be added into the email.

attached_file = "sample_img.jpg"
attachment = open(attached_file, "rb")

# The next step involves creating a payload object. THis process creates a stream that will process the image data.
payLoad = MIMEBase("application", "octet-stream")
payLoad.set_payload(attachment.read())

# The next step then encodes the image that has been read, then add a header to the attachment and then append the attachment to the message.
encoders.encode_base64(payLoad)
payLoad.add_header("Content-Disposition", f"attachment; filename={attached_file}" )
msg.attach(payLoad)

text = msg.as_string() # convert the entire message into a string
server.sendmail("yourEmailaddress@gmail.com", "recipient@gmail.com", text)
server.quit()