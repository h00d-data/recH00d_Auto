from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data: bytes) -> bytes:
    return cipher.encrypt(data)

def decrypt(data: bytes) -> bytes:
    return cipher.decrypt(data)
