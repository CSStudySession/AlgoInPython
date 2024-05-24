from collections import OrderedDict

class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MaxStack:

    def __init__(self):
        self.orderedDict = OrderedDict()                # int_val -> list of Nodes with same int val
        self.tailNode = Node()
        self.headNode = Node()
        self.tailNode.next = self.headNode
        self.headNode.prev = self.tailNode

    def push(self, x: int) -> None:
        curNode = Node(x)
        self.headNode.prev.next = curNode
        curNode.next = self.headNode
        curNode.prev = self.headNode.prev
        self.headNode.prev = curNode

        if x in self.orderedDict:
            self.orderedDict[x].append(curNode)
        else:
            self.orderedDict[x] = [curNode]

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def peekMax(self) -> int:
        pass

    def popMax(self) -> int:
        pass


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()