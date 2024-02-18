import timeit

def hasPathDFS(graph, src, dst, visited):
    if src in visited:
        return False
    
    visited.add(src)

    if (src == dst): 
        return True

    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dst, visited) == True:
            return True
        
    return False

def hasPathBFS(graph, src, dst, visited):
    queue = [src]
    visited.add(src)

    while queue:
        current = queue.pop(0)
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

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


def printResults(type, graph, start, finish):
    visited = set()

    match type:
        case "DFS":
            print(f"DFS - has path from '{start}' to '{finish}': {hasPathDFS(graph, start, finish, visited)} | Visited: {len(visited)} | Time: {measureTime("DFS", graph, start, finish)}s")
        case "BFS":
            print(f"BFS - has path from '{start}' to '{finish}': {hasPathBFS(graph, start, finish, visited)} | Visited: {len(visited)} | Time: {measureTime("BFS", graph, start, finish)}s")
        case _:
            print("ERROR")


def measureTime(type, graph, start, finish):
    visited = set()

    match type:
        case "BFS":
            start_time = timeit.default_timer()
            x = hasPathBFS(graph, start, finish, visited)
            end_time = timeit.default_timer()
        case "DFS":
            start_time = timeit.default_timer()
            x = hasPathDFS(graph, start, finish, visited)
            end_time = timeit.default_timer()
        case _:
            return 0

    return "{:.10f}".format(end_time - start_time)


print("\t"+"  x - y")
print("\t"+" /     \\")
print("\t"+"w       z")
print("\t"+" \\     /")
print("\t"+"    v   ")
print("")

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
graph = buildGraph(edges)

printResults("DFS", graph, 'x', 'v')
printResults("BFS", graph, 'x', 'v')
print("")
printResults("DFS", graph, 'y', 'v')
printResults("BFS", graph, 'y', 'v')
print("")
printResults("DFS", graph, 'w', 'x')
printResults("BFS", graph, 'w', 'x')

print("\t"+"i - j")
print("\t"+"| /")
print("\t"+"k - l")
print("\t"+"|")
print("\t"+"m")
print("\t"+"")
print("\t"+"o - n")
print("")

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
graph = buildGraph(edges)

printResults("DFS", graph, 'i', 'm')
printResults("BFS", graph, 'i', 'm')
print("")
printResults("DFS", graph, 'o', 'n')
printResults("BFS", graph, 'o', 'n')
print("")
printResults("DFS", graph, 'j', 'o')
printResults("BFS", graph, 'j', 'o')

print("\t"+"    a")
print("\t"+"   / \\")
print("\t"+"  b   d")
print("\t"+" /   / \\")
print("\t"+"c   e   f")
print("")

edges = [
    ['f', 'd'],
    ['e', 'd'],
    ['a', 'd'],
    ['a', 'b'],
    ['c', 'b']
]
graph = buildGraph(edges)

printResults("DFS", graph, 'c', 'e')
printResults("BFS", graph, 'c', 'e')
print("")
printResults("DFS", graph, 'e', 'f')
printResults("BFS", graph, 'e', 'f')
print("")
printResults("DFS", graph, 'b', 'd')
printResults("BFS", graph, 'b', 'd')

print("\t"+"a - b - c - d - e")
print("\t"+"|   |   |   |   |")
print("\t"+"f - g - h - i - j")
print("\t"+"|   |   |   |   |")
print("\t"+"k - l - m - n - o")
print("\t"+"|   |   |   |   |")
print("\t"+"p - q - r - s - t")
print("\t"+"|   |   |   |   |")
print("\t"+"u - v - w - x - y")
print("")

edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd'],
    ['d', 'e'],
    ['a', 'f'],
    ['b', 'g'],
    ['c', 'h'],
    ['d', 'i'],
    ['e', 'j'],
    ['f', 'g'],
    ['g', 'h'],
    ['h', 'i'],
    ['i', 'j'],
    ['f', 'k'],
    ['g', 'l'],
    ['h', 'm'],
    ['i', 'n'],
    ['j', 'o'],
    ['k', 'l'],
    ['l', 'm'],
    ['m', 'n'],
    ['n', 'o'],
    ['k', 'p'],
    ['l', 'q'],
    ['m', 'r'],
    ['n', 's'],
    ['o', 't'],
    ['p', 'q'],
    ['q', 'r'],
    ['r', 's'],
    ['s', 't'],
    ['p', 'u'],
    ['q', 'v'],
    ['r', 'w'],
    ['s', 'x'],
    ['t', 'y'],
    ['u', 'v'],
    ['v', 'w'],
    ['w', 'x'],
    ['x', 'y']
]
graph = buildGraph(edges)

printResults("DFS", graph, 'a', 'y')
printResults("BFS", graph, 'a', 'y')
print("")
printResults("DFS", graph, 'm', 'e')
printResults("BFS", graph, 'm', 'e')
print("")
printResults("DFS", graph, 'u', 's')
printResults("BFS", graph, 'u', 's')
