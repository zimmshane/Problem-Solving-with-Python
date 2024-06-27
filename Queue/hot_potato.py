from Queue import Queue

def potato_sim(name_list:list,num:int)->str:
    pass_queue=Queue()
    print("Players:", end=" ")
    for name in name_list:
        print(name, end=" ")
        pass_queue.enqueue(name)
    print()
    while pass_queue.size() > 1:
        for potato_pass in range(num):
            player=pass_queue.dequeue()
            if potato_pass == num-1:
                print(player)
            else:
                print(player,end="->")
            pass_queue.enqueue(player)
        print()
        print(pass_queue.dequeue(), "is out!")
    return pass_queue.dequeue()

print(potato_sim(["Bill", "David", "Susan", "Jane", "Kent",
"Brad"], 100),"Wins!")

    