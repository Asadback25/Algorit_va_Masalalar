# Convert Array of Edges => Adjacency List

from collections import defaultdict

A = [[0,1],[0,2],[3,4],[4,1],[3,3]]

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

print(D)
