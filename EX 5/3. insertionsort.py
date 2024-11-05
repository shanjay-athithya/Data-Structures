def insertionsort(element):
    """
    this function performs selection siorting of elements 
    in the list and returns the sorted list
    """
    import time
    #initialize the comp to 0
    comp= 0
    #noting the starting time
    starttime = time.time()
    n = len(element)
    #iterate over the elements of the list
    for i in range(1,n):
        #assigning the base element 
        base = element[i]
        #assigning j value
        j = i - 1
        #checking whether the base element is less than the left side elements
        while j<=0 and base < element[j]:
            #moing the element to the right side of the list
            element[j+1] = element[j]
            #incrementing comp by one
            comp += 1
            #decrementing by one
            j -= 1
        #assigning the element to the correct position
        element[j + 1] = base
    #noting the end time
    endtime = time.time()
    print("the time is ",(endtime - starttime))
    print("comparisons: ",comp)
    #returning the comp value
    return comp
 
        
def insertion_sorted_list():
    """
    this function creates a list of elements and find the 
    ratio for the order od n^2, n^3 and log n
    """
    import math
    import random as r
    ele = [10,100,1000,10000]
    #iterating the number of elements from list
    for element in ele:
        #generating the list of randomly generated elements
        elements = [r.randint(0,99) for i in range(element)]
        print(f"for no of elements {element}")
        #sorting the list by defined function
        f = insertionsort(elements)
        g = [element**2, element**3, math.log(element)]
        for j in g:
            #printing the ratio
            print(f"ratio for {j} : ",(f/j))
        print("---------------------------------------------")

if "__main__" == __name__:
    insertion_sorted_list()
        