'''
pip install imapclient
easy_install pyzmail
'''
import imapclient
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(conn)
'''
##Email Providers And Their IMAP Servers
Gmail : imap.gmail.com
Outlook : imap-mail.outlook.com
Yahoo Mail : imap.mail.yahoo.com
'''
l1=conn.login('Here is Email','Here is Password')
print(l1)
print("Login Success!!!")
print(conn.list_folders())
names=input("Enter The Folder Name:")
select_info =conn.select_folder(names, readonly=True)
print('%d messages in INBOX' % select_info[b'EXISTS'])
UIDs= conn.search(criteria='ALL')
#UIDs= conn.search(['ALL'])
'''
'ALL'          Returns all messagesin the folder.

'BEFORE date',  These there search keys retuns, respectively, messages thaat
'ON date',      were received by the IMAP server before , on ,or after the given
'SINCE date'    date. Date Format : 05-Jul-2016

'SUBJECT string',  Returns message where string is found in the subject,body,either
'BODY string',     or either, repectively. If the String has spaces in it , then
'TEXT string'      Format : 'TEXT "Search with Spaces"'
'''
print(UIDs)
idn=int(input('Enter Email Id:'))
rawMessage= conn.fetch([idn], ['BODY[]', 'FLAGS'])
message= pyzmail.PyzMessage.factory(rawMessage[idn][b'BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))
print(message.get_address('bcc'))
print(message.text_part)
print(message.html_part == None)
print(message.text_part.get_payload().decode('UTF-8'))
print(message.text_part.charset == None)
#For Deleting The Mails
ans=input("Do you You Want To Delete Any Email(Y/N):")
if ans =='Y' or ans =='y':
    print(conn.list_folders())
    name=input("Enter The Folder Name:")
    conn.select_folder(name, readonly=False)
    UIDs = conn.search(['ALL'])
    print(UIDs)
    idns=input('Enter Email Id:')
    conn.delete_messages([idns])
    conn.logout
print(conn.logout)
print("LogOut Success!!!")



