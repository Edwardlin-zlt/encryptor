import os
import shutil

from cryptography.fernet import Fernet
from pathlib import Path


class Encryptor:
    def __init__(self, key):
        self.key = key

    def __encrypt_file(self, filename):
        """
        Given a filename (str) and key (bytes), it encrypts the file and write it
        """
        f = Fernet(self.key)
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
            # encrypt data
            encrypted_data = f.encrypt(file_data)
            # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print(f"{filename} done")

    def __encrypt_dir(self, targetDir='encrypt-folder'):
        for dirPath, dirNames, filenames in os.walk(targetDir):
            for filename in filenames:
                self.__encrypt_file(os.path.join(dirPath, filename))

    def encrypt(self, file_or_dir):
        path = Path(file_or_dir)
        if os.path.isfile(path):
            self.__encrypt_file(path)
        elif os.path.isdir(path):
            self.__encrypt_dir(path)
        else:
            raise Exception()
