
def hasPathDFS(graph, src, dst):
    if (src == dst): 
        return True
    
    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dst) == True:
            return True
        
    return False

def hasPathBFS(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop(0)
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False
            

#    f -* g -* h
#    |   *    
#    |  /
#    * /       
#    i *- j
#    |
#    *       
#    k

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(f"Graph:\n {graph}")

print("DFS")
print(f"has path from 'f' to 'h': {hasPathDFS(graph, 'f', 'h')}")
print(f"has path from 'f' to 'k': {hasPathDFS(graph, 'f', 'k')}")
print(f"has path from 'f' to 'j': {hasPathDFS(graph, 'f', 'j')}")

print("BFS")
print(f"has path from 'f' to 'h': {hasPathBFS(graph, 'f', 'h')}")
print(f"has path from 'f' to 'k': {hasPathBFS(graph, 'f', 'k')}")
print(f"has path from 'f' to 'j': {hasPathDFS(graph, 'f', 'j')}")