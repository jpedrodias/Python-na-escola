__version__ = 0.2 # 2022/11/09

class Abstract():
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
    a2 = Array(items=[1, 2, 3])"""
    def __init__(self, items=10, default=Abstract.null):
        if isinstance(items, int):
            self.items = [default for i in range(items)]
        elif isinstance(items, list):
            self.items = items
        else:
            self.items = list()
    
    def __len__(self):
        return len(self.items)
    
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
    
    def __repr__(self):
        return f'Array({self.items})'
#End class Array


class Collection():
    """Collection store a ser of elemets of any type
A collection is like a linked-list, but the order of elements is not guaranteed so you can’t use .get(x) or .size() etc.
- .resetNext() → start at the beginning
- .addItem( data ) → add data item to the collection
- .hasNext() → tells whether there is another item in the list
- .getNext() → retrieves a data item from the collection
- .isEmpty() → check whether collection is empty"""
    
    def __init__(self, items=None):
        if isinstance(items, list):
            self.items = items
        else:
            self.items = list()
        self.index = 0
    
    def addItem(self, value):
        self.items.append(value)
    
    def getNext(self):
        if self.index>=len(self.items):
            raise IndexError('Collection has no more values')
        value = self.items[self.index]
        self.index = self.index + 1
        return value
    
    def hasNext(self):
        return len(self.items)>self.index
    
    def resetNext(self):
        self.index = 0
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        return f'Collection({self.items})'
#End class Collection
    

class Stack_with_Fixed_Size():
    """This a Stack with fixed size.
The order in which elements come off a stack gives rise to its alternative name,
LIFO (last in, first out).
- .push(data) → Adds an element to the end
- .pop()      → removes and returns the last item
- .isEmpty() → check whether Stack is empty

Usage:
    s1 = Stack(5)
    my_stack.isEmpty()
    my_stack.push(item)
    item = my_stack.pop()"""
    
    def __init__(self, items=10, default=Abstract.null):
        if isinstance(items, int):
            self.items = [default for i in range(items)]
        elif isinstance(items, list):
            self.items = items
        else:
            self.items = list()
        
        self.size = len(self.items)
        self.index = -1
    
    def push(self, item):
        if self.index >= self.size - 1:
            raise IndexError(f'This Stack has a limit size of {self.size}.')
        self.index = self.index + 1
        self.items[self.index] = item
    
    def pop(self):       
        if self.index < 0:
            raise IndexError(f'This Stack is empty.')
        item = self.items[self.index]
        self.items[self.index] = Abstract.null
        self.index = self.index - 1
        return item
    def peek(self):
        # not available on IB
        if not self.isEmpty():
            return self.items[self.index]
    
    def isFull(self):
        # not available on IB
        return (self.index+1 >= self.size)
    
    def isEmpty(self):
        return (self.index < 0)
    
    @property
    def length(self):
        return self.index+1
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return f'Stack({self.items})'
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
        return f'Stack({self.items})'
#End class Stack_with_Any_Size


class Stack(Stack_with_Fixed_Size):
    def __init__(self, items=10):
        super().__init__(items)
#End class Stack


class Queue_with_Fixed_Size():
    def __init__(self, items=10, default=Abstract.null):
        if isinstance(items, int):
            self.items = [default for i in range(items)]
        elif isinstance(items, list):
            self.items = items
        else:
            self.items = list()

        self.size = len(self.items)
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
        for i in range(self.index):
            self.items[i] = self.items[i+1]
        self.items[self.index] = Abstract.null
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
        return f'Queue({self.items})'
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
        return f'Queue({self.items})'
#End class Queue_with_Any_Size


class Queue(Queue_with_Fixed_Size):
    def __init__(self, items=10):
        super().__init__(items)
#End class Queue


# Linked List
#https://realpython.com/linked-lists-python/#implementing-your-own-linked-list
#https://towardsdatascience.com/python-linked-lists-c3622205da81
class Node():
    def __init__(self, value, next_node=Abstract.null, prev_node=Abstract.null):
        self.value = value
        self.next = next_node
        self.prev = prev_node
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'Node({self.value})'
#End class Node


class SingleLinkedList():   
    def __init__(self, values=Abstract.null):
        self.head = Abstract.null
        self.tail = Abstract.null
        self.value = Abstract.null
        if type(values) != type(Abstract.null):
            self.add_multiple_nodes(values)
    
    def __repr__(self):
        nodes = []
        node = self.head
        while type(node) != type(Abstract.null):
            nodes.append(str(node))
            node = node.next
        return "LinkedList(" + str(nodes) + ')'
    
    def __str__(self):
        nodes = []
        node = self.head
        while type(node) != type(Abstract.null):
            nodes.append(str(node))
            node = node.next
        nodes.append('null')
        return ' -> '.join(nodes)
    
    def __len__(self):
        count = 0
        node = self.head
        while type(node) != type(Abstract.null):
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
        if type(self.head) == type(Abstract.null):
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
    def __init__(self, values=Abstract.null):
        super().__init__(values)
        
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
    def __init__(self, values=Abstract.null):
        super().__init__(values)
#End class CircularLinkedList


class LinkedList(SingleLinkedList):
    def __init__(self, values=Abstract.null):
        super().__init__(values)
#End class CircularLinkedList



class BinaryTree:
    class Node:
        def __init__(self, value=None):
            self.left = None
            self.right = None
            self.value = value
           
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return 
        
        node = self.root
        while node:
            if value < node.value: 
                if node.left is not None:
                    node = node.left
                else:
                    node.left = self.Node(value)
                    node = None
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = self.Node(value)
                    node = None
        #End while
    #end insert
    
    def get_depth(self):
        return self._get_in_depth(self.root)
        
    def _get_in_depth(self, branch=None):
        if branch is None:
            return 0
        return 1 + max(self._get_in_depth(branch.left),
                       self._get_in_depth(branch.right))

    def get_width(self):
        width = 0
        nodes = [self.root] # start from the top
        while nodes:
            width = max(width, len(nodes))
            branchs = []
            for node in nodes:
                if node.left: branchs.append(node.left)
                if node.right: branchs.append(node.right)
            nodes = branchs
        return width
#End of class






def test_Stack():
    print("Testing Stack")
    s1 = Stack(5)
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

def test_Collection():
    print("Testing Collection")
    c1 = Collection()
    for i in range(5):
        c1.addItem(f'item{i+1}')
        print(c1)
    
    while c1.hasNext():
        value = c1.getNext()
        print(value)
    
if __name__ == '__main__':
    #s1 = test_Stack()
    #q1 = test_Queue()
    #l1 = test_LinkedList()
    #a1 = test_Array()
    #a2 = test_Array2D()
    #c1 = test_Collection()
    pass
#end if main