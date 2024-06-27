class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) -> bool:
        return self.items==[]
    
    def enqueue(self,item) -> None:
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self)->int:
        return len(self.items)