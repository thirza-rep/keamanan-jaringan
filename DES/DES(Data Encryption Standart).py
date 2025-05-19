from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = b'12345678'  # 8 bytes

cipher = DES.new(key, DES.MODE_ECB)

data = b'Sriwijaya, berselang serundingan'
padded_data = pad(data, DES.block_size)

encrypted = cipher.encrypt(padded_data)
print("Encrypted:", encrypted.hex())

cipher2 = DES.new(key, DES.MODE_ECB)
decrypted_padded = cipher2.decrypt(encrypted)
decrypted = unpad(decrypted_padded, DES.block_size)
print("Decrypted:", decrypted.decode())
