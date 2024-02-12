import networkx as nx
import matplotlib.pyplot as plt

# Define edges array
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

#   a - b - c - d - e
#   |   |   |   |   |
#   f - g - h - i - j
#   |   |   |   |   |
#   k - l - m - n - o
#   |   |   |   |   |
#   p - q - r - s - t
#   |   |   |   |   |
#   u - v - w - x - y

# Create empty undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='k', linewidths=1, font_size=10)
plt.show()
