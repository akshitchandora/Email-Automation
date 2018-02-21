import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587) #Domain Name:smtp.gmail.com And Port:587
'''##Email Providers And Their SMTP Servers
Gmail: smtp.gmail.com
Outlook.com/Hotmail.com: smtp-mail.outlook.com
Yahoo Mail:smtp.mail.yahoo.com'''
conn.ehlo() #Hello Method To Connect To SMTP Server
conn.starttls() #TLS Encryption For Password Before You Can Login In
conn.login('Here Your Gmail','Here is Your Password') # Email And Password
'''You Can Use Google App Password Generator For Password - It is Easier to generate password for your different devices. 
Here is Link -> https://security.google.com/settings/security/apppasswords'''
conn.sendmail('Here is Sender Email','Here is Receiver Email','Subject: <Here is Subject>\n\n <Body>')
conn.quit() #Closing connection 
