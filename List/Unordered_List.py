class Node:
    def __init__(self, initial_data):
        self.data=initial_data
        self.next=None
    def set_data(self,update_data):
        self.data=update_data
    def get_data(self):
        return self.data
    def set_next(self,new_next):
        self.next=new_next
    def get_next(self):
        return self.next

class Unordered_List:
    def __init__(self) -> None:
        self.head=None
        self.length=0
    def is_empty(self)->bool:
        return self.head == None
    def add(self,item)->None:
        temp=Node(item)
        temp.set_next(self.head)
        self.head=temp
        self.length+=1
    def size(self)->int:
        return self.length
    
    def search(self,item)->bool:   
        current_node=self.head
        found=False
        while current_node.next != None and not found:
            if(current_node.get_data()==item):
                found=True
            else:
                current_node=current_node.get_next()
        return found
    
    def remove(self,item):
        previous_node=None
        current_node=self.head
        found=False
        while (current_node.get_next() != None) and (not found):
            if (current_node.data==item):
                found=True
            else:
                previous_node=current_node
                current_node=current_node.get_next()
        if found:
            if previous_node != None:
                previous_node.set_next(current_node.get_next())
                self.length-=1
                del current_node
            else: #We are removing the first item
                self.head=current_node.get_next()
                self.length-=1
    def append(self,item):
        if self.size() == 0:
            self.head=Node(item)
            self.length = 1
        else:
            next=self.head
            self.head=Node(item)
            self.head.set_next(next)
            self.length += 1
        
hash