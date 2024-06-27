import random
class Printer:
    def __init__(self, ppm:int) -> None:
        self.page_rate=ppm
        self.current_task=None
        self.time_remaining=0
    def tick(self) -> None:
        if self.current_task != None:
            self.time_remaining=self.time_remaining-1
            if self.time_remaining == 0:
                self.current_task=None
    def start_next(self,next_task):
        self.current_task=next_task
        self.time_remaining=next_task.get_pages() * (60/self.page_rate)
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
        
class Task:
    def __init__(self,time) -> None:
        self.timestamp=time
        self.pages=random.randint(1,21)
    def get_pages(self)->int:
        return self.pages
    def get_timestamp(self):
        return self.timestamp
    def wait_time(self,current_time):
        return current_time- self.timestamp