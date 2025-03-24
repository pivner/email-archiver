import json
import getpass
import read_secrets
import os
import datetime

def read_configs():
    with open("../configs.json") as file:
        config = [i for i in json.load(file).values()]
    return config


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
        "lastarchived": datetime.date(1900,1,1).strftime("%s"),
        "backup_delay": -1
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
    new_configs = {
        "email": configs[0],
        "password": configs[1],
        "hostname": configs[2],
        "storage_directory": configs[3],
        "lastarchived": datetime.date.today().strftime("%s"),
        "backup_delay": configs[5]
    }
    configs[4] = datetime.date.today().strftime("%s")
    file = open("../configs.json", "w")
    json.dump(new_configs, file)
    file.close()

def write_scheduled_backup_time(time):
    file = open("../configs.json", "r")
    configs = [i for i in json.load(file).values()]
    file.close()
    new_configs = {
        "email": configs[0],
        "password": configs[1],
        "hostname": configs[2],
        "storage_directory": configs[3],
        "lastarchived": configs[4],
        "backup_delay": time
    }
    file = open("../configs.json", "w")
    json.dump(new_configs, file)
    file.close()

if __name__=="__main__":
    write_today_config()
