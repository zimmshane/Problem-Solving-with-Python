from Queue import Queue
from Printer import Printer,Task
import random, time

def simulate(duration_seconds:int,pages_per_min:int,student_count:int):
    lab_printer=Printer(pages_per_min)
    print_queue=Queue()
    waiting_times=[]
    for current_second in range(duration_seconds):
        if new_print_task(student_count):
            task=Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task=print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()
    if(len(waiting_times)==0):
        average_wait=0
    else:
        average_wait=(sum(waiting_times))/(len(waiting_times))
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))
    
def new_print_task(student_count:int):
    demand=int((student_count*2)/180)
    num=random.randint(1,demand+1)
    if num==demand:
        return True
    else:
        return False
    
for i in range(10):
    simulate(duration_seconds=3600,pages_per_min=10,student_count=20)
    