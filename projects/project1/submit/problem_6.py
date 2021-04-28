class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            previous_head = self.head
            self.head = Node(value)
            self.head.next = previous_head

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        ll_set = set()
        current_node = self.head
        while current_node is not None:
            ll_set.add(current_node.value)
            current_node = current_node.next

        return ll_set

    def to_list(self):
        ll_list = list()
        current_node = self.head
        while current_node is not None:
            ll_list.append(current_node.value)
            current_node = current_node.next

        return ll_list

def iter_to_linked_list(iterable):
    ll = LinkedList()
    for item in iterable:
        ll.prepend(item)

    return ll

def union(llist_1, llist_2):
    union_set = set()
    union_set.update(llist_1.to_set())
    union_set.update(llist_2.to_set())

    return iter_to_linked_list(union_set)

def intersection(llist_1, llist_2):
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    intersection = set()

    for item in list_1:
        if item in list_2:
            intersection.add(item)

    return iter_to_linked_list(intersection)

def main():
    # Test case 1 - all ints - should work correctly

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = [3, 4, 5, 6]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("union linked_list1 & linked_list2 - should contain [6, 5, 6, 3, 2, 1]")
    print (union(linked_list_1,linked_list_2))
    print("\nintersection linked_list1 & linked_list2 - should contain [3]")
    print (intersection(linked_list_1,linked_list_2))

    # Test case 2 - include a string in data set - should work correctly

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1, 1, 2, 2, 3, 4, 5]
    element_2 = [0, 2, 3, 4, 5, 6, "a"]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nunion linked_list3 & linked_list4 - should contain [a, 6, 5, 4, 3, 2, 1, 0]")
    print (union(linked_list_3,linked_list_4))
    print("\nintersection linked_list3 & linked_list4 - should contain [5, 4, 3, 2")
    print (intersection(linked_list_3,linked_list_4))


    # Test case 3 - one list is empty. Union should return non-empty list, intersection should return empty list

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = [0, 2, 3, 4, 5, 6]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print("\nunion linked_list5 & linked_list6 - should contain [0, 2, 3, 4, 5, 6]")
    print(union(linked_list_5, linked_list_6))
    print("\nintersection linked_list5 & linked_list6 - should be empty")
    print(intersection(linked_list_5, linked_list_6))

    # Test case 4 - both lists empty. Both functions should return empty list

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print("\nunion linked_list7 & linked_list8 - should be empty")
    print(union(linked_list_7, linked_list_8))
    print("\nintersection linked_list7 & linked_list8 - should be empty")
    print(intersection(linked_list_7, linked_list_8))



if __name__ == "__main__":
    main()