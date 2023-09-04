from cryptography.fernet import Fernet
import base64


key = 'zoomzoomzoomzoomzoomzoomzoomzoom'
encoded_flag = b'gAAAAABk76o1ijCm0VEkemhiVI7Zbmj6zBo5pYsPs3yflYKvpxORdmPWFW97-nZfB1fGtibgUVCrASFsv5XlCrBXg_TVXCc7hXC0U5hCQ03aGrl6VS7GQ8ZXA6O2lvd1kzq4QKpdf7Yz'
key = base64.b64encode(key.encode())
f = Fernet(key)
flag = f.decrypt(encoded_flag)
print("FLAG: ",flag)


# pesu_ec{Z29vZF9qb2JfY29tcmFkZQ==}

