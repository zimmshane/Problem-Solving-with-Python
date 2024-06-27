from stack import Stack

s=Stack()
text="This is stupid!"
print(text)
reversed=""
for char in text:
    s.push(char)
for k in range(s.size()):
    reversed+="".join(s.peek())
    s.pop()
print(reversed)