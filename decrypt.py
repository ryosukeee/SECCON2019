import sys
from Crypto.Cipher import AES
import base64

def decrypt(key, encTxt):
        t= ''
        for j in range(len(encTxt)):
                t += chr((((ord(encTxt[j]) -0x20) - (ord(key[j % len(key)]) - 0x20)) % (0x7e - 0x20 + 1)) + 0x20)
        return t

key1 = "SECCON"
key2 = "seccon2019"
text = sys.argv[1]

dec1 = base64.b64decode(text)
cipher = AES.new(key2 + chr(0x00) * (16 - (len(key2) % 16)), AES.MODE_ECB)
dec2 = cipher.decrypt(dec1).decode("ascii")
print(decrypt(key1, dec2))
