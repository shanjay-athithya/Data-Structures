def binarysearch(list, low, high, search):
    """ 
    this recursive function is used to 
    find the index of an element
    """
    #base condition
    if low > high:
        return -1
    else:
        #finding the mid index
        mid = (high + low) // 2
        #checking mid index element equal to search
        if list[mid] == search:
            return mid
        #checking mid index element less than to search
        elif list[mid] < search:
            return binarysearch(list, mid+1, high, search)
        #checking mid index element greater than to search
        elif list[mid] > search:
            return binarysearch(list, low, mid-1, search)

if __name__ == '__main__':
    list = [1,2,3,4,5,7,8]
    low = 0
    high = len(list) - 1
    ind = binarysearch(list, low, high, 8)
    print(ind)