
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

def undirectedPathDFS(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    return hasPathDFS(graph, nodeA, nodeB, set())

def hasPathDFS(graph, src, dst, visited):
    if (src == dst): 
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dst, visited) == True:
            return True
        
    return False



#   i - j
#   | /
#   k - l
#   |
#   m
#
#   o - n

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print("DFS")
print(f"has path from 'j' to 'm': {undirectedPathDFS(edges, 'j', 'm')}")
print(f"has path from 'o' to 'n': {undirectedPathDFS(edges, 'o', 'n')}")
print(f"has path from 'k' to 'n': {undirectedPathDFS(edges, 'k', 'n')}")