from typing import collections

# Meta variant: 多实现两个接口 del(key) -> bool, last() -> int
# last()返回most recent used value if there's.
# get, put, del run O(1) average, last runs O(1)
# no capacity requiement: no limitation on capacity
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRU_cache_v1:
    def __init__(self): # 注意没有capacity限制了
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.val_to_ref = collections.defaultdict(Node)
    
    def reconnect_nodes(self, node: Node): # helper func
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def move_to_end(self, node: Node):
        before = self.tail.prev
        before.next = node
        node.prev = before

        node.next = self.tail
        self.tail.prev = node
    
    def get(self, key: int) -> int:
        if key not in self.val_to_ref:
            return -1
        cur = self.val_to_ref[key]
        val = cur.value
        self.reconnect_nodes(cur)
        self.move_to_end(cur)
        return val

    def put(self, key:int, val:int):
        if key in self.val_to_ref: # 之前存在 先删掉 再插入新的
            cur = self.val_to_ref[key]
            self.reconnect_nodes(cur)
            del self.val_to_ref[key]
        
        cur = Node(key, val)
        self.val_to_ref[key] = cur
        self.move_to_end(cur)
    
    def delelte_key(self, key:int) -> bool:
        if key not in self.val_to_ref:
            return False
        remove = self.val_to_ref[key]
        self.reconnect_nodes(remove)
        del self.val_to_ref[key]
        return True

    def last(self) -> int:
        if self.tail.prev == self.head: # cache为空
            return -1
        return self.tail.prev.value # tail之前的节点一直是most recent used one

# leetcode version
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 创建两个dummy, 一个head一个tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.dict = {} 

    def get(self, key: int) -> int:
        if key not in self.dict:          
            return -1
        else:
            node = self.dict[key] 
            self.remove(node)
            self.add(node)         
            return node.value

    def put(self, key: int, value: int) -> None:
        newnode = Node(key, value) #注意这里的处理 需要先new一个新node
        if key in self.dict: # 这里要remove oldnode, add newnode
            oldnode = self.dict[key]
            self.remove(oldnode)
            self.add(newnode)
            self.dict[key] = newnode
        else:
            self.add(newnode) #每次的add/remove dict里面都要一起
            self.dict[key] = newnode
            if len(self.dict) > self.capacity:
                toRemove = self.head.next
                self.remove(toRemove)
                del self.dict[toRemove.key]    
        
    # head -> 0 -> 1 -> tail
    #只需要用到add to tail(this is the dummy tail node)
    def add(self, node):
        tailpre = self.tail.prev
        tailpre.next = node
        node.prev = tailpre
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev