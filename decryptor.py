import shutil
import os

from cryptography.fernet import Fernet


class Decryptor:
    def __init__(self, key):
        self.key = key

    def __decrypt_file(self, filename):
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        f = Fernet(self.key)
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
            # decrypt data
            decrypted_data = f.decrypt(encrypted_data)
            # write the original file
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        print(f"{filename} has done")

    def __decrypt_dir(self, targetDir):
        for dir_path, dir_names, filenames in os.walk(targetDir):
            for filename in filenames:
                self.__decrypt_file(os.path.join(dir_path, filename))

    def decrypt(self, file_or_dir):
        if os.path.isfile(file_or_dir):
            self.__decrypt_file(file_or_dir)
        elif os.path.isdir(file_or_dir):
            self.__decrypt_dir(file_or_dir)
        else:
            raise Exception()
