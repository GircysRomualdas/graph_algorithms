
def islandCount(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1

    return count


def explore(grid, r, c, visited):
    pos = str(r) + ',' + str(c)
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False
    
    if grid[r][c] == 'W':
        return False

    if pos in visited:
        return False 
    
    visited.add(pos)
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True




grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(f"is land count: {islandCount(grid)}")