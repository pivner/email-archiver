from imap_tools import MailBox, A
import read_configs
import read_secrets

def get_emails(email, password, hostname):
    emails = []
    print(password)
    with MailBox(hostname).login(email, password, 'INBOX') as mailbox:
        for msg in mailbox.fetch():
            print("found")
    return emails

if __name__=="__main__":
    print("pending")
    login = read_configs.read_configs()
    mail = get_emails(login[0],read_secrets.read_secret(login[1]),login[2])
    
    print("completed")
