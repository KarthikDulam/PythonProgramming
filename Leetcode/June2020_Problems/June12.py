""" Insert Delete GetRandom O(1) """

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data[val] = val
            return True
        else:
            return False # Element already exist
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            del self.data[val]
            return True
        else:
            return False # Element does not exist, thus cannot be deleted
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.data))
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()