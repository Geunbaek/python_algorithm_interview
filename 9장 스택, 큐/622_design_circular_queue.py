class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [None for _ in range(k)]
        self.left = 0
        self.right = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.right] = value
        self.right += 1
        self.right %= self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.left] = None
        self.left += 1
        self.left %= self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.right-1]

    def isEmpty(self) -> bool:
        return  self.left == self.right and self.arr[self.left] == None

    def isFull(self) -> bool:
        return self.left == self.right and self.arr[self.left] != None

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
print(param_1)
print(obj.arr)
param_2 = obj.enQueue(2)
print(param_2)
print(obj.arr)
param_3 = obj.enQueue(3)
print(param_3)
print(obj.arr)
param_4 = obj.enQueue(4)
print(param_4)
print(obj.arr)
param_7 = obj.Rear()
print(param_7)
param_9 = obj.isFull()
print(param_9)
param_5 = obj.deQueue()
print(param_5)
param_6 = obj.enQueue(4)
print(param_6)
param_8 = obj.Rear()
print(param_8)
