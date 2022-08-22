print('Task 1')
# Depth - First Search method (DFS Method)

graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G', '1'],
    '1' : ['C']
}


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited

visited = dfs(graph1, 'A', [])
print(visited)


print('Task 2')
# Breadth-First Search DFS - method

from collections import deque

class Graph(object):
    def __init__(self, *args, **kwargs):
        self.order = []  # visited order
        self.neighbor = {}

    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            print(
                'Ввод узла должен быть линейной таблицей')
        self.neighbor[key] = val

    def BFS(self, root):
        if root != None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if (not person in visited) and (person in self.neighbor.keys()):
                search_queue += self.neighbor[person]
                visited.append(person)

    def clear(self):
        self.order = []

    def node_print(self):
        for index in self.order:
            print(index, end='  ')


if __name__ == '__main__':
    g = Graph()
    g.add_node(('A', ['B', 'C']))
    g.add_node(('B', ['D', 'E']))
    g.add_node(('C', ['F']))

    # Делаем поиск в ширину
    g.BFS('A')
    print("Первый поиск в ширину:")
    g.node_print()
    g.clear()



adj = [
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]
level = [-1] * len(adj)

# Поиск в ширину функция
def bfs(s):
    global level
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in adj[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1

for i in range(len(adj)):
    if level[i] == -1:
        bfs(i)
print(level[2])