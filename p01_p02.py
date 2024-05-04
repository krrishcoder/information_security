# Q 1 > error correcting code
# Q 2 > ERROR DETECTING CODE

import numpy as np
import math



def find_redundant_bit(m):
    r = 0
    while math.pow(2,r) < m+r+1 :
        r +=1
    return r

def redundant_pos(r):
    redun_pos = np.zeros(r, dtype="int")
    while r >0 :
        r-=1
        redun_pos[r] = math.pow(2,r)

    return  redun_pos

def calc_hamming_code(redun_pos,r,m,data):

    x = math.pow(2,r) - 1
    arr = list(range(1, int(math.pow(2,r))))

    arr = np.array(arr)

    data_pos = np.setdiff1d(arr, redun_pos)

    hamming_code = np.zeros(m + r, dtype="int")


    print("-----------------------------")
    for index,val in enumerate(data_pos):
        hamming_code[val-1] = data[index]
        

    print(hamming_code)
    print("-----------------------------")

    r_value = np.zeros(r,dtype="int")  #size of 3

    # finding parity bits 

    for id,i in enumerate(redun_pos):        # 1 , 2 , 4
       # 2 to power 3 -1
        temp = 0

        for d in data_pos:            
            # i =1 , d = [3 5 6 7]

            if i & d == i :                 #  0 0 1  and  0 1 1 gives -->  0 0 1
                if hamming_code[d-1] ==1:
                    temp +=1

        if temp%2 ==0 :
            # even
            r_value[id] = 0
        else :
            #odd
            r_value[id] = 1

    

    for id,i in enumerate(redun_pos):
        hamming_code[i-1] = r_value[id]


    print(f"this is my final hamming code : : : {hamming_code}")

    return hamming_code


def error_detection(code,m,r, redun_pos,):

    arr = list(range(1, int(math.pow(2, r))))   # from 1 to 2^r or 1 to 8
    arr = np.array(arr)

    data_pos = np.setdiff1d(arr, redun_pos)   # set difference of  1 to 8 and reduntant_pos to get data bit pos

    r_value = np.zeros(r,dtype="int")

    # parity bit checking 


    for id,i in enumerate(redun_pos):
       # 2 to power 3 -1
        temp = 0
        for d in data_pos:
            # i =1 , d = [3 5 6 7]
            if i & d == i :
                if code[d-1] ==1:
                    temp +=1

        temp += code[i-1]

        if temp%2 ==0 :
            # even
            print(f"index is : {id} even for {i}")
            r_value[id] = 0
        else :
            # odd

            print(f"index is : {id} odd for {i}")
            r_value[id] = 1

    return  r_value





# for parity p1 which data d  will bw work

def main():

    # i used 4 data bit
    data = np.array([1, 0, 1, 1])


    # may be, sometime we had to invert the data array , to get right answer

    m = len(data)
    r = find_redundant_bit(m)
    print(f"m = {m} , r = {r}")

    #The r redundant bits placed at bit positions of powers of 2, i.e. 1, 2, 4, 8, 16 etc
    # 2^0 = 1, 2^1 = 2,  2^2 = 4 , 2^3 =8

    # p8 d7_ d6_ d5_ p4 d3_ p2 p1

    redun_pos = redundant_pos(r)                   # here finding the index of reduntatnts bits
    print(f"redundant positions :{redun_pos}")

    hamming_code = calc_hamming_code(redun_pos,r,m,data)   # creating the string that will be send
    print(f"the code that will be send : {hamming_code}")

    #____________________________________________here you can add any error in the code send


    #___________________________________________sending____________

    hamming_code = np.array([0,1,1,0,0,1,1])

    error_parity_pos = error_detection(hamming_code,m,r,redun_pos)
    print(f"error positions : {error_parity_pos}")



if __name__ == "__main__":
    main()

