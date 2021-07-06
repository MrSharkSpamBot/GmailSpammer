# -*- coding: utf-8 -*-
'''
A full fledged gmail spamming tool.

@author: Mr. Shark Spam Bot
'''
import smtplib
import re
import sys
import socket

# Define variables needed.
PASSWORD_MIN = 8
PASSWORD_MAX = 100
gmail_regex = re.compile(r'''
[A-Za-z0-9.]+
@gmail.com
''', re.VERBOSE)

# Print everything needed to user and get info needed to spam.
try:

    print('''
\t░██████╗░███╗░░░███╗░█████╗░██╗██╗░░░░░
\t██╔════╝░████╗░████║██╔══██╗██║██║░░░░░
\t██║░░██╗░██╔████╔██║███████║██║██║░░░░░
\t██║░░╚██╗██║╚██╔╝██║██╔══██║██║██║░░░░░
\t╚██████╔╝██║░╚═╝░██║██║░░██║██║███████╗
\t░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝

\t░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
\t██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
\t╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
\t░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
\t██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
\t╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
\tCreated by Mr. Shark Spam Bot.
    ''')
    print('Every word and punctuation in your message will be sent in a different email.')
    print('For this to work you need to put less secure apps on, on your google account.')
    print('This can be done from the link: https://myaccount.google.com/lesssecureapps.\n')
    print('Please enter your gmail account.')
    user_gmail = input('> ')
    print('Please enter your password.')
    user_password = input('> ')
    print('Please enter the gmail account you want to spam.')
    target_gmail = input('> ')
    print('Please enter your message.')
    spam_message = input('> ')

    # Check for valid input.
    while True:
        user_gmail = user_gmail.strip()
        target_gmail = target_gmail.strip()
        if gmail_regex.search(user_gmail) and gmail_regex.search(target_gmail):
            break
        if not gmail_regex.search(user_gmail):
            print('Please enter your gmail account.(make sure it is valid!!!)')
            user_gmail = input('> ')
        if not gmail_regex.search(target_gmail):
            print('Please enter the gmail account you want to spam.(make sure it is valid!!!)')
            target_gmail = input('> ')

    while True:
        if PASSWORD_MAX >= len(user_password) >= PASSWORD_MIN and not user_password.isspace():
            break
        print('Please enter your password.(make sure it is valid!!!)')
        user_password = input('> ')

    while True:
        if spam_message and not spam_message.isspace():
            break
        print('Please enter your message.(make sure it is valid!!!)')
        spam_message = input('> ')

except KeyboardInterrupt:
    print('\n[+] Ctrl + c detected.')
    print('[-] Terminating program.')
    sys.exit()

# Define Functions needed.
def spam(user, password, target, message):
    '''Spam the target.'''
    try:
        global GMAIL_SERVICE
        GMAIL_SERVICE = smtplib.SMTP('smtp.gmail.com', 587)
    except socket.gaierror:
        print('\n[-] You are not connected to the internet.')
        print('[-] Terminating program.')
        sys.exit()
    try:
        GMAIL_SERVICE.ehlo()
        GMAIL_SERVICE.starttls()
    except smtplib.SMTPServerDisconnected:
        print('\n[-] You have been disconnected from the smtp server.')
        print('[-] Terminating program')
        sys.exit()
    try:
        GMAIL_SERVICE.login(user, password)
    except smtplib.SMTPAuthenticationError:
        print('\n[-] Could not log into gmail account.')
        print('[-] Terminating program.')
        sys.exit()

    try:
        print('\n[*] Sending emails...')
        message = message.split()
        for word in message:
            GMAIL_SERVICE.sendmail(user_gmail, target, word)
    except smtplib.SMTPServerDisconnected:
        print('\n[-] You have been disconnected from the smtp server.')
        print('[-] Terminating program')
        sys.exit()

    GMAIL_SERVICE.quit()
    print('\n[+] Possibly spammed target.')

# Fill the target's gmail inbox.
try:
    spam(user_gmail, user_password, target_gmail, spam_message)
except KeyboardInterrupt:
    print('\n[+] Ctrl + c detected.')
    print('[-] Terminating program.')
    GMAIL_SERVICE.quit()
    sys.exit()
