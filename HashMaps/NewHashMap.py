from abc import ABC, abstractmethod

class Empty(Exception):
    pass


class BaseMap(ABC):
    """
    Abstract Base Class for a Map ADT
    All the methods are abstract and must be used by the subclass 
    so for now im just defining the ones im wanting to use
    """
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def contains(self, key):
        pass

    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __popitem__(self, key):
        pass

    @abstractmethod
    def clear(self):
        pass


class NewHashMap(BaseMap):
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
        
        def __repr__(self):
            return f"Item({self.key}, {self.value})"
    
    def __init__(self, capacity=11):
        self.capacity = capacity
        self._table = [None] * capacity
        self._size = 0

    def hash(self, key):
        return hash(key) % self.capacity
    
    def __getitem__(self, key):
        root = self.hash(key)
        item = self._table[root]
        if item:
            for element in item:
                if element.key == key:
                    return element.value
        raise KeyError(f"KeyError: {key} not found")
    
    def __setitem__(self, key, value):
        while self._size/self.capacity < 0.35:
            index = self.hash(key)
            if self._table[index] is None:
                self._table[index] = []

            for element in self._table[index]:
                if element.key == key:
                    element.value = value
                    return
            
            self._table[index].append(self._Item(key, value))
            self._size += 1
        else:
            self.resize()
    
    def resize(self):
        currentMap = self._table

        self.capacity *= 2
        self._table = [None] * self.capacity
        self._size = 0

        for slot in currentMap:
            if slot:
                for element in slot:
                    self[element.key] =  element.value

    def __delitem__(self, key):
        index = self.hash(key)
        slot = self._table[index]
        if slot:
            for item in slot:
                if item.key == key:
                    slot.remove(item)
                    self._size -= 1
                    return
        raise KeyError(f"KeyError: {key} not found")
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        for slot in self._table:
            if slot:
                for item in slot:
                    yield item.key

    def contains(self, key):
        if self[key]:
            return True
        return False
    
    def __str__(self):
        return f"{self._table}"
    
    def __popitem__(self, key):
        index = self.hash(key)
        slot = self._table[index]

        if slot:
            for element in slot:
                if element.key == key:
                    slot.remove(element)
                    return element.value, element.key
        raise KeyError(f"KeyError: {key} not found")
    
    def clear(self):
        self._table = [None] * self.capacity
        self._size = 0
        return f"Table Cleared Successfully: {self._table}"
    
    def to_dict(self):#to convert the hashmap to a dictionary for use in the movie app
        result = {}

        for key in self:
            result[key] = self[key]
        return result
    
    def from_dict(self, info):#to convert a dictionary to a hashmap for use in the movie app
        for key, value in info.items():
            self[key] = value
                    
        
    