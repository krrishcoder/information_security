# polyalphabetic cipher substitution operation

# vignere

import pandas as pd
import numpy as np
from itertools import permutations



def generate_key(length,key):
    key_len = len(list(key))
    key_gen = ""

    factor = length//key_len
    remainder = length%key_len
    while factor >0 :
        key_gen =  key_gen + key
        factor -=1
    key_gen  = key_gen + key[0:remainder]

    return key_gen

def encryption(plain_text, key):

    p_arr = ''.join(plain_text.split())
    data = list(p_arr)

    plain_text_length = len(data)
    print(f"plain text length: {plain_text_length}")
    keygen = generate_key(plain_text_length,key)

    key_arr= list(keygen)
    cipher= []
    
    for i,j in zip(key_arr,data):
        sum = (ord(i) - 97) + (ord(j)-97)
        sum = sum%26
        
        cipher.append( chr( sum + 97 ))

    return cipher

def decryption(cipher, key):

    cipher_length = len(cipher)
    keygen = generate_key(cipher_length,key)

    key_arr= list(keygen)
    plain_text = []
    
    for i,j in zip(key_arr,cipher):
        sum = (ord(j) - 97) - (ord(i)-97)

        if(sum <0):
            sum += 25

        plain_text.append( chr( sum + 97 ))

    return plain_text




def main():
    print("program started")
    key = "deceptive"
    message = input("give a plain text in alphabet only : ")
    cipher = encryption(message,key)
    print(cipher)

    plain_text = decryption(cipher,key)
    print(f"decoded text is : {plain_text}")

if __name__ == "__main__":
    main()



