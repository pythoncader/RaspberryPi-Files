import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import socket
# Change to your own account information
# Account Information
to = 'dancingmichael2@gmail.com' # Email to send to.
gmail_user = 'caderigby@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'th1s1smy#h3ll0w0rld' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

# Creates a sentence for each ip address.
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(get_ip())
msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()
