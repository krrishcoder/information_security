import pandas as pd
import numpy as np

# ceaser cipher
# a to z indexes

def generate_key(shift=0):
    alphabet = np.array(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x',
         'y', 'z'])

    a_to_int = 97
    arr = np.array(range(0,26))
    arr = arr - shift
    keys = []

    for i in arr:
        val = 0
        if i < 0 :
            val = i + 26
        else:
            val = i
        keys.append(chr(val+a_to_int))

    print(keys)

    return keys

def encryption(plain_text, key):
    p_arr = ''.join(plain_text.split())
    data = list(p_arr)
    cipher = []

    for i in data:
        cipher.append(key[ord(i) - 97])
    return cipher


def decryption(cipher_text, key):

    cipher = cipher_text
    plain_text = []

    for i in cipher:
        plain_text.append(key[ord(i) - 97])
    return plain_text


def main():

    # we are  creating an array of already shifted alphabets,
    # so that at same index we can gets its code
    
    keys = generate_key(3)
    message = input("give a plain text in alphabet only : ")
    cipher = encryption(message,keys)
    print(cipher)


    # d_key = generate_key(-3)
    # plain_text = decryption(cipher,d_key)
    # print(plain_text)

if __name__ == "__main__":
    main()


