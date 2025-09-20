# Phrase Encryption and Decryption
# This program encrypts and decrypts a phrase using a simple substitution cipher.
# It creates a random mapping of characters to encrypt and decrypt the message.
# Note: The key is generated randomly each time the program runs, so the same input will yield different outputs on different runs.
# Only use this for educational purposes, as it is not secure for real-world applications.

# First, I imported shuffle from the module random.
from random import shuffle
# Then, I imported punctuation, digits, and ascii_letters from the module string.
from string import punctuation, digits, ascii_letters
# Next, I created a varible of characters that includes space, punctuation, digits, and letters.
chars = " " + punctuation + digits + ascii_letters
# I converted the string of characters into a list.
chars = list(chars)
# I created a copy of the list of characters and shuffled it to create a random key.
key = chars.copy()
shuffle(key)

# Encryption and Decryption Process
# Encrytion:
# First, I prompted the user to enter a phrase to encrypt.
plain_text = input("Enter to Encrypt: ")
# Then, I initialized an empty string for the cipher text.
cipher_text = ""
# Next, I looped through each letter in the plain text, found its index in the chars list, and appended the corresponding letter from the key list to the cipher text.
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
# Then, I printed the original plain text and the resulting cipher text.
print(f"Decrypted message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decryption:
# First, I prompted the user to enter a phrase to decrypt.
cipher_text = input("Enter to Decrypt: ")
# Then, I initialized an empty string for the plain text.
plain_text = ""
# Next, I looped through each letter in the cipher text, found its index in the key list, and appended the corresponding letter from the chars list to the plain text.
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
# Finally, I printed the original cipher text and the resulting plain text.
print(f"Encrypted message: {cipher_text}")
print(f"Decrypted message: {plain_text}")