from src.services.cipher import Cipher

class Password:
    """
    A representation of the main password that is used to en/de-crypt other passwords.

    @attribute _hashed_master: The hashed master password.
    @attribute _device_secret: A random 16 character string used as a salt.
    @attribute _master_key: The master key used to encrypt and decrypt passwords.
    """

    def __init__(self, masterpass, device_secret=None):
        self._hashed_master = Cipher.generate_hash(masterpass)
        if device_secret is None:
            self._device_secret = Cipher.generate_device_secret()
        else:
            # should check that device_secret is valid
            self._device_secret = device_secret
        self._master_key = Cipher.compute_master_key(masterpass, device_secret)

    def encrypt_password(self, password):
        """
        Encrypts a password using master key.

        @returns Encrypted password as a string.
        @raises InvalidToken: If the master key is incorrect.
        """
        return Cipher.encrypt(self._master_key, password)
    
    def decrypt_password(self, encrypted_password) -> str:
        """
        Decrypts a password using master key.

        @returns Decrypted password as a string.
        @raises InvalidToken: If the master key is incorrect.
        """
        return Cipher.decrypt(self._master_key, encrypted_password)

    def values(self):
        """
        Returns a tuple containing the hashed master password and the device secret.
        """
        return (self._hashed_master, self._device_secret)
















    
    
