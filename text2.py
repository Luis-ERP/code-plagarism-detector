import math
import itertools
from collections import deque

def read_matrix(n):
    """Reads an NxN matrix from standard input."""
    return [list(map(int, input().split())) for _ in range(n)]

def read_coordinates(n):
    """Reads a list of (x, y) coordinates from standard input."""
    return [tuple(map(int, input().split(','))) for _ in range(n)]

def find(parent, u):
    """Finds the root of u with path compression."""
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, u, v):
    """Unites two subsets u and v."""
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        parent[root_u] = root_v
        return True
    return False

def minimum_spanning_tree(n, distance_matrix):
    """Finds the MST using Kruskal's algorithm."""
    edges = [(distance_matrix[i][j], i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()
    parent = list(range(n))
    mst_edges = []
    
    for weight, u, v in edges:
        if union(parent, u, v):
            mst_edges.append((u, v))
            if len(mst_edges) == n - 1:
                break
    return mst_edges

def traveling_salesman(n, distance_matrix):
    """Solves the TSP using brute-force permutation."""
    nodes = list(range(n))
    start_node = 0
    other_nodes = nodes[1:]
    min_distance = float('inf')
    min_route = None
    
    for perm in itertools.permutations(other_nodes):
        route = [start_node] + list(perm) + [start_node]
        total_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(n))
        if total_distance < min_distance:
            min_distance = total_distance
            min_route = route
    return min_route, min_distance

def bfs(C, F, s, t):
    """Performs BFS to find an augmenting path for the max-flow problem."""
    n = len(C)
    parent = [-1] * n
    M = [0] * n
    M[s] = float('inf')
    queue = deque([s])
    
    while queue:
        u = queue.popleft()
        for v in range(n):
            if C[u][v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v == t:
                    return M[t], parent
                queue.append(v)
    return 0, parent

def max_flow(capacity_matrix, s, t):
    """Calculates maximum flow from s to t."""
    n = len(capacity_matrix)
    F = [[0] * n for _ in range(n)]
    flow = 0
    
    while True:
        m, parent = bfs(capacity_matrix, F, s, t)
        if m == 0:
            break
        flow += m
        v = t
        while v != s:
            u = parent[v]
            F[u][v] += m
            F[v][u] -= m
            v = u
    return flow

def closest_central_distance(central_coords, new_central_coord):
    """Finds the shortest Euclidean distance to the new central."""
    return min(math.hypot(x - new_central_coord[0], y - new_central_coord[1]) for x, y in central_coords)

# Input handling
N = int(input())
distance_matrix = read_matrix(N)
capacity_matrix = read_matrix(N)
central_coords = read_coordinates(N)
new_central_coord = tuple(map(int, input().split(',')))

# Problem 1: Minimum Spanning Tree
mst_edges = minimum_spanning_tree(N, distance_matrix)
node_labels = [chr(ord('A') + i) for i in range(N)]
print("Forma de cablear las colonias con fibra:")
for u, v in mst_edges:
    print(f"({node_labels[u]}, {node_labels[v]})")

# Problem 2: Traveling Salesman Problem
min_route, min_distance = traveling_salesman(N, distance_matrix)
route_labels = [node_labels[u] for u in min_route]
print("\nRuta a seguir por el personal que reparte correspondencia:")
print(' -> '.join(route_labels))

# Problem 3: Maximum Flow
s, t = 0, N - 1
flow = max_flow(capacity_matrix, s, t)
print("\nValor de flujo máximo de información del nodo inicial al nodo final:")
print(flow)

# Problem 4: Closest Distance to New Central
shortest_distance = closest_central_distance(central_coords, new_central_coord)
print("\nDistancia más corta entre la nueva central y la más cercana existente:")
print(shortest_distance)