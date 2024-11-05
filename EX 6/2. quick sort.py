def meanfinder(list, start, end):
    """
    this functions arranges the mid number as pivot
    and low number to the start and highest number to the end
    """
    mid = (start + end) // 2
    if list[start] > list[mid]:
        list[start], list[mid] = list[mid], list[start]
    if list[mid] > list[end]:
        list[mid], list[end] = list[end], list[mid]
    if list[start] > list[end]:
        list[start], list[end] = list[end], list[start]
    return list

def indexfinder(list, start, end):
    """
    this function arranges the small numbers to 
    the left and large numbers to the right of the pivot
    """
    list = meanfinder(list,start,end)
    #initiating i and j
    i = start
    j = end - 1
    #assigning pivot as last number
    pivot = list[end]
    #iterating the index until i less than j
    while i <= j :
        while list[i] < pivot and i <= end:
            i += 1
        while list[j] > pivot and j >= start:
            j -= 1
        if i < j:
            list[i], list[j] =  list[j], list[i]
            i += 1
            j -= 1
    #out of the loop swaping
    if i < end:
        list[i], list[end] = list[end], list[i]
    return i
            

def quicksort(list, start, end):
    """ 
    this recursive function is used to
    sort a list by quicksort method
    """
    if start < end:
        ind = indexfinder(list, start, end)
        quicksort(list, start, ind-1)
        quicksort(list, ind+1, end)
    return list

if __name__ == '__main__':
    import time as t
    import random as r
    import math as m
    for ran in [10, 100, 1000, 10000]:
        print(ran)
        rand_list = [r.randint(0,999) for ele in range(ran)]
        start = 0
        end = len(rand_list) - 1
        """print("the unsorted list is : ", rand_list)
        print("------------------------------------------------")"""
        starttime = t.time()
        sorted_list = quicksort(rand_list, start, end)
        endtime = t.time()
        """print("the sortded list is : ",sorted_list )
        print("-------------------------------------------------")"""
        totaltime = endtime - starttime
        print("the total time taken is : ", (totaltime))
        for g in [ran**2, ran**3, ran*(m.log(ran, 2))]:
            ratio = (totaltime/g)
            print(ratio)
    