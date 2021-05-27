from collections import defaultdict
class MyHashMap:
    def __init__(self):
        self.len = 1000
        self.table = defaultdict(list)
    def put(self, key: int, value: int) -> None:
        idx = key % self.len
        for i, elems in enumerate(self.table[idx]):
            if elems[0] == key:
                self.table[idx][i] = (key, value)
                return
        else:
            self.table[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.len
        for i, elems in enumerate(self.table[idx]):
            if elems[0] == key:
                return elems[1]
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.len
        for i, elems in enumerate(self.table[idx]):
            if elems[0] == key:
                self.table[idx].pop(i)
                return
        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)