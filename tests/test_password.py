import pytest
from src.core.password import Password
from cryptography.fernet import InvalidToken

def test_password_encrypt_and_decrypt():
    pw1 = Password('master_pass', "AAAAAAAAAAAAAAAA")
    encrypted = pw1.encrypt_password('test_password')
    assert encrypted != 'test_password'
    decrypted = pw1.decrypt_password(encrypted)
    assert decrypted == 'test_password'

def test_with_wrong_masterkey():
    pw1 = Password('master_pass', "AAAAAAAAAAAAAAAA")
    pw2 = Password('master_pass', "BBBBBBBBBBBBBBBB")
    encrypted_with_pw1 = pw1.encrypt_password('test_password')
    assert encrypted_with_pw1 != 'test_password'
    with pytest.raises(InvalidToken):
        # different salts result in different keys
        pw2.decrypt_password(encrypted_with_pw1)        

    