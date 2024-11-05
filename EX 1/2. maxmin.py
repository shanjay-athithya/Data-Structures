#defining a function to find the minimum and maximum
def minmax():
    #creating a empty list
    list = []
    #getting input sequence from user
    elements = int(input("enter the number of elements : "))
    #creating a for loop to get as many as input given by user
    for i in range(elements):
        #asking the user to enter the element number
        element = int(input("enter the element : "))
        #addind the element to list
        list.append(element)
    #assigning the first element as maximum and minimum value
    min_element = list[0]
    max_element = list[0]
    #checking for minimum number
    for sequence in range(len(list)):
        #checking minimum is smaller than other elements
        if min_element > list[sequence]:
            #assigning element as minimum element
            min_element = list[sequence]
    #checking for maximum number
    for sequence in range(len(list)):
        #checking maximum is larger than other elements
        if max_element < list[sequence]:
            #assigning element as maximum element
            max_element = list[sequence] 
    #returning the output      
    return (min_element,max_element)
if __name__ == '__main__':
    #displaying the required output
    print("the minimum and maximum number is(minimum,maximum) = ",minmax())

