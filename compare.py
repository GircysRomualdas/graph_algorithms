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


# def measurTime1(type, graph, start, finish):
#     visited = set()

#     match type:
#         case "BFS":
#             time_taken = timeit.timeit(lambda: hasPathBFS(graph, start, finish, visited))
#         case "DFS":
#             time_taken = timeit.timeit(lambda: hasPathDFS(graph, start, finish, visited))
#         case _:
#             return 0

#     return time_taken


# def measurTime2(type, graph, start, finish):
#     visited = set()

#     match type:
#         case "BFS":
#             start_time = timeit.default_timer()
#             x = hasPathBFS(graph, start, finish, visited)
#             end_time = timeit.default_timer()
#         case "DFS":
#             start_time = timeit.default_timer()
#             x = hasPathDFS(graph, start, finish, visited)
#             end_time = timeit.default_timer()
#         case _:
#             return 0

#     return end_time - start_time


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

print("\t\tDFS")
visited = set()
print(f"has path from 'x' to 'v': {hasPathDFS(graph, 'x', 'v', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'x', 'v', visited))} s")
visited = set()
print(f"has path from 'y' to 'v': {hasPathDFS(graph, 'y', 'v', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'y', 'v', visited))} s")
visited = set()
print(f"has path from 'w' to 'x': {hasPathDFS(graph, 'w', 'x', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'w', 'x', visited))} s")

print("\t\tBFS")
visited = set()
print(f"has path from 'x' to 'v': {hasPathBFS(graph, 'x', 'v', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'x', 'v', visited))} s")
visited = set()
print(f"has path from 'y' to 'v': {hasPathBFS(graph, 'y', 'v', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'y', 'v', visited))} s")
visited = set()
print(f"has path from 'w' to 'x': {hasPathBFS(graph, 'w', 'x', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'w', 'x', visited))} s")

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
graph = buildGraph(edges)

print("\t\tDFS")
visited = set()
print(f"has path from 'i' to 'm': {hasPathDFS(graph, 'i', 'm', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'i', 'm', visited))} s")
visited = set()
print(f"has path from 'o' to 'n': {hasPathDFS(graph, 'o', 'n', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'o', 'n', visited))} s")
visited = set()
print(f"has path from 'j' to 'o': {hasPathDFS(graph, 'j', 'o', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'j', 'o', visited))} s")

print("\t\tBFS")
visited = set()
print(f"has path from 'i' to 'm': {hasPathBFS(graph, 'i', 'm', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'i', 'm', visited))} s")
visited = set()
print(f"has path from 'o' to 'n': {hasPathBFS(graph, 'o', 'n', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'o', 'n', visited))} s")
visited = set()
print(f"has path from 'j' to 'o': {hasPathBFS(graph, 'j', 'o', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'j', 'o', visited))} s")

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
graph = buildGraph(edges)

print("\t\tDFS")
visited = set()
print(f"has path from 'c' to 'e': {hasPathDFS(graph, 'c', 'e', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'c', 'e', visited))} s")
visited = set()
print(f"has path from 'e' to 'f': {hasPathDFS(graph, 'e', 'f', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'e', 'f', visited))} s")
visited = set()
print(f"has path from 'b' to 'd': {hasPathDFS(graph, 'b', 'd', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'b', 'd', visited))} s")

print("\t\tBFS")
visited = set()
print(f"has path from 'c' to 'e': {hasPathBFS(graph, 'c', 'e', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'c', 'e', visited))} s")
visited = set()
print(f"has path from 'e' to 'f': {hasPathBFS(graph, 'e', 'f', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'e', 'f', visited))} s")
visited = set()
print(f"has path from 'b' to 'd': {hasPathBFS(graph, 'b', 'd', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'b', 'd', visited))} s")

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
graph = buildGraph(edges)

print("\t\tDFS")
visited = set()
print(f"has path from 'a' to 'y': {hasPathDFS(graph, 'a', 'y', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'a', 'y', visited))} s")
visited = set()
print(f"has path from 'm' to 'e': {hasPathDFS(graph, 'm', 'e', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'm', 'e', visited))} s")
visited = set()
print(f"has path from 'u' to 's': {hasPathDFS(graph, 'u', 's', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathDFS(graph, 'u', 's', visited))} s")

print("\t\tBFS")
visited = set()
print(f"has path from 'a' to 'y': {hasPathBFS(graph, 'a', 'y', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'a', 'y', visited))} s")
visited = set()
print(f"has path from 'm' to 'e': {hasPathBFS(graph, 'm', 'e', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'm', 'e', visited))} s")
visited = set()
print(f"has path from 'u' to 's': {hasPathBFS(graph, 'u', 's', visited)} | Visited: {len(visited)} | Time: {timeit.timeit(lambda: hasPathBFS(graph, 'u', 's', visited))} s")

