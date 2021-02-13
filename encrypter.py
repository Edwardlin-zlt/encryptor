import sys
import getopt
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


def encryptDir(key, targetDir='encryptfolder'):
    dest = targetDir + '-encrypt'
    shutil.copytree(targetDir, dest)
    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in filenames:
            encrypt(os.path.join(dirpath, filename), key)


def decryptDir(key, targetDir='encryptfolder-encrypt'):
    if targetDir.endswith('-encrypt'):
        dest = targetDir.split('-')[0] + '-decrypt'
    else:
        dest = targetDir + '-decrypt'

    shutil.copytree(targetDir, dest)
    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in filenames:
            decrypt(os.path.join(dirpath, filename), key)


def main():
    opts, args = getopt.getopt(sys.argv[1:], '-d-e-c:', ["decrypt", "encrypt", "credential="])
    # key = load_key()
    key = 1234
    opts_dict = {'operation': None, 'credential': None}
    for (opt, val) in opts:
        if opt in ('-d', 'decrypt'):
            if opts_dict['operation'] is not None:
                raise Exception("Only d or e")
            else:
                opts_dict['operation'] = 'd'
        if opt in ('-e', 'encrypt'):
            if opts_dict['operation'] is not None:
                raise Exception("Only d or e")
            else:
                opts_dict['operation'] = 'd'
        if opt in ('-c', 'credential'):
            opts_dict['credential'] = val

    if opts_dict['credential'] is None:
        raise Exception("No credential found")
    print(opts_dict)


if __name__ == '__main__':
    main()
