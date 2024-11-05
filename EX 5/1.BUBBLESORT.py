def bubblesort(elements):
    """
    this function performs bubblle siorting of elements 
    in the list and returns the sorted list
    """
    import time
    com = 0
    swap = 0
    #assigning the starting time
    start_time = time.time()
    n = len(elements)
    #iterating the loop for no of elements
    for i in range(n-1):
        #iterating for comparisons
        for j in range(n-i-1):
            #incrementing comparisons by one
            com += 1
            #checking if element is greater than next element
            if elements[j] > elements[j+1]:
                #incrementing swap by one
                swap += 1
                #swaping the elements
                elements[j], elements[j+1] = elements[j+1], elements[j]
    #
    end_time = time.time()
    print("the time is ",(end_time - start_time))
    print("comparisons: ",com)
    print("swaps: ",swap)
    return com

def bubble_sorted_list():
    """
    this function creates a list of elements and find the 
    ratio for the order od n^2, n^3 and log n
    """
    import math
    import random as r
    ele = [10,100,1000,10000]
    for element in ele:
        #generating the list of randomly generated elements
        elements = [r.randint(0,99) for i in range(element)]
        print(f"for no of elements {element}")
        #sorting the randomly generated elements
        f = bubblesort(elements)
        g = [element**2, element**3, math.log(element)]
        for j in g:
            #printing the ratio
            print(f"ratio for {j} : ",(f/j))
        print("---------------------------------------------")

if "__main__" == __name__:
    bubble_sorted_list()
