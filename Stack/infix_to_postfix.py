from stack import Stack

def infix_to_postfix(expression:str)->str:
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    op_stack=Stack()
    output=[]
    expression_list=expression.split()
    print(expression_list)
    for item in expression_list:
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            output.append(item)
        elif item =="(":
            op_stack.push(item)
        elif item ==")":
            hold_item=op_stack.pop_peek()
            while hold_item != "(":
                output.append(hold_item)
                hold_item=op_stack.pop_peek()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[item]):
                output.append(op_stack.pop_peek())
            op_stack.push(item)
            
    while not op_stack.is_empty():
        output.append(op_stack.pop_peek())
    return " ".join(output)

print(infix_to_postfix("( ( ( A + B ) * D ) / A )"))