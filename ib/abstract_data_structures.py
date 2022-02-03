class abstract():
    class VirtualEmptySpace():
        def __repr__(self):
            return ' '
    #End Nothing
    
    @classmethod
    @property
    def null(cls):
        return cls.VirtualEmptySpace()
    
    @classmethod
    @property
    def nothing(cls):
        return cls.null
#End class abstract

class Array():
    """This a Array with fixed size.
Usage:
    a1 = Array(size=10)
    
"""
    def __init__(self, size=10, default=abstract.null):
        self.items = [default for i in range(size)]
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return "Array" + str(self.items) + ''
    
    def __getitem__(self, index):
        if 0 < index >= self.lenght:
            raise IndexError(f'Index must be a value between 0 and {self.lenght-1}.')
        return self.items[index]
    
    def __setitem__(self, index, value):
        if 0 < index >= self.lenght:
            raise IndexError(f'Index must be a value between 0 and {self.lenght-1}.')
        self.items[index] = value
    
    def __iter__(self):          
        return iter(self.items)
    
    def pprint(self, indentation='\t'):
        for index, value in enumerate(self):
            print(f'{indentation}index {index}:', end=' ')
            if isinstance(value, Array):
                print("Array:")
                value.pprint(indentation+'\t')
            else:
                print(f'value: {value}')
    
    @property
    def lenght(self):
        return len(self)
    
#End class Array


class Stack_with_Fixed_Size():
    """This a Stack with fixed size.
The order in which elements come off a stack gives rise to its alternative name,
LIFO (last in, first out).

Usage:
    s1 = Stack(size=5)
    my_stack.isEmpty()
    my_stack.push(item)
    item = my_stack.pop()
"""
    def __init__(self, items=None, size=10):
        if isinstance(items, list):
            self.items = items
        else:
            self.items = list()
            for i in range(size):
                self.items.append(abstract.null)
        self.size = size
        self.index = -1
    
    def push(self, item):
        """Example:
    my_stack = Stack(size=5)
    my_stack.push(item)
"""
        if self.index >= self.size - 1:
            raise IndexError(f'This Stack has a limit size of {self.size}.')
        self.index = self.index + 1
        self.items[self.index] = item
    
    def pop(self):
        """Return the next item in the Stack:
    my_stack = Stack(size=5)
    my_stack.push(item)
    item = my_stack.pop()
"""
        if self.index < 0:
            raise IndexError(f'This Stack is empty.')
        item = self.items[self.index]
        self.items[self.index] = abstract.null
        self.index = self.index - 1
        return item
    def peek(self):
        """Example:
    my_stack = Stack(size=5)
    my_stack.peek() # not available on IB
"""
        if not self.isEmpty():
            return self.items[self.index]
    
    def isFull(self):
        """Returns True if is Full or False otherwise:
    my_stack = Stack(size=5)
    my_stack.isFull() # not available on IB
"""
        return (self.index+1 >= self.size)
    
    def isEmpty(self):
        """Returns True if is Empty or False otherwise:
    my_stack = Stack(size=5)
    my_stack.isEmpty()
"""
        return (self.index < 0)
    
    @property
    def length(self):
        return self.index+1
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return "Stack(" + str(self.items) + ')'
#End class Stack_with_Fixed_Size


class Stack_with_Any_Size():
    def __init__(self, items=None):
        if isinstance(items, list):
            self.items = items
        else:
            self.items = list()
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.length == 0
    
    @property
    def length(self):
        return len(self.items)
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return "Stack(" + str(self.items) + ')'
#End class Stack_with_Any_Size


class Stack(Stack_with_Fixed_Size):
    pass
#End class Stack


