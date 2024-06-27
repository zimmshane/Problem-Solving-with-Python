
class Stack:
    def __init__(self) -> None:
        self.items=[]
        
    def is_empty(self) -> bool:
        return self.items==[]
    
    def push(self, item)->None:
        self.items.append(item)
    
    def pop(self)->None:
        self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def pop_peek(self):
        val=self.peek()
        self.pop()
        return val
    