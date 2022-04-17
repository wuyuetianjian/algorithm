class MyCircularDeque:

    def __init__(self, k: int):
        self.li = []
        self.k = k


    def insertFront(self, value: int) -> bool:
        m = [value] + self.li
        if len(m) <= self.k:
            self.li = m
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        m = self.li + [value]
        if len(m) <= self.k:
            self.li = m
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.li == []:
            return False
        else:
            self.li.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.li == []:
            return False
        else:
            # print(self.li)
            self.li.pop(-1)
            return True

    def getFront(self) -> int:
        if self.li == []:
            return -1
        else:
            return self.li[0]

    def getRear(self) -> int:
        print(self.li)
        if self.li == []:
            return -1
        else:
            return self.li[-1]

    def isEmpty(self) -> bool:
        if self.li == []:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.li) >= self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()