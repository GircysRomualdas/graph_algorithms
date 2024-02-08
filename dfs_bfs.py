
def dfs(graph, source):
    print("\nDFS:")
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def bfs(graph, source):
    print("\nBFS:")
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)
            

#    a -* c
#    |    |
#    *    *     
#    b    e
#    |
#    *       
#    d -* f

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(f"Graph:\n {graph}")
dfs(graph, 'a')
bfs(graph, 'a')
