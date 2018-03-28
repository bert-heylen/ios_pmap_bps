import smtplib
import sys
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
me = sys.argv[1] 
recipient = [sys.argv[2]]
pngfiles = ['chart-series.png', 'chart-stacked.png']

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Policy-map graphs'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = me
msg['To'] = COMMASPACE.join(recipient)
msg.preamble = 'Policy-map graphs'

# Assume we know that the image files are all in PNG format
for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP(sys.argv[3])
s.sendmail(me, recipient, msg.as_string())
s.quit()
