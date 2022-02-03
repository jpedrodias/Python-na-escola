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
