import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail_attch(from_addr, password,to_addr,files):
    try:
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = password
        msg['From'] = from_addr
        msg['Subject'] = "Annotation Details"
        message = "Annotation Details"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # add multiple recipients
        to_list = to_addr


        # open the file to be sent
        for filename in files:
            attachment = open(filename, "rb")

            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # attach the instance 'p' to instance 'msg'
            msg.attach(p)

        # create SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(msg['From'], password)

        # send the message to multiple recipients
        s.sendmail(msg['From'], to_list, msg.as_string())

        # Terminate the SMTP session
        s.quit()
        return "Mail sent successfully !!!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    message = send_mail_attch()
    print(message)
    
