class LinkedNode:
    def __init__(self,data=None,next=None):
        self._data = data
        if next is None or isinstance(next,LinkedNode):
            self._next = next
        else:
            raise TypeError('Expected LinkedNode object')
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,value):
        self._data = value
        
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self,node):
        if node is None or isinstance(node,LinkedNode):
            self._next = node
        else:
            raise TypeError("Expected a LinkedNode object")

class LinkedStack:
    def __init__(self,top=None,size=0):
        self._size = size
        if top is None or isinstance(top,LinkedNode):
            self._top = top
        else:
            raise TypeError('Expected a node object')
        
    def __str__(self):
        values = []
        n = self._top
        while n is not None:
            values.append(n._data)
            n = n._next
        values = values[:-1] #to not print the None value at the end of the stack
        return (f'Linked Stack({values})')
    
    def push(self,value):
        newnode = LinkedNode(value)
        if self._top == None:
            self._top = newnode
        else:
            newnode._next = self._top
            self._top = newnode
        self._size += 1
    
    def pop(self):
        if self._top == None:
            raise ValueError('Stack is empty')
        else:
            old_top = self._top
            self._top = self._top._next
            old_top._next = None
            self._size -= 1
            return old_top._data
    
    def peek(self):
        if self._top is not None:
            return self._top._data
        else:
            raise ValueError('Stack is empty')
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self,first=None,last=None,size=0):
        if first is None or isinstance(first,LinkedNode):
            self._first = first
            self._last = last
        else:
            raise TypeError('Excpected node object')
        self._size = size
        
    def __str__(self):
        values = []
        n = self._first
        while n is not None:
            values.append(n._data)
            n = n._next
        
        return (f'LinkedQueue ({values})')
    
    def enqueue(self,value):
        newnode = LinkedNode(value)
        if self._first is  None:
            self._first = newnode
            self._last = self._first
            self._size += 1
        else:
            self._last._next = newnode
            self._last = newnode
            self._size += 1
    
    def pop(self):
        if self._first == None:
            raise ValueError('Empty queue')
        else:
            old_first = self._first
            self._first = self._first._next
            old_first._next = None
            self._size -= 1
    
    def peek(self):
        if self._first._data == None:
            raise ValueError('Empty queue')
        else:
            return self._first._data
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False