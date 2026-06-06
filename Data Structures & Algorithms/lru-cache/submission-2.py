class ListNode:
    def __init__(self, key: int,  value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: ListNode(int, int)) -> None:
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
#prev = left, nxt = right
#left.next = node:(1, 10)
#right.prev = node:(1, 10), = left -> (1, 10) <- right
#(1, 10).prev = prev:left, (1, 10).next = right
#left <-> (1, 10) <-> right
    def remove(self, node: ListNode(int, int)) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
#left <-> (1, 10) <-> (3, 30) <-> (2, 20) <-> right
#prev = left, nxt = (3, 30)


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value

        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            print(len(self.cache))
            node = self.left.next.key
            lru = self.cache[node]
            self.remove(lru)
            del self.cache[lru.key]
            print(len(self.cache))