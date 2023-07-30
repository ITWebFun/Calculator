expression = ''

def write_expression(text):
    global expression
    if (text == '+' or text == '-' or text == '*' or text == '/' or text == '.') \
        and (expression[len(expression)-1] == '+' or expression[len(expression)-1] == '-' or expression[len(expression)-1] == '*' or expression[len(expression)-1] == '/' or expression[len(expression)-1] == '.'):
        expression = expression[0:len(expression)-1] + text
    else:
        expression = expression + text
        
def get_expression():
    global expression
    print(expression)
    return expression

def null_expression():
    global expression
    expression=''

def get_result_of_expression():
    global expression
    expression = str(eval(expression))
    return expression