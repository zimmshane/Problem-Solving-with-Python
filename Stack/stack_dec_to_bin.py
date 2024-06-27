from stack import Stack

def base_conversion(num:int,base:int)-> str:
    digits = "0123456789ABCDEF"
    remainers=Stack()
    while num > 0:
        remainers.push(num%base)
        num=num//base
    output_str=""
    while not remainers.is_empty():
         output_str=output_str + digits[remainers.pop_peek()] #this uses int from the stack as the index of the char from 'digits' we want. Clever!
    return output_str


dec_num=int(input("Input a decimal number: "))
base=int(input("Input base to convert to: "))
print(dec_num, "is", base_conversion(dec_num,base), "in base", base)