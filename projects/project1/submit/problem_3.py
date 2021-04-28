import sys

class Node:
    def __init__(self, char=None, frequency=None):
        self.left = None
        self.right = None
        self.char = char
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def get_char(self):
        return self.char

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def __lt__(self, other):
        return self.frequency < other.frequency


def character_frequency(input_string):
    frequency_map = {}

    for char in input_string:
        if frequency_map.get(char):
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1

    return frequency_map


def huffman_encoding(data):
    huffman_tree = HuffmanTree()

    len_of_input = len(data)
    frequency_dict = character_frequency(data)
    priority_queue = MinHeap()

    for char, frequency in frequency_dict.items():
        new_node = Node(char, ((frequency / len_of_input) *100))
        priority_queue.insert(new_node)


    huffman_tree.build_from_queue(priority_queue)
    encoded_data = huffman_tree.encode(data)

    return encoded_data, huffman_tree


def huffman_decoding(data,tree):
    root = tree.get_root()
    node = root
    decoded_string = ""
    for bit in data:
        if bit == "0":
            node = node.get_left_child()
            if node.get_char() is not None:
                decoded_string += node.get_char()
                node = root
        if bit == "1":
            node = node.get_right_child()
            if node.get_char() is not None:
                decoded_string += node.get_char()
                node = root

    return decoded_string


class HuffmanTree:
    def __init__(self, root=None):
        self.root = root
        self.encoded = {}

    def get_root(self):
        return self.root

    def build_from_queue(self, priority_queue):

        if len(priority_queue) == 1:
            char_tuple = priority_queue.pop()
            new_node = Node(None, 100)
            new_node.left = char_tuple[1]
            priority_queue.insert(new_node)
        else:
            while len(priority_queue) > 1:
                left_tuple = priority_queue.pop()
                right_tuple = priority_queue.pop()

                frequency = right_tuple[0] + left_tuple[0]

                new_node = Node(None, frequency)
                new_node.left = left_tuple[1]
                new_node.right = right_tuple[1]
                priority_queue.insert(new_node)

        head_node = priority_queue.pop()

        self.root = head_node[1]

    def encode(self, data):
        self._encode(self.root, "")
        encoded_data = ""
        for char in data:
            encoded_data += self.encoded[char]

        return encoded_data

    def _encode(self, node, encoding):
        if node.get_char() is not None:
            self.encoded[node.get_char()] = encoding
        else:
            left_encoding = encoding + "0"
            self._encode(node.get_left_child(), left_encoding)
            if node.has_right_child():
                right_encoding = encoding + "1"
                self._encode(node.get_right_child(), right_encoding)

    def __repr__(self):

        queue = []
        queue.insert(0, self.root)

        while len(queue) > 0:
            node = queue.pop()
            if node.has_right_child():
                queue.insert(0,node.get_right_child())
            if node.has_left_child():
                queue.insert(0,node.get_left_child())
            else:
                return node.get_char()


class MinHeap:
    def __init__(self):
        self.Heap = []

    def insert(self, node):
        self.Heap.append((node.get_frequency(), node))
        self.Heap.sort()

    def pop(self):
        return self.Heap.pop(0)

    def __len__(self):
        return len(self.Heap)

    def __repr__(self):
        return str(self.Heap)


def main():
    ### Test 1
    print("Experiment 1\n")

    input_string = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The content of the data is: {}\n".format(input_string))
    print("The size of the data is: {}\n".format(sys.getsizeof(input_string)))

    encoded_data, tree = huffman_encoding(input_string)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    ### Test 2
    print("Experiment 2\n")

    input_string_2 = "AAA"

    print("The content of the data is: {}\n".format(input_string_2))
    print("The size of the data is: {}\n".format(sys.getsizeof(input_string_2)))

    encoded_data_2, tree_2 = huffman_encoding(input_string_2)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_2))))
    print("The content of the encoded data is: {}\n".format(encoded_data_2))

    decoded_data = huffman_decoding(encoded_data_2, tree_2)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Experiment 3\n")

    input_string = "E"

    print("The content of the data is: {}\n".format(input_string))
    print("The size of the data is: {}\n".format(sys.getsizeof(input_string)))

    encoded_data, tree = huffman_encoding(input_string)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    main()