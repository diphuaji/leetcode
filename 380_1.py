'''
380. Insert Delete GetRandom O(1)
'''
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d={}
        self._nums=[]
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._d:
            return False
        self._d[val]=len(self._nums)
        self._nums.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._d:
            self._nums[self._d[val]]=self._nums[-1]
            self._d[self._nums[-1]]=self._d[val]
            self._nums.pop()
            del self._d[val]
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self._nums[random.randint(0,len(self._nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()