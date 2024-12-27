from abc import ABC, abstractmethod


class Empty(Exception):
    pass

class BaseMap(ABC):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __contains__(self, key):
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
    def __iter__(self):
        pass

    @abstractmethod
    def keys(self):
        pass

    @abstractmethod
    def values(self):
        pass

    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def get(self, key, default=None):
        pass

    @abstractmethod
    def pop(self, key, default=None):
        pass

    @abstractmethod
    def popitem(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def update(self, other):
        pass

    @abstractmethod
    def setdefault(self, key, default=None):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __bool__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __reversed__(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

class HashMap(BaseMap):
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = {}
    
    def __getitem__(self, key):
        if key in self.table:
            return self.table[key]
        raise KeyError(f'Key Error {repr(key)}')
    
    def __setitem__(self, key, value):
        
        if key in self.table:
            self.table[key] = value
        else:
            self.table[key] = value
        
    def __delitem__(self, key):
        if key in self.table:  # if we find a value in the table with this Key
            del self.table[key]
            return
        raise KeyError(f'Key Error {repr(key)}')
    
    def __len__(self):
        return len(self.table)
    
    def __iter__(self):
        yield from self.table

    def is_empty(self):
        return len(self.table) == 0
