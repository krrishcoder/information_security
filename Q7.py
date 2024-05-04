# rail fence cipher transposition operation

# depth of rail cipher
# 2 , 3  , 4

import numpy as np
import math

def encryption(plain_text,depth):

    plain_text = plain_text.replace(" ", "")

    col = len(plain_text)
    arr = np.empty((depth, col), dtype='str')

    k =0
    j = 0
    flag = 0

    cipher = []

    for i in range(0,col):
        arr[j,i] = plain_text[k]

        if j == depth-1:
            flag =1
            
        if j == 0:
            flag = 0


        if flag ==0:
            j +=1
        else:
            j -=1
            
        k +=1

        # 0 1 2 3 4 5 6 7
        # 0 1 2 0 1 2 0
       
    for i in range(0,depth):
        for j in range(0,col):
            if arr[i,j] != "":
                cipher.append(arr[i,j])

    print(arr.shape)
    print("\n==========================================================================================================\n")
    print(arr)
    print("\n==========================================================================================================\n")
    print(cipher)
    return cipher



def decryption(cipher,depth):
    num = int(len(cipher)/depth)
    l = len(cipher)

    print("num ",num)
    
    j =0
    for i in range(0,num):
        j=i
        for i in range(0,2):
            print(cipher[j],end=" ")
            j +=9

    print("\n")



def main():
    print("start__")
    plain_text = "thank you very much b"
    depth =2
    x= encryption(plain_text,depth)
    decryption(x,depth)


if __name__ == "__main__":
    main()