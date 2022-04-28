from aes.aes import AES
from config import config


master_key = config.default_key

aes = AES(master_key)

coded=aes.encrypt("word")
print(coded)
decoded = aes.decrypt(coded)
print(decoded)