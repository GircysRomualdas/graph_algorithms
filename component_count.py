
def connectedComponentsCount(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count

def explore(graph, current, visited):

    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

    


#   1 - 2
#
#       4
#       |
#   5 - 6 - 8
#       |
#       7
#
#   3

graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}

print(f"count connected components: {connectedComponentsCount(graph)}")