import smtplib
import string
import random
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#creates email template using a comma seperated list of college names and email addresses
def makeRecipients():
    #opens list
    with open("/Users/kateriordan/Desktop/emails/CollegeEmails2.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      #parses through list
      for row in csv_reader:
          if line_count == 0:
            line_count += 1
          else:
              line_count += 1
              sender(row[0],row[1])

#recieves name and email + generic message from make recipients to send email
def sender(name,email):
    print (email)
    size = random.choice("SML")

    body = """Dear """+ name + """,
My name is Kate Riordan and I am a senior at Columbus North High School in Columbus, Indiana. I recently heard about your school, but I would love to learn more! I serve as the president of the National Honor Society and Spanish Club, and co-founded our school's Model United Nations Club. I scored a 1450 on my SAT, have a 3.95 unweighted GPA, and have taken 12 AP classes. I play the french horn in our Wind Ensemble and Orchestra, and am a member of my school's tennis team. I also enjoy teaching kids to code in my free time! Please send me any information or materials to help me make my college decision! (I love t-shirts!) Have a great day!
Kate Riordan
825 Tipton Lane
Columbus, IN 47201
T-shirt Size: """+size+""""""

    msg = MIMEMultipart()

    msg['Subject'] = 'College Representation'
    msg['From'] = 'kate.riordan19@gmail.com'
    msg['To'] = (email)

    msg.attach(MIMEText(body,'plain'))

    #logs into gmail server to send messages
    server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
    server.starttls()
    server.login('kate.riordan19@gmail.com', '9356Kate')
    server.send_message(msg)
    del msg
    server.quit()

#calls method to send all emails
makeRecipients()

