
class SemanticError(Exception):
    pass


def scan_token():
    global lookAhead
    global pos
    if pos >= len(expression):
        lookAhead = ''
        return
    lookAhead = expression[pos]
    pos += 1

def match(expected):
    if lookAhead == expected:
        scan_token()
    else:
        raise SyntaxError(f"Expected {expected}, but found {lookAhead}")
    

def A():
    V()
    match('=')
    E()
    assembly_code.append("STORE")

def E():
    if lookAhead == '-':
        match('-')
        T()
        assembly_code.append("NEG")
    else:
        T()
    while lookAhead == '+' or lookAhead == '-':
        if lookAhead == '+':
            match('+')
            T()
            assembly_code.append("ADD")
        else:
            match('-')
            T()
            assembly_code.append("SUB")

def T():
    F()
    while lookAhead == '*' or lookAhead == '/':
        if lookAhead == '*':
            match('*')
            F()
            assembly_code.append("MUL")
        else:
            match('/')
            F()
            assembly_code.append("DIV")

def F():
    if lookAhead == '(':
        match('(')
        E()
        match(')')
    elif lookAhead.isdigit():
        C()
    elif lookAhead.isalpha():
        V()
        assembly_code.append("LOAD")
    else:
        raise SemanticError("Semantic error: Invalid statement detected .... me no understand :(")

def C():
    if lookAhead.isdigit():
        assembly_code.append(f"LIT {lookAhead}")
        match(lookAhead)
    else:
        raise SyntaxError(f"Unexpected token: {lookAhead}")
    
def V():
    #check if lookAhead is an uppercase letter

    if lookAhead.isalpha() and lookAhead.isupper():
        assembly_code.append(f"LIT {lookAhead}")
        match(lookAhead)
    else:
        raise SyntaxError(f"Unexpected token: {lookAhead}")
    
if __name__ == "__main__":
    expression = input("Enter an expression: ")
    # remove all spaces from expression
    expression = expression.replace(" ", "")
    global pos
    pos = 0
    assembly_code = []
    scan_token()
    A()
    print(assembly_code)
