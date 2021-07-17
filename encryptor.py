import os
import shutil

from cryptography.fernet import Fernet


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

    def __encrypt_dir(self, targetDir='encrypt-folder'):
        for dirPath, dirNames, filenames in os.walk(targetDir):
            for filename in filenames:
                self.__encrypt_file(os.path.join(dirPath, filename))
                print(f"{filename} done")

    def encrypt(self, file_or_dir):
        if os.path.isfile(file_or_dir):
            self.__encrypt_file(file_or_dir)
        elif os.path.isdir(file_or_dir):
            self.__encrypt_dir(file_or_dir)
        else:
            raise Exception()
