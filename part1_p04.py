
# 4. Implement monoalphabetic 

import pandas as pd
import numpy as np
from itertools import permutations

# ceaser cipher
# a to z indexes



def generate_key():
    arr = np.arange(26)
    np.random.shuffle(arr)

    return arr

def encryption(plain_text, key):
    p_arr = ''.join(plain_text.split())
    data = list(p_arr)
    cipher = []

    for i in data:
        cipher.append( chr(key[ord(i) - 97] +97)  )
    return cipher


def decryption(cipher_text, key):

    cipher = cipher_text
    plain_text = []

    for i in cipher:
        index = np.where(key == (ord(i)-97) )
        z = index[0][0]
        plain_text.append(chr(z + 97)  )

    return plain_text


def main():
    common_key = generate_key()
    print(common_key)
    message = input("give a plain text in alphabet only : ")
    cipher = encryption(message,common_key)
    print(cipher)
    #
    #
    plain_text = decryption(cipher,common_key)
    print(plain_text)

if __name__ == "__main__":
    main()


