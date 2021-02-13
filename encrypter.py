import os
import shutil

from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named key.key
    """
    return open("key.key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def encryptDir(targetDir, key):
    dest = targetDir + '-encrypt'
    shutil.copytree(targetDir, dest)
    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in filenames:
            encrypt(os.path.join(dirpath, filename), key)


def decryptDir(targetDir: str, key):
    if targetDir.endswith('-encrypt'):
        dest = targetDir.split('-')[0] + '-decrypt'
    else:
        dest = targetDir + '-decrypt'

    shutil.copytree(targetDir, dest)
    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in filenames:
            decrypt(os.path.join(dirpath, filename), key)


if __name__ == '__main__':
    # load the previously generated key
    key = load_key()

    # filePath = path.join(path.abspath('.'), 'encryptfolder/1775139-bigthumbnail.jpg')
    # encrypt(filePath, key)
    # decrypt(filePath, key)

    # targetDir = 'encryptfolder'
    # encryptDir(targetDir, key)
    targetDir = 'encryptfolder-encrypt'
    decryptDir(targetDir, key)
