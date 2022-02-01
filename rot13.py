#!/usr/bin/env python3

import string

offset = int(input("Please enter the offset: "))
encrypted_text = input("Please enter the encrypted text: ")
    
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

decrypted_text = ""

for c in encrypted_text:
    if c in uppercase:
        decrypted_text += uppercase[(uppercase.find(c) + offset) % len(uppercase)]
    elif c in lowercase:
        decrypted_text += lowercase[(lowercase.find(c) + offset) % len(lowercase)]
    else:
        decrypted_text += c

print(decrypted_text)
