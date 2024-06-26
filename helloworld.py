from random import Random

__TARGET='methinks it is like a weasel'
__CHAR_LIST='abcdefghijklmnopqrstuvwxyz '
Random.seed(342)

def string_gen(length: int) -> str:
    chars=[]
    for i in range(97,122):
        chars.append(chr(i))
    chars.append(" ")
    random_string=""
    for i in range(length):
        random_string.join(Random.choice(chars))
    return random_string

print(string_gen(27))
