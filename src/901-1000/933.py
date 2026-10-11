# 933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.queue = Queue(16, True)
        pass        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue.peek() < t - 3000:
            self.queue.pop()
        return len(self.queue)        
    
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
    
class Queue:
    """
    A queue implemented using a circular cyclic list
    """
    
    def __init__(self, cap: int, resizeable: bool = False, initial_elems: list[int] | None = None):
        self.__array: list[int] = [None] * cap
        self.start:  int = 0
        self.length: int = 0
        self.cap:    int = cap
        self.is_resizeable: bool = resizeable
        
        if initial_elems != None:
            for elem in initial_elems:
                self.append(elem)
                
    def __str__(self):
        return self.__array[:self.length]
    
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        for i in range(len(self)):
            index = (self.start + i) % self.cap
            yield self.__array[index]
    
    def __len__(self):
        return self.length
    
    def _check_if_resize(self):
        if self.length >= self.cap:
            self._resize(self.cap << 1)
            if not self.is_resizeable: raise RuntimeError(f"Cannot insert new item into Stack as stack is full")
    
    def _resize(self, new_cap: int):
        if self.length > new_cap: raise ValueError(f"new cap of array of new size {new_cap} cannot be less than existing size of {self.length}")
        # create new array, copy elements over 
        # set start to 0 as we do a full iteration
        arr = [None] * new_cap 
        for i, elem in enumerate(self):
            arr[i] = elem
        self.__array = arr
        self.start = 0
        self.cap = new_cap
    
    def peek(self) -> int:
        return self.__array[self.start]
    
    # methods which polymorphically mirror python's inbuilt list methods
    
    def pop(self) -> int:
        ret = self.peek()
        self.__array[self.start] = None
        self.start = (self.start + 1) % self.cap
        self.length -= 1
        return ret
    
    def append(self, item: int) -> None:
        # resize if need be
        self._check_if_resize()
            
        # insert
        insert_index = (self.start + self.length) % self.cap
        self.__array[insert_index] = item
        self.length += 1


