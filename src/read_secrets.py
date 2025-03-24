import secrets
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def create_secret(Unencrypted):
    while True:
        try:
            file = open("../secrets","x")
            using_preexisting = False
            break
        except:
            while True:
                using_preexisting = input("File already exists, should we use preexisting keys? [Y/N]").lower()
                using_preexisting = True if using_preexisting=='y' else using_preexisting
                using_preexisting = False if using_preexisting=='n' else using_preexisting
                if using_preexisting:
                    file = open("../secrets","r")
                    break
                elif not (using_preexisting):
                    os.remove("../secrets")
                    file = open("../secrets", "x")
                    break
        break
    if using_preexisting:
        key = Fernet(file.readline())
        file.close()
        return key.encrypt(Unencrypted)
    else:
        file.close()
        file = open("../secrets", "wb")
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000)
        key = base64.urlsafe_b64encode(kdf.derive(Unencrypted))
        file.write(key)
        key = Fernet(key)
    return key.encrypt(Unencrypted)

def read_secret(Secret):
    file = open("../secrets", "r")
    key = file.readline()
    key = Fernet(key)
    temp = key.decrypt(Secret)
    return temp
