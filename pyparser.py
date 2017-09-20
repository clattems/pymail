#!/usr/bin/python
# Import the email modules we'll need
import re
from email.parser import Parser
from email.utils import parseaddr

#  If the e-mail headers are in a file, uncomment this line:
headers = Parser().parse(open('mail_backup/msg.150593019409-20-17.eml', 'r'))


#  Or for parsing headers in a string, use:
#headers = Parser().parsestr('From: <user@example.com>\n'
#        'To: <someone_else@example.com>\n'
#        'Subject: Test message\n'
#        '\n'
#        'Body would go here\n')

#  Now the header items can be accessed as a dictionary:
print 'To: %s' % headers['to']
print 'From: %s' % headers['from']
print 'Subject: %s' % headers['subject']
print 'Date: %s' % headers['date']
print 'Message-id: %s' % headers['message-id']


with open("mail_backup/msg.150593019409-20-17.eml") as origin_file:
    for line in origin_file:
        if "attachment" in line:
            print line

with open("mail_backup/msg.150593019409-20-17.eml") as origin_file:
    for line in origin_file:
        if "size=" in line:
            print line
