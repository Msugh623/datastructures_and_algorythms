class Node:
    def __init__(self,data):
       self.data=data
       self.next_node=None
       
    def __repr__(self):
        return f'<Node data: {self.data} >'
    
class LinkedList: 
    
    def __init__(self, data:list=[]):
        self.head=None
        if data:
            if type(data) is list:
                self.append(data)
            else:
                raise TypeError('%s is not itterable' %type(data))
                    
        
    def is_empty(self):
        return bool(self.head==None)
    
    def size(self):
        current=self.head
        count=0
        
        while current:
            count+=1
            current=current.next_node
            
        return count
    
    def prepend(self,data):
        """
        Adds New Nodes to the head of the list
        Runtime: O(1)
        Args:
            data (Any):
        """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    
    def insert(self,data,index=0):
        """
        Inserts New Node to a position in the list
        Runtime: O(n)
        Args:
            data (Any): data to insert
            data (index): where to insert
        """
        new_node=Node(data)
        current_index=0
        
        current=self.head
        
        while current:
            if current==self.head and current_index==index:
               return self.prepend(data)
            elif current_index==index-1:
                new_node.next_node=current.next_node
                current.next_node=new_node
                return new_node
            else:
                current=current.next_node
                current_index+=1
        if index==0:
            return self.prepend(data)
        
        raise IndexError('%s is out of range'%index)
    
    def delete(self,index=-1):
        """
        deletes Node at a position in the list
        Runtime: O(n)
        Args: 
            index (int): where to delete
        """ 
        current_index=0
        
        current=self.head
        if index>=self.size()or index<0:
            raise IndexError('%s is out of range'%index)
        if index==0:
            next_node=self.head.next_node 
            self.head=next_node
            return current
        while current:
            if current_index==index-1:
                next_node=current.next_node 
                current.next_node=next_node.next_node
                return current
            else:
                current=current.next_node
                current_index+=1
              
        raise IndexError('%s is out of range'%index)
        
    def append(self,data):
        """
        Inserts New Nodes to a position in the list
        Runtime: O(n)
        Args:
            data (Any): data to insert
            data (index): where to insert
        """
        if str(type(data))=="<class 'list'>":
            for item in data:
                self.append(item)
            return
        size=self.size()
        if size==0:
            return self.prepend(data)
        self.insert(data,size)
    
    def search(self,key):
        """Finds the First Node that matches the key
            Takes O(n) time
        Args:
            key (Any):  

        Returns:
            Node:
        """
        current=self.head
    
        while current: 
            if current.data ==key:
                return current            
            else:
                current=current.next_node
        return None
    
    def find_index(self, func):
        """Finds the First Node that matches the key
            Takes O(n) time
        Args:
            key (Any):  

        Returns:
            int: index of found node
        """
        count=0
        current=self.head
    
        while current: 
            if bool(func(current.data)):
                return count            
            else:
                current=current.next_node
                count+=1
        return -1
       
    def __getitem__(self, index): 
        current_index=0
        current=self.head
        
        while current:
            if current_index==index:
               return current.data
            else:
                current=current.next_node
                current_index+=1         
        raise IndexError('%s is out of range'%index)
        
    def __repr__(self):
        
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        
        nodes=[]
        current=self.head
        
        if self.is_empty():
            return '[]'
        
        while current: 
            if current is self.head:
                nodes.append(f'[HEAD: {current.data}]')
            elif not current.next_node:
                nodes.append(f'[TAIL: {current.data}]')
            else:
                nodes.append(f'[{current.data}]')
                            
            current=current.next_node
        return ' -> '.join(nodes)
