class DoubleNode:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self,key,value):
        node = DoubleNode(key,value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

    def pop(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            self.tail = None
            self.head = None
            return None
        else:
            previous_tail = self.tail
            self.tail.previous.next = None
            self.tail = self.tail.previous
            return previous_tail

    def remove(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous


class LRU_Cache(object):
    def __init__(self, capacity):
        self.cache = dict({})
        self.ll = DoublyLinkedList()
        self.capacity = capacity
        self.entries = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_to_front(node)
            return node.value

    def set(self, key, value):
        if self.entries >= self.capacity:
            least_recently_used = self.ll.pop()
            self.cache.pop(least_recently_used.key,None)
            self.entries -= 1

        self.ll.prepend(key, value)
        self.cache[key] = self.ll.head
        self.entries += 1

    def move_to_front(self, node):
        self.ll.remove(node)
        self.ll.prepend(node.key, node.value)
        self.cache[node.key] = self.ll.head


def main():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))
    # returns 1
    print(our_cache.get(2))
    # returns 2
    print(our_cache.get(9))
    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))
    # returns -1 as 3 has now been removed from cache

if __name__ == "__main__":
    main()
