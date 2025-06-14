from Crypto.Cipher import AES
import base64
import hashlib

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_password(password, key_hex):
    key = bytes.fromhex(key_hex)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(password).encode())
    return base64.b64encode(encrypted).decode()

from Crypto.Cipher import AES
import base64

def decrypt_password(enc_password_b64, key_hex):
    key = bytes.fromhex(key_hex)
    enc_data = base64.b64decode(enc_password_b64)
    nonce = enc_data[:16]
    ciphertext = enc_data[16:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()

