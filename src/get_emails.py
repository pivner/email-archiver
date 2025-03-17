from imap_tools import MailBox, A
import read_configs
import read_secrets
import process_emails

def get_emails(email, password, hostname, return_dir):
    emails = []
    with MailBox(hostname).login(email, password, 'INBOX') as mailbox:
        for msg in mailbox.fetch():
            process_emails.process_email(msg,return_dir)
    return emails

if __name__=="__main__":
    print("pending")
    login = read_configs.read_configs()
    mail = get_emails(login[0],read_secrets.read_secret(login[1]).decode("utf-8"),login[2],login[3])
    print("completed")
