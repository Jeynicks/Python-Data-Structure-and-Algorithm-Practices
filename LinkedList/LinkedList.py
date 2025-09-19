from Node import Node

class LinkedList:
    """Linked List Methods"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        """Append Value to the end of the Linked List"""
        new_node = Node(value)
        
        if self.head is None:
            # Create Node if None
            self.head = self.tail = new_node
            
        else:
            # append value 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def extend(self, iterable: iter):
        """Append iterables to the end of the Linked List"""
        if isinstance(iterable, dict):
            iterable = iterable.items()
            
        for element in iterable:
            self.append(element)
            
    def insert(self, index: int, value):
        """Insert Value to Index"""       
        if not isinstance(index, int):
            raise TypeError('Index should be an integer')
        
        
        if index < 0:
            raise ValueError('Index should be greater than 0')
        
        new_node = Node(value)
         
        if index == 0:
            # If index is 0 we assign it to the head
            if self.head:
                self.head.prev = new_node
                new_node.next = self.head
                
            self.head = new_node
            return
        
        # if it's not 0 we traverse
        current = self.head
        i = 0
        
        # loop ends if current is none and/or index is found
        while current and i < index:    
            current = current.next
            i += 1
            
            if current is None:
                raise IndexError('Index out of range')
            
        
        # insert the new node after index is found    
        prev_node = current.prev
        prev_node.next = new_node
            
        new_node.prev = prev_node
        new_node.next = current
            
        current.prev = new_node                       
    
    def insert_iter(self, index, iterable):
        """Insert an Iterable as a seperate element"""
        if index < 0:
            raise ValueError("Index must be >= 0")
        
        if isinstance(iterable, dict):
            iterable = iterable.items()

        if index == 0:
            for element in reversed(iterable):
                new_node = Node(element)
                if self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                else:
                    self.tail = new_node
                self.head = new_node
            return

        # Traverse once to find the node at the target index
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1

        if current is None and i != index:
            raise IndexError("Index out of range")

        # Insert elements before 'current'
        prev_node = current.prev if current else self.tail
        for element in iterable:
            new_node = Node(element)
            prev_node.next = new_node
            new_node.prev = prev_node
            if current:
                new_node.next = current
                current.prev = new_node
            else:
                self.tail = new_node
            prev_node = new_node
    
    def remove(self, target_value):
        """Removes the first occurence of an element in the Linked List"""
        
        current = self.head
        while current:
            
            if current.value == target_value:
                
                # removing first element
                if current.prev is None:
                    self.head = current.next
            
                # removing last element
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                # removing from the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    
                return
                
            current = current.next
            
        raise ValueError(f"{target_value} not found in Linked List")            
            
        
    def pop(self, index: int):
        
        if index < 0:
            raise ValueError('Index should be >= 0')
        
        if not isinstance(index, int):
            raise TypeError('Index should be an integer')
        
        if self.head is None:
            raise IndexError('Trying to pop from an empty list')
        
        
        # pop first element 
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None    
            
            return value
        
        
        # traverse through elements
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
            
            if current is None:
                raise IndexError('Index out of range')         
        
        # pop if the target is the last index
        if current.next is None:
            self.tail = current.prev
            self.tail.next = None
            return current.value
        
        # pop if the target is in the middle 
        current.prev.next = current.next
        current.next.prev = current.prev
        
        return current.value
        
    def clear(self):
        """ Clears all the element from the Linked List"""
        
        current = self.head
        while current:
              
            nxt = current.next
            current.next = None
            current.prev = None
            current = nxt
        
        self.head = None
        self.tail = None    
            

            
        
                     
            
        
            
        