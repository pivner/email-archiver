from imap_tools import OR
import os


def process_email(msg, dir):
    for i in range(2):
        try:
            if i and msg.text: # i=1, msg.text isnt empty
                file = open(f'{dir}/{msg.from_}:{msg.subject}:{msg.date}.txt', "x")
            elif not i and msg.html: #i=0, msg.html isnt empty
                file = open(f'{dir}/{msg.from_}:{msg.subject}:{msg.date}.html', "x")
            else: #Both are empty
                break # Dont open null file
        except:
            break # file exists, dont open it again
        if i:
            file.write(msg.text)
        else:
            file.write(msg.html)
        file.close()
