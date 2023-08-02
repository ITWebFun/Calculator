expression = ''
should_delete_expression = False

def write_expression(text):
    global expression
    global should_delete_expression
    
    if text == '=':
        should_delete_expression = True
        
        
    if (text == '+' or text == '-' or text == '*' or text == '/') \
        and (expression[len(expression)-1] == '+' or expression[len(expression)-1] == '-' or expression[len(expression)-1] == '*' or expression[len(expression)-1] == '/' or expression[len(expression)-1] == '.'):
        expression = expression[0:len(expression)-1] + text
    else:
        if (text == '.' and expression == '') or (text == '.' and (expression[len(expression)-1] == '+' or expression[len(expression)-1] == '-' or expression[len(expression)-1] == '*' or expression[len(expression)-1] == '/')):
            expression = expression+'0'+text
        elif (text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6' or text == '7' or text == '8' or text == '9' or text == '0') and expression == '0':
            expression = expression[0:len(expression)-1] + text 
        elif len(expression) >=2 and (expression[len(expression)-1] == '0' and (expression[len(expression)-2] == '+' or expression[len(expression)-2] == '-' or expression[len(expression)-2] == '*' or expression[len(expression)-2] == '/')):
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