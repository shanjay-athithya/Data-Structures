from stack import Stack

def infixtopostfix(name):
    prece = {'+': 4, '-': 4, '*' : 3, '/' : 3, '**' : 2, '(' : 1 }
    s = Stack()
    post = ''
    for ch in name:
        if ch.isalnum():
            post = post + ch
        
        elif ch == '(':
            s.push(ch)
            
        elif ch == ')':
            while s.seq[-1] != '(':
                c = s.pop()
                post = post + c
            if s.seq[-1] == '(':
                s.pop()
        
        elif ch in ['+', '-', '*', '/', '**']:
            if s.isempty():
                s.push(ch)
            else:
                while not s.isempty() and prece[ch] <= prece[s.seq[-1]]:
                    post = post + s.pop()
                s.push(ch)
        
    while not s.isempty():
        post = post + s.pop()
        
    return post



def postsolve(post):
    stack = Stack()
    for ch in post:
        if ch.isalnum():
            stack.push(int(ch))
        elif ch in ['+', '-', '*', '/', '**']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(ch, operand1, operand2)
            stack.push(result)

    return stack.pop()

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '**':
        return operand1 ** operand2
    
if __name__ == '__main__':
    post = infixtopostfix("(5 * (((9 + 8) * (4 * 6)) + 7))")
    print(post)
    result = postsolve(post)
    print("Result:", result)
    
    post = infixtopostfix("6 * (5 + (2 + 3) * 8 + 3)")
    print(post)
    result = postsolve(post)
    print("Result:", result)
    
    post = infixtopostfix("a + b * c + (d * e + f) * g")
    print(post)
    """result = postsolve(post)
    print("Result:", result)"""
