from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1:])]


class CustomAES:

    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        cipher = AES.new(self.key, AES.MODE_ECB)
        cipher_text = cipher.encrypt(pad(plain_text))
        return cipher_text.hex()

    def decrypt(self, cipher_text):
        cipher = AES.new(self.key, AES.MODE_ECB)
        plain_text = unpad(cipher.decrypt(bytes.fromhex(cipher_text)))
        return plain_text.decode('euc-kr')
