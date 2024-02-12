
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

print("\t\tDFS")
visited = set()
print(f"has path from 'x' to 'v': {hasPathDFS(buildGraph(edges), 'x', 'v', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'y' to 'v': {hasPathDFS(buildGraph(edges), 'y', 'v', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'w' to 'x': {hasPathDFS(buildGraph(edges), 'w', 'x', visited)} | Visited: {len(visited)} ")

print("\t\tBFS")
visited = set()
print(f"has path from 'x' to 'v': {hasPathBFS(buildGraph(edges), 'x', 'v', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'y' to 'v': {hasPathBFS(buildGraph(edges), 'y', 'v', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'w' to 'x': {hasPathBFS(buildGraph(edges), 'w', 'x', visited)} | Visited: {len(visited)} ")

print("________________________________________________\n")


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

print("\t\tDFS")
visited = set()
print(f"has path from 'i' to 'm': {hasPathDFS(buildGraph(edges), 'i', 'm', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'o' to 'n': {hasPathDFS(buildGraph(edges), 'o', 'n', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'j' to 'o': {hasPathDFS(buildGraph(edges), 'j', 'o', visited)} | Visited: {len(visited)} ")

print("\t\tBFS")
visited = set()
print(f"has path from 'i' to 'm': {hasPathBFS(buildGraph(edges), 'i', 'm', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'o' to 'n': {hasPathBFS(buildGraph(edges), 'o', 'n', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'j' to 'o': {hasPathBFS(buildGraph(edges), 'j', 'o', visited)} | Visited: {len(visited)} ")

print("________________________________________________\n")


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

print("\t\tDFS")
visited = set()
print(f"has path from 'c' to 'e': {hasPathDFS(buildGraph(edges), 'c', 'e', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'e' to 'f': {hasPathDFS(buildGraph(edges), 'e', 'f', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'b' to 'd': {hasPathDFS(buildGraph(edges), 'b', 'd', visited)} | Visited: {len(visited)} ")

print("\t\tBFS")
visited = set()
print(f"has path from 'c' to 'e': {hasPathBFS(buildGraph(edges), 'c', 'e', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'e' to 'f': {hasPathBFS(buildGraph(edges), 'e', 'f', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'b' to 'd': {hasPathBFS(buildGraph(edges), 'b', 'd', visited)} | Visited: {len(visited)} ")

print("________________________________________________\n")


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

print("\t\tDFS")
visited = set()
print(f"has path from 'a' to 'y': {hasPathDFS(buildGraph(edges), 'a', 'y', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'm' to 'e': {hasPathDFS(buildGraph(edges), 'm', 'e', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'u' to 's': {hasPathDFS(buildGraph(edges), 'u', 's', visited)} | Visited: {len(visited)} ")

print("\t\tBFS")
visited = set()
print(f"has path from 'a' to 'y': {hasPathBFS(buildGraph(edges), 'a', 'y', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'm' to 'e': {hasPathBFS(buildGraph(edges), 'm', 'e', visited)} | Visited: {len(visited)} ")
visited = set()
print(f"has path from 'u' to 's': {hasPathBFS(buildGraph(edges), 'u', 's', visited)} | Visited: {len(visited)} ")
