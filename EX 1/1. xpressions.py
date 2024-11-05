#defining a fuction to find the expressions satisfied with the values
def correct_expression():
    #getting input from user for the values of a , b and c
    value_a = int(input("enter the value of a : "))
    value_b = int(input("enter the value of b : "))
    value_c = int(input("enter the value of c : "))
    #using the below statement to make the output user understand 
    print("The expression satisfied by the values are : ")
    c=0
    #checking whether the values satisfy the expression "a + b = c"
    if value_a + value_b == value_c:
        print("a + b = c")
        c+=1
    #checking whether the values satisfy the expression "a = b - c"
    if value_a == value_b - value_c:
        print("a = b - c")
        c+=1
    #checking whether the values satisfy the expression "a * b = c"
    if value_a * value_b == value_c:
        print("a * b = c")
        c+=1
    #checking whether the values satisfy the expression "a % b = c"
    if value_a % value_b == value_c:
        print("a % b = c")
        c+=1
    #checking whether the values satisfy the expression "a / b = c"
    if value_a / value_b == value_c:
        print("a / b = c")
        c+=1
    #checking whether the values satisfy the expression "a // b = c"
    if value_a // value_b == value_c:
        print("a // b = c")
        c+=1
    #checking whether the values satisfy the expression "a ** b = c"
    if value_a ** value_b == value_c:
        print("a ** b = c")
        c+=1
    #checking whether the values satisfy the expression "a = b + c"
    if value_a == value_b + value_c:
        print("a = b + c")
        c+=1
    #checking whether the values satisfy the expression "a - b = c"
    if value_a - value_b == value_c:
        print("a - b = c")
        c+=1
    #checking whether the values satisfy the expression "a = b * c"
    if value_a == value_b * value_c:
        print("a = b * c")
        c+=1
    #checking whether the values satisfy the expression "a = b % c"
    if value_a == value_b % value_c:
        print("a = b % c")
        c+=1
    #checking whether the values satisfy the expression "a = b / c"
    if value_a == value_b / value_c:
        print("a = b / c")
        c+=1
    #checking whether the values satisfy the expression "a = b // c"
    if value_a == value_b // value_c:
        print("a = b // c")
        c+=1
    #checking whether the values satisfy the expression "a = b ** c"
    if value_a == value_b ** value_c:
        print("a = b ** c")
        c+=1
    if c == 0:
        print("No expression")
if __name__ == "__main__":
    #calling the defined function of checking the satisfaction of expressions by the values
    correct_expression()