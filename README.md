# new
### implement queues----- using list 

my_list=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
my_queue=[]
print(my_list)

### adding element in the queue

for i in range(0,len(my_list)):
    my_queue.append(my_list[i])
    print(my_queue)

### removing element from the stack

for i in range(0,len(my_list)):
    my_queue.pop(0)
    print(my_queue)
