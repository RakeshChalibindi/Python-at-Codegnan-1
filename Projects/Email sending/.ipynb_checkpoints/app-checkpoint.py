# import required modules

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

#server configuration 
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "Here write sender mail"
passkey = "Here, write your sender mail passkey"

def singleEmailSend(to_email:str,subject:str,body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email 
    msg['from'] = sender_email
    msg['subject'] = subject 
    msg.attach(MIMEText(body,'plain'))

    try:
        #start server
        server = SMTP(smtp_server,smtp_port)
        #start server 
        server.starttls()
        #login to server
        server.login(sender_email,passkey)
        #send email
        server.sendmail(from_addr=sender_email,to_addrs=to_email,msg=msg.as_string())
        server.quit()
        return f"Successfully email send to {to_email}"
    except Exception as e:
        return f"Failed to send email because:{e}"
    
#to_email input("Enter Email address:")
to_email = input("Enter Email Address: ")
subject = input("Enter subject:")
body = input("Enter Email Body:")

#call singleEmailSend
print(singleEmailSend(to_email,subject,body))