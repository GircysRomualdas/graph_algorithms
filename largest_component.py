
def largestComponent(graph):
    longest = 0
    visited = set()

    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size

    return longest

def exploreSize(graph, node, visited):
    size = 1

    if node in visited:
        return 0
    
    visited.add(node)
    
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    return size


#       5
#       | \ 
#   1 - 0 - 8
#
#       4 - 2
#       \  /
#         3

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(f"largest component count: {largestComponent(graph)}")