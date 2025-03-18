import store_emails

def process_email(msg, dir):
    file = open(f'{dir}/{msg.from_}:{msg.subject}:{msg.date}.txt', "x")
    file.write(msg.text)
    file.close()
    file = open(f'{dir}/{msg.from_}:{msg.subject}:{msg.date}.html', "x")
    file.write(msg.html)
    file.close()
    store_emails.store_email()

