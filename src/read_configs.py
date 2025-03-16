import json
import getpass
import read_secrets
import os

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
    configs = {
        "email": email,
        "password": password,
        "hostname": hostname,
        "lastarchived": 0
    }
    try:
        file = open("../configs.json", "x")
    except:
        os.remove("../configs.json")
        file = open("../configs.json", "x")
    file.close()
    file = open("../configs.json", "w")
    json.dump(configs, file)
if __name__=="__main__":
    write_configs()
