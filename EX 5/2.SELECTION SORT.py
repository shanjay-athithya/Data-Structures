import time
def selectionsort(element):
    """
    this function performs selection siorting of elements 
    in the list and returns the sorted list
    """
    n = len(element)
    #noting the starting time of loop
    start_time = time.time()
    comp = 0
    swap = 0
    #iterating the elements
    for i in range(n-1):
        #assigning the minimum index
        minindex = i
        #iterating the forloop for the elements afteer the minindex element
        for j in range(i+1, n-1):
            #incrementing comparison by one
            comp += 1
            #checking if minimum index number is greater than the other elements
            if element[j] < element[minindex]:
                #incrementing swap by one
                swap += 1
                #assigning the minimum index as j
                minindex = j
        #swaping the elements
        element[i], element[minindex] = element[minindex], element[i]
    #notig the end time 
    end_time = time.time() 
    print("the time is ",(end_time - start_time))
    print("comparisons: ",comp)
    print("swaps: ",swap)
    #returning comp value
    return comp

def selection_sorted_list():
    """
    this function creates a list of elements and find the 
    ratio for the order od n^2, n^3 and log n
    """
    #importing math module to perform logging
    import math
    #importing random to generate random numbers
    import random as r
    ele = [10,100,1000,10000]
    for element in ele:
        #creating a list of randomly generated elements
        elements = [r.randint(0,99) for i in range(element)]
        #sorting the randomly generated elements
        print(f"for no of elements {element}")
        f = selectionsort(elements)
        g = [element**2, element**3, math.log(element)]
        for j in g:
            #printing the ratio
            print(f"ratio for {j} : ",(f/j))
        print("---------------------------------------------")

if "__main__" == __name__:
    selection_sorted_list()