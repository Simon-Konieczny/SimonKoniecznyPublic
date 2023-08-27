class LinkedNode:

    def __init__(self, data=None, next= None):
        self._data = data
        if next is None or isinstance(next, LinkedNode):
            self._next = next
        else:
            raise TypeError('Node type object expected!')
        

    def __str__(self):
        """
        Note, this is a recursive method (implicit via str()). As you can see
        recursion can be used for linked data structures.
        """
        if self._data is None:
            return ''
        elif self._next is None:
            return str(self._data)
        else:
            return str(self._data) + ', ' + str(self._next)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def tail(self):
        return self._next

    @tail.setter
    def tail(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._next = node
        else:
            raise TypeError('Node type object expected!')



    def __init__(self):
        """
        1) To ensure that we can pop the element at the front efficiently,
        we must have a pointer to the front of the queue. This is done via the attribute _front

        2) To ensure that we can enqueue the element at the back efficiently,
        we must have a pointer to the back of the queue node. This is done via the attribute _back

        """
        self._front = None
        self._back = None
        self._size = 0


    def __str__(self):
        return 'LinkedQueue([' + str(self._front) +')]'


    def enqueue(self, value):
        """
        We enqueue at the back of the queue, so we must remember to mode the back of the queue to the latest addition.
        """
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._back = newnode
        else:
            # Be careful, here again the order of the statements matter
            self._back.tail = newnode 
            self._back = newnode
        self._size += 1


    def peek(self):
        if self._front is None:
            return None
        else:
            return self._front.data


    def pop(self):
        """
        We pop from the front of the queue, so we must remember to mode the front of the queue to the next element in the queue.
        """
        if self._front is None:
            raise ValueError('Cannot pop an empty queue!')
        else:
            # we need a temp variable <popped> in order to keep a reference to 
            # the first node of the stack
            popped = self._front 
            self._front = self._front.tail
            if self._front is None: # we removed the last element in the queue
                self._back = self._front
            popped.tail = None # this is optional
            self._size -= 1
            return popped.data


    def isempty(self):
        return self._size == 0

        
    def __len__(self):
        return self._size

class LinkedList:

    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0


    def __str__(self):
        if self._front is None:
            return 'LinkedList([])'
        else:
            return 'LinkedList([' + str(self._front) +'])'


    def __len__(self):
        """ 
        Rather than traversing the list from front to end, it is better to have an attribute _size
        that is updated every time we add or remove an element.
        The code below shows you how to traverse a linked list, from start to end. 
        To traverse the list, we need to use a local variable <currentnode> to move along the list, 
        we must not change/move the pointer _front.
            count = 0
            currentnode = self._front
            while currentnode is not None:
                count += 1
                currentnode = currentnode._next

        """        
        return self._size

    
    def isempty(self):
        return self._size == 0


    def append(self, value):
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode

        self._size += 1

    def pop(self):
        if self.isempty():
            raise IndexError('The list is empty.')
        
        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data

    def __getitem__(self, index):
        if index >= self._size :
            raise IndexError('list index out of range')
        
        currentnode = self._front
        for i in range(index): # move to node before index
            currentnode = currentnode.tail
        return currentnode.data


    def __setitem__(self, index, value):
        if index >= self._size :
            raise IndexError('list assignment index out of range')
        
        currentnode = self._front
        for i in range(index): # move to node before index
            currentnode = currentnode.tail
        currentnode.data = value


    def __contains__(self, key):
        if self._size == 0:
            return False

        currentnode = self._front
        while currentnode is not None:
            if currentnode.data == key:
                return True
            currentnode = currentnode.tail
        return False


    def index(self, value, start=0, stop=2147483647):
        if self._size == 0:
            raise ValueError(str(value) + ' is not in list')
        
        index = 0
        currentnode = self._front
        while currentnode is not None:
            if currentnode.data == value:
                return index
            currentnode = currentnode.tail
            index += 1
        raise ValueError(str(value) + ' is not in list')


    def insert(self, index, object):
        newnode = LinkedNode(object)
        if self._size == 0: # insert at front
            self._front = newnode
            self._tail = newnode
            self._size = 1
            return
                    
        if index == 0: # insert at front
            newnode.tail = self._front
            self._front = newnode
            self._size += 1
            return
                    
        if index >= self._size: # insert at back
            self._tail.tail = newnode
            self._tail = newnode
            self._size += 1
            return

        currentnode = self._front
        for i in range(index-1): # move to node before index
            currentnode = currentnode.tail
        newnode.tail = currentnode.tail
        currentnode.tail = newnode
        self._size += 1

    def remove(self, value):
        if self._size == 0:
            raise ValueError(str(value) + ' is not in list')
        
        index = 0
        currentnode = self._front
        if currentnode.data == value: # removed the first element
            self._front = self._front.tail
            currentnode.tail = None
            self._size -= 1
            if self._size == 0: # removed the only element in list
                self._tail = self._front
            return

        previousnode = currentnode
        currentnode = currentnode.tail
        while currentnode is not None:
            if currentnode.data == value:
                if currentnode is self._tail: # removed the last node in the lsit
                    self._tail = previousnode
                previousnode.tail = currentnode.tail
                currentnode.tail = None
                self._size -= 1
                return
            previousnode = currentnode
            currentnode = currentnode.tail

        raise ValueError(str(value) + ' is not in list')
    
    def clear(self):
        n = self._front
        
        while n is not None:
            m = n
            n = n.tail
            m._data = None
            m.tail = None
            
mylist = LinkedList()

mylist.append(1)

print(mylist)
