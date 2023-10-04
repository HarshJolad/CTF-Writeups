from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii

def decrypt_message(ciphertext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message


key_utf8 = input('ENTER THE KEY (as UTF-8 string): ')
key_bytes = key_utf8.encode('utf-8')  

iv_utf8 = input("ENTER THE IV (as UTF-8 string): ")
iv_bytes = iv_utf8.encode('utf-8')  

ciphertext_hex = "7a8f550d25dcc94f6544525dcd26ae128cf93955455e62e556f2b562a4e8544d"
ciphertext = binascii.unhexlify(ciphertext_hex)

try:
    decrypted_message = decrypt_message(ciphertext, key_bytes, iv_bytes)
    decrypted_hex = binascii.hexlify(decrypted_message).decode('utf-8')
    
    print("Decrypted Message (Hex):", decrypted_hex)
except Exception as e:
    print("Error:", str(e))
