#importing random function
import random
#defining a fuction to shuffle the input list
def shuffle(input_data):
    #using index number to shuffle the elements of the input list
    for i in range(len(input_data)-1):
        #generating random index number
        j = random.randint(0,len(input_data)-1)
        #shuffling the input data
        input_data[j], input_data[i] = input_data[i], input_data[j]
        #returing the final result
        return input_data
#defining a fuction to get input from user
def required_input():
    data=eval(input("enter the given sequence of numbers as a list : "))
    return data
if __name__ == "__main__":
    #assigning a fuction to a variable
    input_data = required_input()
    #calling and displaying the result from the fuction
    print(shuffle(input_data))
