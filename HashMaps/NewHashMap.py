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
    
    