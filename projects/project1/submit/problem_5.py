import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
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


if __name__ == "__main__":
    main()
