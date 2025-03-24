from time import sleep
import read_configs
import get_emails
import read_secrets

if __name__ == "__main__":
    login = read_configs.read_configs()
    time = int(login[5])
    while time != -1:
        sleep(time)
        get_emails.get_emails(login[0],read_secrets.read_secret(login[1]).decode("utf-8"),login[2],login[3],login[4])
