#defining a functuction to find the chances of getting odd pair
def odd_pair():
    #intiatiating the no of times as zero
    no_of_times = 0
    #creating an empty list
    odd_list = []
    #getting required input list from user
    list = eval(input("enter the required list of elements : "))
    #creating for loop to get the index of element 1
    for element1 in range(len(list)):
        #creating for loop to get the index of element 2
        for element2 in range(len(list)):
            #checking whether the index are equal
            if element1 != element2:
                #checking whether the product is an odd number
                if (list[element1]*list[element2]) % 2 != 0:
                    odd_list.append((list[element1],list[element2]))
                    break
                else:
                    #incrementing the no ot times by 1
                    no_of_times += 1
                    
            else:
                continue
    #returning the final result
    if len(odd_list) == 0:
        return False
    else:
        return True
if __name__ == '__main__':
    #displaying the result from the above definied  fuctions
    print(odd_pair())


