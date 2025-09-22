# Convert Array of Edges => Adjacency Matrix

n = 5
A = [[0,1],[0,2],[3,4],[4,1],[3,3]]

M = []

for i in range(n):
    M.append([0] * n)

for u, v in A:
    M[u][v] = 1

    # Uncomment the following line if the graph undirected
    # M[v][u] = 1

for i in M:
    print(i)

