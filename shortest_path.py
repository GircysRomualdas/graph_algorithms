
def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    queue = [[nodeA, 0]]
    visited = set([nodeA])

    while queue:
        [node, distance] = queue.pop(0)

        if node == nodeB:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
    
    return -1


def buildGraph(edges):
    graph = {}

    for edge in edges:
        [a, b] = edge

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph 

#
#      x - y
#     /     \
#    w       z
#     \     /
#        v

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

print(f"shortest path from 'w' to 'z': {shortestPath(edges, 'w', 'z')}")