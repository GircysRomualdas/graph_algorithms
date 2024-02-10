
def minimumIsland(grid):
    visited = set()
    minSize = float('inf')

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r, c, visited)

            if size < minSize and size > 0:
                minSize = size

    return minSize


def exploreSize(grid, r, c, visited):
    pos = str(r) + ',' + str(c)
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])

    if not rowInbounds or not colInbounds:
        return 0
    
    if grid[r][c] == 'W':
        return 0
    
    if pos in visited:
        return 0

    visited.add(pos)
    size = 1
    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r, c - 1, visited)
    size += exploreSize(grid, r, c + 1, visited)

    return size
    

    



grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(f"minimum Is land: {minimumIsland(grid)}")