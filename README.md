# abstract_data_structures.py

## Array
```python
from abstract_data_structures import Array

#my_array = Array(size=10, default=0)
my_array = Array()

for i in range(10):
    my_array[i] = i+1
print(my_array)
```
Special helpper: `my_array.pprint()`

## STACK is LIFO
methods: push, pop and isEmpty
```python
from abstract_data_structures import Stack

my_stack = Stack(size=10)
 
for i in range(10):
  my_stack.push(chr(ord("A")+i))

while not my_stack.isEmpty():
    value = my_stack.pop()
    print(value)
```


## QUEUE is FIFO
methods: enqueue, dequeue and isEmpty
```python
from abstract_data_structures import Queue

my_queue = Queue(size=10)

for i in range(10):
  my_queue.enqueue(chr(ord("A")+i))

while not my_queue.isEmpty():
  value = my_queue.dequeue()
  print(value)
```

## LinkedList
methods: add_node; property: length
```python
from abstract_data_structures import LinkedList

my_llist = LinkedList()
for i in range(10):
	my_llist.add_node(chr(ord("A")+i))
	print(my_llist)
```
