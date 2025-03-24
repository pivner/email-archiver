from imap_tools import MailBox
import read_configs
import read_secrets
import process_emails
import datetime

def get_emails(email, password, hostname, return_dir, earliest_date):
    emails = []
    with MailBox(hostname).login(email, password, 'INBOX') as mailbox:
        for msg in mailbox.fetch():
            temp = msg.date.date().strftime("%s")
            if int(temp)>int(earliest_date):
                process_emails.process_email(msg,return_dir)
    return emails

if __name__=="__main__":
    login = read_configs.read_configs()
    mail = get_emails(login[0],read_secrets.read_secret(login[1]).decode("utf-8"),login[2],login[3],login[4])
