class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.root, self.tail = Node(None), Node(None)
        self.k, self.len = k, 0
        self.root.next, self.root.pre = self.tail, self.tail
        self.tail.next, self.tail.pre = self.root, self.root

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new = Node(value)
        new.pre, new.next = self.root, self.root.next
        self.root.next.pre = new
        self.root.next = new
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new = Node(value)
        new.pre, new.next = self.tail.pre, self.tail
        self.tail.pre.next = new
        self.tail.pre = new
        self.len += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        tmp = self.root.next.next
        self.root.next = tmp
        tmp.pre = self.root
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        tmp = self.tail.pre.pre
        self.tail.pre = tmp
        tmp.next = self.tail
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.root.next.data

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.pre.data

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
param_1 = obj.insertFront(9)
print(param_1)
param_2 = obj.getRear()
print(param_2)
node = obj.tail
print(node.pre.data)
# obj = MyCircularDeque(3)
# param_1 = obj.insertLast(1)
# print(param_1)
# param_2 = obj.insertLast(2)
# print(param_2)
# param_3 = obj.insertFront(3)
# print(param_3)
# param_4 = obj.insertFront(4)
# print(param_4)
# param_5 = obj.getRear()
# print(param_5)
# param_6 = obj.isFull()
# print(param_6)
# param_7 = obj.deleteLast()
# print(param_7)
# param_8 = obj.insertFront(4)
# print(param_8)
# param_9 = obj.getFront()
# print(param_9)