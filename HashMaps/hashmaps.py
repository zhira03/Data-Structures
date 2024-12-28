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
    def __iter__(self):
        pass
    @abstractmethod
    def __str__(self):
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
    
    def __str__(self):
            items = '\n '.join(f'{key}: {value}' for key, value in sorted(self.table.items()))
            return f'{{{items}}}'