

def process_email(msg, dir):
    file = open(f'{dir}/{msg.from_}:{msg.subject}:{msg.date}.txt', "x")
    file.write(msg.text)
    file.close()
