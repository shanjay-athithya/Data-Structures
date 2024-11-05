"""def bubblesort(list):
    n = len(list)
    for i in range(0, len(list)-1):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
    
    print(bubblesort([9,6,4,0,1]))"""
    
"""def insertionsort(list):
    for i in range(1,len(list)):
        a = list[i]
        j = i -1
        while j>=0 and  a < list[j]:
            list[j +1] = list[j]
            j -= 1
        list[j+1] = a
    return list
print(insertionsort([9,6,4,0,1]))"""

"""def selectionsort(list):
    n = len(list)
    for i in range(n):
        min = i
        for j in range(i +1,n ):
            if list[min]> list[j]:  
                min = j
        list[i], list[min] = list[min], list[i]
    return list 
print(selectionsort([9,6,4,0,1]))"""

"""def merging(l1, l2):
    l = []
    a = len(l1)
    b = len(l2)
    aind = 0
    bind = 0
    while aind < a and bind < b:
        if l1[aind] < l2[bind]:
            l.append(l1[aind])
            aind += 1
        else:
            l.append(l2[bind])
            bind += 1
    if aind < a :
        l.extend(l1[aind:])
        
    if bind < b :
        l.extend(l2[bind:])
    return l
def mergesort(list):
    n = len(list)
    if n <2:
        return list[:]
    else:
        d = n //2
        return (merging(mergesort(list[:d]), mergesort(list[d:])))
    
print(mergesort([0,7,5,3,2,1]))"""

"""def median(list,begin,end):
    mid = (begin + end )//2
    if list[begin] > list[mid]:
        list[begin], list[mid] = list[mid], list[begin]
    if list[mid] > list[end]:
        list[mid], list[end] = list[end], list[mid]
    if list[begin] > list[end]:
        list[begin], list[end] = list[end], list[begin]
    list[mid], list[end] = list[end], list[mid]
    
        

def partition(list,begin,end):
    median(list, begin, end)
    i = begin
    j = end - 1
    pivot = list[end]
    while i <= j:
        while list[i] < pivot:
            i = + 1
        while list[j] > pivot:
            j = j - 1
        if i < j :
            list[i],list[j] = list[j],list[i]
            i += 1
            j -= 1
    if i < end:
        list[i],list[end] = list[end],list[i]
    return i

        
def quicksort(list, begin, end):
    if begin < end:
        k = partition(list,begin,end)
        quicksort(list,begin,k - 1)
        quicksort(list,k + 1, end)
        
list = [1,9,8,6,3,0]
begin = 0
end = len(list) - 1

quicksort(list, begin,end)
print(list)"""