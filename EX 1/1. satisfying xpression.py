#defining a funtion to chack for expression
def correct_expression():
    #getting input from user
    value_a=int(input("enter the value of a :"))
    value_b=int(input("enter the value of b :"))
    value_c=int(input("enter the value of c :"))
    #checking whether the values work for the 1st condition
    if value_a + value_b == value_c:
        #checking the 2nd expression
        if value_a == value_b - value_c:
            #checking the 3rd expression
            if value_a * value_b == value_c:
                print("the given numbers works for all expressions: a + b = c, a = b - c, a * b = c")
            else:
                print("the given numbers works for 1st and 2nd expressions: a + b = c and a = b - c")
        #the second condition is false so checking for 3rd condition
        else:
            if value_a * value_b == value_c:
                print("the given numbers works for 1st and 3rd expressions: a + b = c and a * b = c")
            else:
                print("the given number works only for 1st expression: a + b = c")
    #the 1st expression is not true so checking for 2nd expression
    else:
        #checking the 2nd exprssion
        if value_a == value_b - value_c:
            #checking the 3rd expression
            if value_a * value_b == value_c:
                print("the given numbers works for 2nd and 3rd expressions: a = b - c, a * b = c")
            else:
                print("the given numbers works for only expression: a = b - c")
        #the 1st and 2nd condition are false so checking for 3rd condtion
        else:
            if value_a * value_b == value_c:
                print("the given numbers works only for 3rd expression: a * b = c")
            else:
                print("the given numbers doesnt work for any expression")
                

    
correct_expression()