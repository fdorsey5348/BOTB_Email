import smtplib, csv, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

emailSubject= "For HBCU x HBCU by The NFL";
sender = "botbtestemail@gmail.com";
bodyText = "Place Holder";
password = "BattleOfTheBrains123"


msg = MIMEMultipart()
#body = MIMEText(bodyText)
msg['Subject'] = emailSubject
msg['From'] = sender  

with open('contacts.csv', newline='') as csvfile:
    recipients = list(csv.reader(csvfile))

#for loop
for recipient in recipients:
    msg['To'] = recipient[0]

    #attach body to message
    msg.attach(MIMEText(bodyText, "plain"))

    #convert message to string
    text = msg.as_string()

    # Log in to server using secure context and send email
    #context = ssl.create_default_context()
    #Create SMTP session for sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587, timeout=120) #use gmail with port
    server.starttls() #enable security
    server.login(sender, password)
    server.sendmail(sender, recipient, text)
    server.quit()
    print("Sent Mail to ", recipient[0])