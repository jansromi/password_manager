import base64
import hashlib
import random
import string
from cryptography.fernet import Fernet
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

class Cipher:
    """
    Static class for encrypting and decrypting passwords.
    """
    
    @staticmethod
    def encrypt(key, source):
            key = base64.urlsafe_b64encode(key)
            f = Fernet(key)
            encrypted_data = f.encrypt(source.encode())
            return encrypted_data.decode()
    
    @staticmethod
    def decrypt(key, source):
        key = base64.urlsafe_b64encode(key)
        f = Fernet(key)
        decrypted_data = f.decrypt(source.encode())
        return decrypted_data.decode()

    @staticmethod
    def compute_master_key(password, salt):
        return PBKDF2(password, salt, dkLen=32,
                      count=1000000, hmac_hash_module=SHA512)

    @staticmethod
    def generate_device_secret():
        return ''.join(random.choice(string.ascii_letters) for i in range(16))
    
    @staticmethod
    def generate_hash(source):
        return hashlib.sha512(source.encode()).hexdigest()