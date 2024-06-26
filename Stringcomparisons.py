import random

__TARGET='methinks it is like a weasel'
__CHAR_LIST='abcdefghijklmnopqrstuvwxyz '

def rnd_string(length:int)->str:
    random_string=""
    for i in range(length):
        random_string+=random.choice(__CHAR_LIST)
    return random_string

def scoring(random:str)->int:
    score=0
    for i in range(len(random)):
        if random[i] == __TARGET[i]:
            score+=1 
    return score

random.seed()
best_string=""
best_score=0
for i in range(10):
    str_proccessing=rnd_string(27)
    score_proccessing=scoring(str_proccessing)
    if score_proccessing > best_score:
        best_score=score_proccessing
        best_string=str_proccessing
print("After 1000 iterations\nThe best scoring string was \"%s\"\nwith %i characters in common with \"%s\"" %(best_string,best_score,__TARGET))
