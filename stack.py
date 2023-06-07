### implement stack using array

import array as myarray

my_stack=myarray.array("i",[1,2,3,4,5,6,7,8,9,10])

### reading the Aarray/stack

for i in my_stack:
    print(i,end=" ")
print("\n")    

### inserting element in the stack

my_stack.append(11)
for i in my_stack:
    print(i,end=" ")
print("\n")    

### deleting element from the stack
### deleted
for i in range(0,len(my_stack)):
    my_stack.pop()
    for i in my_stack:
        print(i,end=" ")
    print("\n")    
