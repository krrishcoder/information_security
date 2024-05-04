# row transposition cipher transposition operation

import  numpy as np
import  math


def create_cipher(plain_text,key):
    col = len(key)
    text_len = len(plain_text)
    row = text_len//col

    arr = np.zeros((row,col),dtype='int')
    print(arr)

    plain_text = plain_text.replace(" ", "")

    text_len = len(plain_text)

    k = 0
    for i in range(0,row):
        j = 0
        while(j<col):  # 0 1 2  3 4 5 6 

            if(k == text_len):
                 arr[i,j] = ord('x') - 97
                 j +=1
                 continue
    
            arr[i,j] = ord(plain_text[k]) - 97
            j += 1
            k += 1

    print_in_char(arr,row,col)

    # matrix is ready now

    new_cipher = []

    for i in range(0,len(key)):

        index = np.where(key == (i+1))
        index = index[0][0]
        
        for j in range(0,row):
            new_cipher.append(arr[j,index])

    
    print_array(new_cipher)

    return new_cipher





def print_in_char(mat,row,col):
        
        print("")
        for i in range(0,row):
            for j in range(0,col):
                print(f"{chr(mat[i,j] +97)}  ",end="")
            print("")

        print("")




def print_array(arr):

    for i in range(0,len(arr)):
        print(f"{chr(arr[i]+97)}", end="")

        

def decryption(key,cipher,n):
    col = len(key)

    text_len = len(cipher)

    row = text_len//col

    arr = np.zeros((row,col),dtype='int')
    print(arr)

    temp = []
    k = 0

    
  
    for i in range(0,len(key)):  # 0 to 6

        index = np.where(key == (i+1))
        index = index[0][0]
        
        for j in range(0,row):         # 0 to 5
            arr[j,index] = cipher[k]
            k +=1

    print("done")
    print_in_char(arr,row,col)

      


def main():
    print("start__")

    n = 7
    key = np.array([4,3,1,2,5,6,7])      # index is used
    plain_text = "kill corona virus at twelve am tomorrow"
    cipher = create_cipher(plain_text,key)


    decryption(key,cipher,n)






if __name__ == "__main__":
    main()