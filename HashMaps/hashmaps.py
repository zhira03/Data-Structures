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


class HashMap(BaseMap):
    class _Item:
        """
        A class used to represent an item in a hash map.
        Attributes
        ----------
        key : any
            The key associated with the item.
        value : any
            The value associated with the item.
        Methods
        -------
        __init__(self, key, value):
            Initializes the _Item with a key and a value.
        """
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = {}
    
    def __getitem__(self, key):
        """
        Retrieve the value associated with the given key from the hash map.
        Parameters:
        key (any): The key to look up in the hash map.
        Returns:
        any: The value associated with the given key.
        Raises:
        KeyError: If the key is not found in the hash map.
        """
        if key in self.table:
            return self.table[key]
        raise KeyError(f'Key Error {repr(key)}')
    
    def __setitem__(self, key, value):  # can be used to add or update a value/key pair
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
    
    def contains(self, key):
        return key in self.table
    
    def __str__(self):
            items = '\n '.join(f'{key}: {value}' for key, value in sorted(self.table.items()))
            return f'{{{items}}}'
    
    def __popitem__(self, key):
        """
        Remove the item with the specified key from the hash map and return it.
        Args:
            key: The key of the item to be removed.
        Returns:
            A tuple containing the value associated with the key and the key itself.
        Raises:
            KeyError: If the key is not found in the hash map.
        """
        if key in self.table:
            value = self.table[key]
            self.table.__delitem__(key)
            return value,key
        
        raise KeyError(f'Key Error {repr(key)}')
    
    def clear(self):
        self.table.clear()
