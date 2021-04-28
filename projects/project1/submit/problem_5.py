import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
        if len(data) == 0:
            print("Please provide data for block")
            return

        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data, timestamp)
        self.next = None

    def get_hash(self):
        return self.hash

    def set_next(self, block):
        self.next = block

    def get_next(self):
        return self.next

    def calc_hash(self, data, timestamp):
        sha = hashlib.sha256()

        hash_str = (str(timestamp) + data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Block(time.time(), data, None)
        else:
            new_node = Block(time.time(), data, self.head.get_hash())
            new_node.set_next(self.head)
            self.head = new_node

    def get_head(self):
        return self.head


def main():

    ### Test 1
    ### Create a new BlockChain
    bc = BlockChain()

    ### Add three blocks
    bc.add("Some data")
    bc.add("Some data")
    bc.add("Some data")

    ### Print all hash entries in blockchain
    block = bc.get_head()
    while block is not None:
        print(block.get_hash())
        block = block.get_next()

    ### Test 2
    bc_2 = BlockChain()
    ### Add empty block - prints message instructing user to add data
    bc_2.add("")

    ### Test 3
    bc_3 = BlockChain()
    ### Add different characters to data
    bc_3.add("123123")
    bc_3.add("Some data")

    ### Print all hash entries in blockchain
    block = bc_3.get_head()
    while block is not None:
        print(block.get_hash())
        block = block.get_next()


if __name__ == "__main__":
    main()
