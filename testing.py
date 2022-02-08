import smtplib, time, random, cryptography
afile = open('phrases.txt',encoding="utf8")
lines = afile.readlines()


gmail_user = 'hellomyfriend12121@gmail.com'
gmail_pass = 'SECRET_KEY'


while True:
    new_line = random.choice(lines)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user,gmail_pass)
        server.sendmail(gmail_user, 'luis1abreu11@gmail.com', new_line.encode("ascii", "ignore"))
        server.close()

        print('Email Sent')
        time.sleep(10)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
        break
