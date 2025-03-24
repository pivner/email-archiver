import json
import getpass
import read_secrets
import os
import datetime

def read_configs():
    with open("../configs.json") as file:
        config = json.load(file)
    return [i for i in config.values()]


def write_configs():
    email = input("Enter email address:")
    while True:
        password = getpass.getpass(prompt="Please Enter your password:")
        if password == getpass.getpass(prompt="Please Re-enter your password:"):
            break
        else:
            print("Error validating password")
    password = read_secrets.create_secret(password.encode("utf-8")).decode("utf-8")
    hostname = input("Enter your hostname:")
    storage_directory= input("Enter the directory which the files should be stored:")
    configs = {
        "email": email,
        "password": password,
        "hostname": hostname,
        "storage_directory": storage_directory,
        "lastarchived": datetime.date(1900,1,1).strftime("%s")
    }
    try:
        file = open("../configs.json", "x")
    except:
        os.remove("../configs.json")
        file = open("../configs.json", "x")
    file.close()
    file = open("../configs.json", "w")
    json.dump(configs, file)
    file.close()

def write_today_config():
    file = open("../configs.json", "r")
    configs = [i for i in json.load(file).values()]
    file.close()
    configs[4] = datetime.date.today()
    file = open("../configs.json", "w")
    json.dump(configs, file)
    file.close()
if __name__=="__main__":
    write_today_config()
