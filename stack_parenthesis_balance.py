from stack import Stack

def par_check(expression:str) -> bool:
    s=Stack()
    balance = True
    for char in expression:
        if char in "([{":
            s.push(char)
        if char in ")]}":
            if s.is_empty():
                balance=False
                break
            else:
                just_popped=s.peek()
                s.pop()
                if not matches(just_popped,char):
                    balance=False
                    break             
    if balance and s.is_empty():
        return True
    else: 
        return False

def matches(open,close) -> bool:
    opens="([{"
    closes=")]}"
    return opens.index(open) == closes.index(close)

print(par_check(" ((()[{()}][])) "))