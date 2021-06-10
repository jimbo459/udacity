import heapq
import math


class Map_10:
    def __init__(self, intersections, roads):
        self.intersections = intersections
        self.roads = roads


class Node:
    def __init__(self, value, x, y):
        self.visited = False
        self.parent = None
        self.x = x
        self.y = y
        self.children = []
        self.total_cost = math.inf
        self.path_cost = math.inf
        self.value = value

    def __lt__(self,other):
        return self.total_cost < other.total_cost


def create_graph(map_object):
    graph = []

    for key, values in map_object.intersections.items():
        graph.append(Node(key, values[0], values[1]))

    for x in range(len(map_object.roads)):
        for road in map_object.roads[x]:
            graph[x].children.append(graph[road])

    return graph


def heuristic(node_1, node_2):
    return math.sqrt(math.pow(node_2.x - node_1.x, 2)+math.pow(node_2.y - node_1.y, 2))


def shortest_path(map_object, start, goal):

    graph = create_graph(map_object)

    node_start = graph[start]
    node_goal = graph[goal]

    node_start.path_cost = 0
    node_start.total_cost = heuristic(node_start, node_goal)

    min_heap = list()

    min_heap.append(node_start)

    while len(min_heap) > 0:

        min_heap.sort(key=lambda x: x.total_cost)

        current_node = min_heap.pop(0)

        current_node.visited = True

        for child in current_node.children:
            if child.visited is False:
                min_heap.append(child)

            new_path_cost = current_node.path_cost + heuristic(current_node, child)

            if new_path_cost < child.path_cost:
                child.parent = current_node
                child.path_cost = new_path_cost
                child.total_cost = child.path_cost + heuristic(child, node_goal)

    parent_node = node_goal

    path = []
    while parent_node is not None:
        path.insert(0, parent_node.value)
        parent_node = parent_node.parent

    return path


def main():
    map_object = Map_10(
        {0: [0.7798606835438107, 0.6922727646627362],
         1: [0.7647837074641568, 0.3252670836724646],
         2: [0.7155217893995438, 0.20026498027300055],
         3: [0.7076566826610747, 0.3278339270610988],
         4: [0.8325506249953353, 0.02310946309985762],
         5: [0.49016747075266875, 0.5464878695400415],
         6: [0.8820353070895344, 0.6791919587749445],
         7: [0.46247219371675075, 0.6258061621642713],
         8: [0.11622158839385677, 0.11236327488812581],
         9: [0.1285377678230034, 0.3285840695698353]},
            [[7, 6, 5],
             [4, 3, 2],
             [4, 3, 1],
             [5, 4, 1, 2],
             [1, 2, 3],
             [7, 0, 3],
             [0],
             [0, 5],
             [9],
             [8]]
    )

    print(shortest_path(map_object, 0,2))

if __name__ == "__main__":
    main()