import os.path

from KeyUtil import load_key
from KeyUtil import write_key
from decryptor import Decryptor
from encryptor import Encryptor


def main():
    key = ""
    while True:
        command = input("Commands: 1.newKey | 2.loadKey | 3.encrypt | 4.decrypt\n")
        if command == "newKey" or command == "1":
            write_key()
        if command == "loadKey" or command == "2":
            key = load_key()
            encryptor = Encryptor(key)
            decryptor = Decryptor(key)
        if command == "encrypt" or command == "3":
            if len(key) > 0:
                fileOrDir = input("Please enter the file or dir you want to encrypt\n")
                encryptor.encrypt(fileOrDir)
            else:
                print("key file didn't load yet")
        if command == "decrypt" or command == "4":
            if len(key) > 0:
                fileOrDir = input("Please enter the file or dir you want to decrypt\n")
                decryptor.decrypt(fileOrDir)
            else:
                print("key file didn't load yet")
        if command == "exit" or command == "0":
            exit()


if __name__ == '__main__':
    main()
