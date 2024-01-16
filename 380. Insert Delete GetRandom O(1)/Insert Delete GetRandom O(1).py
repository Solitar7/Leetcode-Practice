import random

class RandomizedSet:

    def __init__(self):
        self.rs = set()

    def insert(self, val: int) -> bool:
        if val in self.rs:
            return False
        self.rs.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.rs:
            self.rs.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return list(self.rs)[int(random.random()*len(self.rs))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
