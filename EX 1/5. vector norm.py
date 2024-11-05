#defining a fuction to find the norm of vector
def norm(v,p):
    #initiating vector sum as zero
    vector_sum = 0
    #iterating the input vactors
    for value in v:
        vector_sum += value ** p
    p_norm_value = vector_sum ** (1/p)
    #returning the result
    return p_norm_value
#defining a fuction to get input vectors from user
def input_vectors():
    #creating an empty list
    input_list = []
    #asking the range of vector list
    input_range = int(input("enter the range of the vectors : "))
    for vectors in range(0,input_range,1):
        #geting input vactor and adddind to the list
        input_vector = int(input("enter the input vectors : "))
        input_list.append(input_vector)
    #returing the list as tuple
    return tuple(input_list)
if __name__ == "__main__":
    #assingning a variable to the input function
    v = input_vectors()
    #calling the function and displaying the result
    print(norm(v,2))