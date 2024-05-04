import  numpy as np
import  math

def char_to_int(key):
    arr = np.empty(len(key), dtype='int')
    for i in range(0,len(key)):
        arr[i] = ord(key[i]) - 97
    return arr

          
def create_matrix(key,polybius_text):
    col = len(polybius_text)
    row = len(polybius_text)
    print(f"col : {col} , row : {col}")

    key = list(key)
    arr = np.empty((row, col), dtype='str')

    alphabet = np.arange(26)
    key_np =  char_to_int(key)
    remain_alphabet = np.setdiff1d(alphabet, key_np)
    k =0
    p =0
    x = 0
    for i in range(0,row):
        for j in range(0,col):
            if k <len(key):
                # first filling the key letters
                arr[i][j] = key[k]
                k +=1
            elif p < len(remain_alphabet):
                 # now filling the remaining letters
                arr[i][j] = chr(remain_alphabet[p] +97)
                p +=1
            else:
                # now filling the remaining with numbers
                arr[i][j] = str(x)
                x +=1

    print(arr)
    return arr
  
# intermediate cipher function 
def encoding_first_time(key ,key2, polybius_text , plain_text ):

    arr = create_matrix(key, polybius_text)
    cipher = []
    polybius_text = list(polybius_text)
    plain_text = list(plain_text)

    # first store all the indexes for each letter
    dict = {}
    col = len(polybius_text)
    row = len(polybius_text)

    for i in range(0,row):
        for j in range(0,col):
            dict[arr[i][j]] = [i,j]
    #print(dict)
    # now iterating for the plain text encoding
    for i in range(0, len(plain_text)):
        cipher.append( [ polybius_text[dict[plain_text[i]][0]] ,  polybius_text[dict[plain_text[i]][1]]]  )
    print("intermediate cipher_________________")
    print(cipher)
    return final_encoding(cipher,key2, arr)


def final_encoding(cipher , key2 , key_arr):
    print("key2 is : ", key2)
    print("col is : ",len(key2))

    col = len(key2)
    row = math.ceil(len(cipher)*2/col)
    print("row is : ",row)

    arr = np.empty((row, col), dtype='str')

    x = 0
    temp =0
    for i in range(0,row):
        for j in range(0,col):

            if x == len(cipher):
                arr[i][j] = 'X'

            else:
                arr[i][j] = cipher[x][temp]

                if temp == 1:
                    x +=1
                    temp=0
                else:
                    temp =1
    print(arr)
    # now read according to key given
    print(key2)
    cipher_text = []

    for i in range(0,len(key2)):
        index = np.where(key2 == i)
        cipher_text.append(list(arr[:,index[0][0]]))

    my_string = ''.join(''.join(sub_list) for sub_list in cipher_text)
    print(my_string)

    return my_string

  

def decoding(cipher_text, key2, key, polybius_text):
    print("__________________________________________________________________________________________________________\n")
    key_arr = create_matrix(key, polybius_text)
    col = len(key2)
    row = int(len(cipher_text)/col)

    print(row,col)
    arr = np.empty((row, col), dtype='str')
    cipher_text = np.array(list(cipher_text))

    for i in range(0,len(key2)):
        index = np.where(key2 == i)
       # print(cipher_text[i*row : (i*row)+(row)])         # 0 to 5 , 6 to 11

        arr[:,index[0][0]] = cipher_text[i*row : (i*row)+(row)]

    intermediate_cipher = []

    for i in range(0,row):
        intermediate_cipher.append(list(arr[i,:]))

    print(arr)
    my_string = ''.join(''.join(sub_list) for sub_list in intermediate_cipher)

    print(my_string)
    polybius_text = list("ADFGVX")
    print(key_arr)


    dict = {}
    col = len(polybius_text)
    row = len(polybius_text)

    for i in range(0,row):
        for j in range(0,col):
            dict[( polybius_text[i],polybius_text[j])] =   key_arr[i][j]

        #print(dict)
    # now iterating for the plain text encoding

    print(dict)

    plain_text = []

    len_arr = len(my_string)
    i = 0
    my_string = list(my_string)
    while(i<len_arr):
        plain_text.append(dict[ ( my_string[i], my_string[i+1]) ])
        i +=2

    print("\n")
    print(plain_text)


def main():
    print("start__")  
    # A D F G V X

    key = "hi mom i love you much"
    key2 = "402153"
    plain_text = "you see but you do no"
    polybius_text = "ADFGVX"

    key = key.replace(" ", "")
    key = list(dict.fromkeys(list(key)))
    plain_text = plain_text.replace(" ","")

    key2 = list(key2)
    num_list = [int(num_str) for num_str in key2]
    key2 = np.array(num_list)

    #encoding 
    my_string = encoding_first_time(key, key2, polybius_text,plain_text)
    #decoding
    decoding(my_string, key2, key, polybius_text)


if __name__ == "__main__":
    main()