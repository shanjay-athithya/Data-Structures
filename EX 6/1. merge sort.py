def merging(list1,list2):
    """
    this funstion is used to merge two
    sorted list into one and return the list
    """
    a = len(list1)
    #assigning the index of list1 to 0
    ind_a = 0
    b = len(list2)
    #assigning the index of list2 to 0
    ind_b = 0
    final = []
    #checking whether the index are less than the length of the lists
    while ind_a < a and ind_b < b:
        #checking if the element in ind_a is less than the element in ind_b
        if list1[ind_a] < list2[ind_b]:
            #adding the small element to result list
            final.append(list1[ind_a])
            #incrementing index by 1
            ind_a += 1
        else:
            #if the element in ind_b is smaller adding it to result lis5t
            final.append(list2[ind_b])
            #incrementing index by 1
            ind_b += 1
    #adding the remaining elements in the list
    if ind_a < a:
        final.extend(list1[ind_a:])
    elif ind_b < b:
        final.extend(list2[ind_b:])
    #returning the final merged list
    return final

def mergesort(seq):
    """
    this is a recursive function that sorts 
    the list by dividing it ands conquering it 
    with the help of merging function and 
    returns the sorted list
    """
    l = len(seq)
    #checking whether the there is only one element in list base condition
    if l < 2:
        return seq[:]
    else:
        #dividing the list into two based on divider index
        divider = l // 2
        return merging(mergesort(seq[:divider]),mergesort(seq[divider:]))

if "__main__" == __name__:
    import time as t
    import random as r
    import math as m
    for ran in [10, 100, 1000, 10000]:
        rand_list = [r.randint(0,999) for ele in range(ran)]
        """print("the unsorted list is : ", rand_list)
        print("------------------------------------------------")"""
        starttime = t.time()
        sorted_list = mergesort(rand_list)
        endtime = t.time()
        """print("the sortded list is : ",sorted_list )
        print("-------------------------------------------------")"""
        totaltime = endtime - starttime
        print("the total time taken is : ", (totaltime))
        for g in [ran**2, ran**3, ran*(m.log(ran, 2))]:
            ratio = (totaltime/g)
            print(ratio)
