def bruteforce(exp, sol):
    """
    This function takes two parameters:
    exp: a list of integers, representing the coefficients of a polynomial
    sol: an integer, representing the value of x for which the polynomial needs to be evaluated
    This function computes the value of the polynomial using the brute-force method, and returns
    the number of operations performed.
    """
    c = 0
    l = len(exp)
    c += 1
    result = 0
    c += 1
    #iterating the coefficients
    for i in range (l):
        c += 1
        ele = exp[i]
        #iterating the powers
        for j in range(l-i-1):
            c += 1
            ele = ele * sol
            c += 1
        result += ele
    c += 1
    #returning the number of operations performed
    return c

def horner(exp, sol):
    """
    This function takes two parameters:
    exp: a list of integers, representing the coefficients of a polynomial
    sol: an integer, representing the value of x for which the polynomial needs to be evaluated
    This function computes the value of the polynomial using the Horner's method, 
    and returns the number of operations performed.
    """
    c = 0
    n = len(exp)
    c += 1
    #assignning the coefficient of higher power
    result = exp[0]
    #iterating the coefficients
    for i in range(1, n):
        c += 1
        result = result * sol + exp[i]
        c += 1
    c += 1
    #returning the number of operations performed
    return c

c1 = 0
def power(x, pow):
    """
    This function takes two parameters:
    x: an integer, representing the base
    pow: an integer, representing the power to which x needs to be raised
    This function computes the value of x raised to the power pow using 
    the divide-and-conquer approach, and returns the result. 
    The global variable c1 is used to keep track of the number of operations performed.
    """
    global c1
    c1 += 1
    if pow == 0:
        return 1
    if pow == 1:
        return x
    #checks the number is even
    if pow % 2 == 0:
        return power(x * x, pow // 2)
    #checks the number is odd
    if pow % 2 != 0:
        return x * power(x * x, (pow - 1) // 2)
    
def divide_conquer(exp, sol):
    """ 
    This function takes two parameters:
    exp: a list of integers, representing the coefficients of a polynomial
    sol: an integer, representing the value of x for which the polynomial needs to be evaluated
    This function computes the value of the polynomial using the divide-and-conquer 
    approach with the help of the power function, and returns the number of operations performed.
    """
    global c1
    l = len(exp)
    c1 += 1
    result = 0
    #iterating the coefficients
    for i in range(l):
        c1 += 1
        result += exp[i] * power(sol, l-i-1)
        c1 += 1  
    c1 += 1
    #return the number of operations performed
    return c1
    
if __name__ == "__main__":
    """
    The main code reads the value of sol from the user and generates polynomials
    of different sizes (10, 100, 1000, 10000) with random coefficients. 
    For each polynomial, it calculates the number of operations performed by 
    each of the three functions (bruteforce, horner, and divide_conquer) and compares it with the 
    theoretical bruteforce complexity (in the order of n, n^2, n^3, and nlogn). 
    The ratios of actual bruteforce complexity to theoretical bruteforce complexity are printed 
    for each polynomial size and each function.
    """
    import random as r
    import math
    sol = int(input("enter the value of x: "))
    num_ele = [10, 100, 1000, 10000]
    #iterating the number of elements
    for num in num_ele:
        #generating random coefficients
        exp = [r.randint(0,9) for i in range(num)]
        
        print("bruteforce")
        f_1 = bruteforce(exp, sol)
        g_1 = num ** 1
        ratio_1 = f_1/g_1
        print(f"the ratio in the order of n for {num} elements is {ratio_1}")
        
        g_1 = num ** 2
        ratio_1 = f_1/g_1
        print(f"the ratio in the order of n^2 for {num} elements is {ratio_1}")
        
        g_1 = num ** 3
        ratio_1 = f_1/g_1
        print(f"the ratio in the order of n^3 for {num} elements is {ratio_1}")
        
        g_1 = num * math.log(num)
        ratio_1 = f_1/g_1
        print(f"the ratio in the order of n logn for {num} elements is {ratio_1}")
        print("--------------------")
        
        print("horner")
        f_2 = horner(exp, sol)
        g_2 = num
        ratio_2 = f_2/g_2
        print(f"the ratio in the order of n for {num} elements is {ratio_2}")
        
        g_2 = num ** 2
        ratio_2 = f_2/g_2
        print(f"the ratio in the order of n^2 for {num} elements is {ratio_2}")
        
        g_2 = num ** 3
        ratio_2 = f_2/g_2
        print(f"the ratio in the order of n^3 for {num} elements is {ratio_2}")
        
        g_2 = num * math.log(num)
        ratio_2 = f_2/g_2
        print(f"the ratio in the order of n logn for {num} elements is {ratio_2}")
        print("--------------------")
        
        print("divide_conquer")
        f_3 = divide_conquer(exp, sol)
        g_3 = num
        ratio_3 = f_3/g_3
        print(f"the ratio in the order of n for {num} elements is {ratio_3}")
        
        g_3 = num ** 2
        ratio_3 = f_3/g_3
        print(f"the ratio in the order of n^2 for {num} elements is {ratio_3}")
        
        g_3 = num ** 3
        ratio_3 = f_3/g_3
        print(f"the ratio in the order of n^3 for {num} elements is {ratio_3}")
        
        g_3 = num * math.log(num)
        ratio_3 = f_3/g_3
        print(f"the ratio in the order of n logn for {num} elements is {ratio_3}")
        print("----------------------------------------------------------------")
