class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        suffix_list = []
        return self._suffixes(suffix, suffix_list)

    def _suffixes(self, suffix, suffix_list):
        for key, node in self.children.items():
            suffix += key

            if node.isWord:
                suffix_list.append(suffix)
            if node.children:
                node._suffixes(suffix, suffix_list)

            suffix = ""

        return suffix_list


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, value):
        node = self.root

        for char in value:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]

        node.isWord = True

    def find(self, value):
        node = self.root

        for char in value:
            if char not in node.children:
                return False
            node = node.children[char]

        return node


def main():

    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    f = MyTrie.find("f")

    print(f.suffixes())


if __name__ == "__main__":
    main()

