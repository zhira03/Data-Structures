"""
used much like a dictionary but with added functionality

"""

class HashMap:
    def __init__(self) -> None:
        self.size = 64
        self.map = [None] * self.size
    
    def _get_hash(self,key):
        hash = 0
        for item in str(key):
            hash += ord(item)
        return hash % self.size
    
    def add(self,key,value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = ([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    
    def get(self,key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def get_by_value(self, value):
        result = []
        for bucket in self.map:
            if bucket is not None:
                for pair in bucket:
                    if pair[1] == value:
                        result.append(pair)
        return result if result else None
    
    def delete(self,key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for item in range(0, len(self.map[key_hash])):
            if self.map[key_hash][item][0] == key:
                self.map[key_hash].pop(item)
                return True
            
    def print(self):
        print('--------------------------------IN USE--------------------------------')
        for item in self.map:
            if item is not None:
                print(str(item))
    
myHash = HashMap()
myHash.add('tzhira8@gmail.com','Takudzwa Zhira')
myHash.add('tendai100@gmail.com','Tendai Zhira')
myHash.add('rudoZhirr@gmail.com','Takudzwa Zhira')
myHash.add('lindaRose2k@gmail.com','Zhira')
myHash.add('lillyRoads@gmail.com','Taksudzwa Zhira')
myHash.add('NaleliJoey@gmail.com','Takudzwa Zhira')

#myHash.print()

print(myHash.get_by_value("Takudzwa Zhira"))

myHash.print()

#myHash.print()
