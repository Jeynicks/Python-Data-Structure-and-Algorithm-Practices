class Node:
    """Handle Nodes"""
    
    def __init__(self, value, next= None, prev= None):
        """Initialize Attributes"""
        self.value = value
        self.__next = next
        self.__prev = prev
        
                
    @property
    def next(self):
        """returns the value of next"""
        return self.__next
    
    @property
    def prev(self):
        """returns the value of previous"""
        return self.__prev    
    
    @next.setter
    def next(self, next):
        ""f"sets the value of next Node to {next}"""
        self.__next = next
        
    @prev.setter
    def prev(self, prev):
        ""f"sets the value of previous Node to {prev}"""
        self.__prev = prev
        
    def __str__(self):
        """returns the string of value"""
        return str(self.value)             