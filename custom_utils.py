

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


import socket
socket.getaddrinfo('192.168.32.217', 25)
def send_mail(sender,password,receiver,filename):
	try:
		subject = "Annotaion Details"
		body = "Annotaion Details"
		sender_email = sender
		receiver_email = receiver
		password = password

		# Create a multipart message and set headers
		message = MIMEMultipart()
		message["From"] = sender
		message["To"] = receiver
		message["Cc"] = receiver

		message["Subject"] = subject
		# message["Bcc"] = mail  # Recommended for mass emails

		# Add body to email
		message.attach(MIMEText(body, "plain"))

		filename =  filename#"info.csv" # In same directory as script

		# Open PDF file in binary mode
		with open(filename, "rb") as attachment:
			# Add file as application/octet-stream
			# Email client can usually download this automatically as attachment
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		# Encode file in ASCII characters to send by email    
		encoders.encode_base64(part)

		# Add header as key/value pair to attachment part
		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {filename}",
		)

		# Add attachment to message and convert message to string
		message.attach(part)
		text = message.as_string()

		# Log in to server using secure context and send email
		context = ssl.create_default_context()

		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, text)
		return "Message sent sucessfully."
	except Exception as e:
		print(e)
		return e


def send_mail_attcach(sender,password, receiver,files):

	try:
		subject = "Annotaion Details"
		body = f" Hi {receiver.split('.')[0]}, \n\n  Please find the attcahed files for the annotations details"
		sender_email = sender
		receiver_email = receiver
		password = password

		# Create a multipart message and set headers
		message = MIMEMultipart()
		message["From"] = sender
		message["To"] = receiver
		# message["Cc"] = "niladri.das@lincode.ai"
		# message["Cc"] = "sadakat.ali@lincode.ai"


		message["Subject"] = subject
		# message["Bcc"] = mail  # Recommended for mass emails

		# Add body to email
		message.attach(MIMEText(body, "plain"))

		filename =  files[0]#"info.csv" # In same directory as script
		
		for filename in files:
			# Open PDF file in binary mode
			with open(filename, "rb") as attachment:
				# Add file as application/octet-stream
				# Email client can usually download this automatically as attachment
				part = MIMEBase("application", "octet-stream")
				part.set_payload(attachment.read())

			# Encode file in ASCII characters to send by email    
			encoders.encode_base64(part)

			# Add header as key/value pair to attachment part
			part.add_header(
				"Content-Disposition",
				f"attachment; filename= {filename}",
			)

			# Add attachment to message and convert message to string
			message.attach(part)




		text = message.as_string()



		# Log in to server using secure context and send email
		context = ssl.create_default_context()

		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, text)


		return "Mail sent sucessfully."
	except Exception as e:
		print(e)
		return e
