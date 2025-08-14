# Python Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
# print(f"chars: {chars}")
# print(f"key: {chars}")

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""
for symbol in cipher_text:
    index = key.index(symbol)
    plain_text += chars[index]

print(f"Original message: {cipher_text}")
print(f"Decrypted message: {plain_text}")