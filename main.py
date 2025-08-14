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
print(f"Original message: {cipher_text}")