import smtplib

def sendmail(skey,skey1,skey2):
    TO = "pbr1996.pk@gmail.com"
    SUBJECT = 'Digital Signature'
    TEXT ="key1:" + skey +" ----------" +"key2:"+skey1+" ----------" +"key3:"+skey2
     
    print(TEXT)
    # Gmail Sign In
    gmail_sender = "pbr1996.pk@gmail.com"
    gmail_passwd = "Pulkit123"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()
