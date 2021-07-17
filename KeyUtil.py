from cryptography.fernet import Fernet
import os.path


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        print(f"key file has been write to {os.path.realpath(key_file.name)}")


def load_key():
    """
    Loads the key from the current directory named key.key
    """
    try:
        key = open("key.key", "rb").read()
        print("key loaded")
        return key
    except IOError:
        print(f"please put your key file in {os.path.dirname(__file__)}")


def generate_key():
    print(Fernet.generate_key())
