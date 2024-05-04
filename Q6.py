# hill cipher substituion operation

# multi letter cipher
# improved quality

# 2 letter at a time , 3 letter at a time

# key is  asquare matrix
# 2 x 2 can encrypt 2 letter at  a time 
# 3 x 3 can encrypt 3 letter at a time

# if ends with two letter than just fill it with filler letter x or z

import  numpy as np
import  math


def find_multiplicative_inverse(num):
    i = 0
    x = 1
    while(i!=1):
        if((num * x)%26 == 1):
            i=1
            break
        else:
            x +=1
    return x

def InverseOfMatrix(mat, n):
    adjoint = np.zeros((n,n),dtype='int')
    for i in range(0,n):
        for j in range(0,n):

            result_matrix = np.delete(mat, i, axis=0)
            result_matrix = np.delete(result_matrix, j, axis=1)
            x = np.linalg.det(result_matrix)
            x = pow(-1,i+j) * round(x)
            adjoint[i,j] = x

    adjoint = adjoint.T % 26

    det_mat = round(np.linalg.det(mat)) % 26

    multi_inv = find_multiplicative_inverse(det_mat)
    result_dot = (multi_inv *  adjoint ) % 26

    return result_dot

  

def make_pair_of_message(mssg,n):     # will return array of array , that is  [[ , , ],  [ , , ], [  ,  ,]]

    arr_ =  np.array(list(mssg))
    text_length = len(arr_)

    result = []

    i = 0
    number_of_triplet = len(arr_)//n

    while  number_of_triplet >0 :      # until we read all the letter in word
        temp = []
        j = n
        while  j >0 and text_length > i  :
            if arr_[i] ==" ":
                i +=1
            else:
                temp.append(arr_[i])
                j -=1
                i +=1
        if len(temp) !=0:
            result.append(temp)

        number_of_triplet -=1

     # code to fill the last triplet which would be half filled  
     # example : [['p', 'a', 'y'], ['m', 'o', 'r'], ['e', 'm', 'o'], ['n', 'e', 'y'], ['a', ]]
     #

    letter_filler = len(result[len(result) - 1 ])  # 2
    while letter_filler < n :
        result[len(result) - 1 ].append("x")
        letter_filler +=1
    return  result


def matrix_multiplication_encoding(triplet_arr , key):   # 1 x 3  , 3 x 3  - -> 1 x 3
    arr = np.array(triplet_arr)
    result_dot = np.dot(arr , key)
    result_dot = result_dot % 26 
    return list(result_dot)



def encryption(plain_text, key,n):

    triplets = make_pair_of_message(plain_text,n)

    print(f"making pair of 3 : : {triplets}")
    triplet_length = len(triplets)
    cipher = []

    for i in range(0,triplet_length):
       
       # before multiplying , convert triplet to intger

       temp = [(ord(letter) -97) for letter in triplets[i]]
       r =  matrix_multiplication_encoding(temp,key)

       int_to_char = [chr(letter + 97) for letter in r]
       cipher.append(int_to_char)

    
    return cipher



def decryption(key,cipher,n):

    print("prepaing inverse of key matrix")
    key_inverse =  InverseOfMatrix(key,n)

    triplet_length = len(cipher)
    
    decoded_text = []

    for i in range(0,triplet_length):
       
       # before multiplying , convert triplet to intger

       temp = [(ord(letter) -97) for letter in cipher[i]]

       r =  matrix_multiplication_encoding(temp,key_inverse)

       int_to_char = [chr(letter + 97) for letter in r]
       decoded_text.append(int_to_char)

    return decoded_text





      

  

def main():
    print("starting___")

    n = 3
    key = np.array([[17,17,5],[21,18,21],[2,2,19]])

    print(f"key matrix of 3 x 3  : {key}")

    plain_text = "pay more money and enjoy"
    cipher = encryption(plain_text,key,n)

    print(cipher)


    decoded_text = decryption(key,cipher,n)

    print("=======================================================================================================================")
    print(decoded_text)
 




if __name__ == "__main__":
    main()