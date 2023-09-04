from cryptography.fernet import Fernet
import base64

key_str = "???"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                #secret_keyword=zoom
key = base64.b64encode(key_str.encode())
f = Fernet(key)
encoded_flag = f.encrypt(b"???")
print("The encoded flag is: ",encoded_flag)