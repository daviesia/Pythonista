#!/usr/bin/env python
"""
    small script to check for unread count on imap inbox
"""
import sys
import imaplib
import keychain
import clipboard
import shortcuts

# keychain.set_password('IMAP', 'HSE', ' ')
# keychain.set_password('IMAP', 'LKD', ' ')

IMAPSERVER = 'imap.bell.net'
USER1 = 'iddavies@sympatico.ca'
PASSWORD1 = keychain.get_password('IMAP', 'HSE')

USER2 = 'ianddavies@sympatico.ca'
PASSWORD2 = keychain.get_password('IMAP', 'LKD')

def get_unread_mail_count(USER, PASSWORD) :
    try:
        mail = imaplib.IMAP4_SSL(IMAPSERVER)
        mail.login(USER, PASSWORD)
        mail.select("inbox", True) # connect to inbox.
        return_code, mail_ids = mail.search(None, 'UnSeen')
        # count = len(mail_ids[0].split(b' '))
        # 2022-11-03 Fix an issue where count was always one over the actual count.
        count = len(mail_ids[0].split())
        mail.close()
        mail.logout()
    except:
        count = 0
    
    # print(count)
    return (count)

def main():
    # If Shortcuts name is passed in the
    # command line, use it. Otherwise
    # default to "Goodnight 1".
    if len(sys.argv) - 1==0:
        shortcutName="Goodnight 1"
    else:
        shortcutName = sys.argv[1]
    
    count = get_unread_mail_count(USER1, PASSWORD1)
    # print(count)
    
    count = count + get_unread_mail_count(USER2, PASSWORD2)
    # print(count)

    clipboard.set(str(count))
    # print(count)
    shortcuts.open_shortcuts_app(name=shortcutName)

if __name__ == '__main__':
	main()