class Queue_with_Fixed_Size():
    def __init__(self, items=None, size=10):
        if isinstance(items, list):
            self.items = items
        else:
            self.items = list()
            for i in range(size):
                self.items.append(abstract.null)
        self.size = size
        self.index = -1
        
    def enqueue(self, item):
        if self.index >= self.size - 1:
            raise IndexError(f'This Queue has a limit size of {self.size}.')
        self.index = self.index + 1
        self.items[self.index] = item
        
    def dequeue(self):
        if self.index < 0:
            raise IndexError(f'This Queue is empty.')
        item = self.items[0]
        for i in range(self.index+1):
            self.items[i] = self.items[i+1]
        self.items[self.index] = abstract.null
        self.index = self.index - 1
        return item
    
    def isEmpty(self):
        return self.length == 0
    
    @property
    def length(self):
        return self.index+1
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return "Queue(" + str(self.items) + ')'
#End class Queue_with_Fixed_Size


class Queue_with_Any_Size():
    def __init__(self, items=None):
        if isinstance(items, list):
            self.items = items
        else:
            self.items = list()
            
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.length<1:
            raise IndexError(f'This Queue is empty.')
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.length == 0
    
    @property
    def length(self):
        return len(self.items)
    
    def __repr__(self):
        return "Queue(" + str(self.items) + ')'
#End class Queue_with_Any_Size


class Queue(Queue_with_Fixed_Size):
    pass
#End class Queue


# Linked List
"""
https://realpython.com/linked-lists-python/#implementing-your-own-linked-list
https://towardsdatascience.com/python-linked-lists-c3622205da81
"""
class Node():
    def __init__(self, value, next_node=abstract.null, prev_node=abstract.null):
        self.value = value
        self.next = next_node
        self.prev = prev_node
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'Node({self.value})'
#End class Node


class SingleLinkedList():   
    def __init__(self, values=abstract.null):
        self.head = abstract.null
        self.tail = abstract.null
        self.value = abstract.null
        if type(values) != type(abstract.null):
            self.add_multiple_nodes(values)
    
    def __repr__(self):
        nodes = []
        node = self.head
        while type(node) != type(abstract.null):
            nodes.append(str(node))
            node = node.next
        return "LinkedList(" + str(nodes) + ')'
    
    def __str__(self):
        nodes = []
        node = self.head
        while type(node) != type(abstract.null):
            nodes.append(str(node))
            node = node.next
        nodes.append('null')
        return ' -> '.join(nodes)
    
    def __len__(self):
        count = 0
        node = self.head
        while type(node) != type(abstract.null):
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    @property
    def length(self):
        return len(self)
    
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_node(self, value):
        if type(self.head) == type(abstract.null):
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
#End class LinkedList


class DoublyLinkedList(SingleLinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self
    
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head
    
#End class DoublyLinkedList


class CircularLinkedList(SingleLinkedList):
    pass
#End class CircularLinkedList


class LinkedList(SingleLinkedList):
    pass
#End class CircularLinkedList


def test_Stack():
    print("Testing Stack")
    s1 = Stack(size=5)
    i = 0
    while not s1.isFull():
        s1.push(i)
        print(i, s1, s1.isFull())
        i = i + 1 

    while not s1.isEmpty():
        i = s1.pop()
        print(i, s1, s1.isEmpty())
    return s1
#end def test_Stack


def test_Queue():
    print("Testing Queue")
    q1 = Queue(5)
    for i in range(5):
        q1.enqueue(chr(ord("A")+i))
    while not q1.isEmpty():
        print(q1, end=" ")
        item = q1.dequeue()
        print(item)
    return q1
#end def test_Queue


def test_LinkedList():
    print("Testing Linked List")
    l1 = LinkedList()
    for i in range(5):
        l1.add_node(chr(ord("A")+i))
        print(l1)
    return l1
#end def test_Queue


def test_Array():
    print("Testing Array")
    a1 = Array(10, 0)
    a1.pprint()
    return a1
#end def test_Array

def test_Array2D():
    print("Testing Array")
    a2 = Array(5, Array(2, 0))
    a2.pprint()
    return a2
#end def test_Array

if __name__ == '__main__':
    #s1 = test_Stack()
    #q1 = test_Queue()
    #l1 = test_LinkedList()
    #a1 = test_Array()
    #a2 = test_Array2D()
    pass
#end if main
