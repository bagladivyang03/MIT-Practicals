import imaplib
import pprint
from email import message_from_bytes
from email.parser import HeaderParser
from getpass import getpass

imap_host = 'imap.gmail.com'
imap_user = 'mail_id'
imap_pass = 'mail_id_password'

imap = imaplib.IMAP4_SSL(imap_host)

imap.login(imap_user, imap_pass)
imap.select("Inbox")
print(imap.list())


imap.select("inbox")
_, all_messages = imap.search(None, "ALL")

# Printing total number of messages in inbox
print(f"Total number of mesages in INBOX : {len(all_messages[0].split())}\n\n\n")



_, nth_mail = data = imap.fetch(
    all_messages[0].split()[int(input("Enter n for print headers of 'n'th mail: "))],
    "(RFC822)",
)
headers = []
parser = HeaderParser()
for response in nth_mail:
    if isinstance(response, tuple):
        headers.extend(
            parser.parsestr(message_from_bytes(response[1]).as_string()).items()
        )

# Print all the headers
print("\n\n".join(f"{key}:\n{value}" for key, value in headers))

imap.close()