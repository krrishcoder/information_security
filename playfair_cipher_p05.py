# error detecting code

# Q 5  -->  playfair cipher

import  numpy as np
import  math


def prepare_matrix(key):

    arr =  np.empty((5, 5), dtype=str)

    alphabet = np.array(['a' ,'b', 'c', 'd', 'e' ,'f', 'g' ,'h', 'ij' ,'k' ,'l', 'm' ,'n' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v' ,'w' ,'x' ,'y' ,'z'])

    alphabetx = []

    flag = -1

    for id, i in enumerate(alphabet):

        for j in key:

            if i == "i" or i =="j":
                alphabetx.append("ij")
                continue

            if i != j:
                flag = 0
            else:
                flag = -1
                break

        if flag ==0:
            alphabetx.append(i)

   # this array contains all alpabets except "company"

    print(f"printing array { alphabetx}")

    k = 0
    flag = 0

    for i in range(0,5):
        for j in range(0,5):
            if flag == 0:
                arr[i,j] = key[k]       
            else:
                arr[i,j] = alphabetx[k]            # when flag is -1 than we will read from remaining alphabets,

            if k == (key.shape[0] -1) and flag==0: # until we have company word, till that we will read from key
                k= -1
                flag = -1
            k +=1
    return arr



def make_pair_of_message(mssg):  # will return array of array , that is  [[ , ],  [ , ], [  , ]]


    arr  = list(mssg)
    arr_ = np.array(arr)
 
    result = []

    i = 0

    while i < arr_.shape[0] :   # until we read all the letter in word
        temp = []

        if arr_[i] ==" ":
            i +=1


        temp.append(arr_[i])
        i +=1

        if i == arr_.shape[0]:
            temp.append("z")
            result.append(temp)
            continue



        if arr_[i] ==" ":
            temp.append("z")
            i +=1
            result.append(temp)
            continue

        temp.append(arr_[i])
        i+=1

        # check for same

        if temp[0] == temp[1]:
            temp[1] = "x"
            i -=1

        result.append(temp)

    print(result)

    return  result

def encode_the_message(paired, arr):

    dict  = {}

    for i in range(0,5):
        for j in range(0,5):
            dict[arr[i,j]] = [i,j]

    
    # dict will be used as
    # input : 'c'  , output  [0,0]
    # input : letter , output index if that letter in array of 5 x 5


    i = 0

    result = []
    # print(dict)

    while i < (len(paired)-1):   # running for each pair of letter,

        temp_arr = []
        a,b = dict[paired[i][0]]
        ax,bx = dict[paired[i][1]]

        # [a , b]    is  the index of member 1st of a pair
        # [ax , bx]  is  the index of member 2nd of a pair

        # check for same row
        if a == ax :
            print("same row")
            code_a_pos = (b + 1) % 5    # getting letter positioned at right side of ___ letter
            code_b_pos = (bx + 1) % 5
            temp_arr.append(arr[a,code_a_pos])
            temp_arr.append(arr[a,code_b_pos])

            # print(temp_arr)
            result.append(temp_arr)
            i += 1
            continue

        # # check for same column
        if b == bx:
            print("same col")
            code_a_pos = (a + 1) % 5  # getting letter positioned at down side of ___ letter
            code_b_pos = (ax + 1) % 5
            temp_arr.append(arr[code_a_pos,b])

            temp_arr.append(arr[code_b_pos,b])

            # print(temp_arr)
            result.append(temp_arr)
            i += 1
            continue

   
        # if not found on same column or row

        tempp = paired[i]  

        sorted_flag = 0
        a, b = dict[paired[i][0]]
        ax, bx = dict[paired[i][1]]


        if a >ax :
            paired[i] = sorted(paired[i])
            if tempp != paired[i]:
                sorted_flag = 1

            a, b = dict[paired[i][0]]
            ax, bx = dict[paired[i][1]]


        temp = []

        if a>=ax:
            if b>=bx:
                temp = arr[ax:a+1,bx:b+1]
            else:
                temp = arr[ax:a+1,b:bx+1]

        else:
            if b>=bx:
                temp = arr[a:ax + 1, bx:b + 1]
            else:
                temp = arr[a:ax + 1, b:bx + 1]


        print(f"temp is {temp}")


        r,c = temp.shape
        print(r,c)

        pos_first_letter = 0
        pos_second_letter = 0

        if temp[0,c-1] == paired[i][0]:
            pos_first_letter = c-1
        else:
            pos_first_letter = 0

        code_a_col = 0
        if pos_first_letter==0:
            code_a_col = c-1


        code_a  =  temp[0,code_a_col]

        print(f"position first letter {pos_first_letter}")
        print(f"code_a {code_a}, code_col_a {code_a_col}")

        if code_a_col == 0:
            code_b_col = (code_a_col) + c - 1
        else:
            code_b_col = 0

        # print(f"position of first letter {pos_first_letter}")
        # print(f"code for 1st {code_a_col} code for 2nd  {code_b_col}")
        code_b =  temp[r-1,code_b_col]


        temp_arr.append(code_a)
        temp_arr.append(code_b)

        if sorted_flag == 1:
            print(f"revering back {temp_arr}")
            temp_arr = temp_arr[::-1]


        # print(temp_arr)
        result.append(temp_arr)
        i += 1

    return result



def main():

    # word "company" used for creating the array of 5 x 5, which will be furthur used to create a cipher
    key = np.array(list("company"))
    
    # preparing matrix
    arr = prepare_matrix(key)

 
    message = "meet me after the toga party"

    print(arr)

    # making pair of letter , if we get single member in a pair than we will give 'z' to it, to make  a complete pair
    paired  = make_pair_of_message(message)

    # creaing cipher code
    result = encode_the_message(paired,arr)

    print(f"cipher text {result}")







if __name__ == "__main__":
    main()
