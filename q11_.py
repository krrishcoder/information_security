import time

def xor_cipher(plaintext, key):
   
    ciphertext = ""
    key_stream = generate_key_stream(len(plaintext), key)   # length of complete message  , key

    print("key gen  :- ", key_stream)
    
    for i in range(len(plaintext)):
        # XOR the plaintext character with the corresponding key stream character
        # and convert the result to a character
        char = chr(ord(plaintext[i]) ^ key_stream[i])
        ciphertext += char
    
    return ciphertext

def generate_key_stream(length, key):
   
    key_stream = []
    key_length = len(key)
    
    for i in range(length):                                         # loop till length of plain_text
        # Generate the key stream by repeating the key cyclically
        key_stream.append(ord(key[i % key_length]))                 # same key will be used each time 
                                                                    # using remainder 
    return key_stream



def main():
    print("________________________________________ starting of code ________________________________________")

    time.sleep(1)
    # Example usage:
    plaintext = "Ram ji ki sena chali"
    key = "secretkey"

    # Encryption
    encrypted_text = xor_cipher(plaintext, key)
    print("Encrypted:", encrypted_text)
    print("length of encrypted text is , ", len(encrypted_text))

    # Decryption
    decrypted_text = xor_cipher(encrypted_text, key)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()