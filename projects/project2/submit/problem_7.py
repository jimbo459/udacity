class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        node = self.root

        for path in self._prepare_path(path):
            if path not in node.children:
                node.insert(path)
            node = node.children[path]

        node.handler = handler

    def find(self, path):
        node = self.root

        for path in self._prepare_path(path):
            if path not in node.children:
                return False
            node = node.children[path]

        return node.handler

    def _prepare_path(self, path):
        return path.strip("/").split("/")


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.mux = RouteTrie(root_handler)
        self.handler = not_found_handler

    def add_handler(self, path, handler):
        self.mux.insert(path, handler)

    def lookup(self, path):
        if path == "/":
            return self.mux.handler

        handler = self.mux.find(path)

        if handler is None or handler is False:
            return self.handler
        else:
            return handler


def main():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler'
    print(router.lookup("/home/about/me"))  # should print 'not found handler'

    ### Additional tests for blank path and broken path
    print(router.lookup(""))  # should print 'not found handler'
    print(router.lookup("//"))  # should print 'not found handler'
    print(router.lookup("/home/abo"))  # should print 'not found handler'


if __name__ == "__main__":
    main()
