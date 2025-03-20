import os
import read_configs
import read_secrets
import get_emails

if __name__ == "__main__":
    first_run = True if os.path.isfile("./configs.json") else False
    if first_run:
        read_configs.write_configs()
    cond = 0;
    login = read_configs.read_configs()
    while True:
        cond = input("Please select an option: 1-4\n1: Archive emails\n2: Search for emails\n3: Reset configs.json\n4: Exit\n")
        if cond=="1":
            get_emails(login[0],read_secrets.read_secret(login[1]).decode("utf-8"),login[2],login[3])
        elif cond=="2":
            #missing search functions
            pass
        elif cond=="3":
            read_configs.write_configs()
        elif cond=="4":
            break
