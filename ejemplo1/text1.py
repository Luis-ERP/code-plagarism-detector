import math
import itertools
from collections import deque

# Lectura de datos de entrada
N = int(input())
distance_matrix = []
for _ in range(N):
    line = input().split(" ")
    distance_matrix.append([int(x) for x in line])

capacity_matrix = []
for _ in range(N):
    line = input().split(" ")
    capacity_matrix.append([int(x) for x in line])

central_coords = []
for _ in range(N):
    line = input()
    x_str, y_str = line.split(',')
    x = int(x_str)
    y = int(y_str)
    central_coords.append((x, y))

line = input()
x_str, y_str = line.split(',')
new_central_coord = (int(x_str), int(y_str))

# Problema 1: Encontrar el árbol de expansión mínima (MST)
edges = []
for i in range(N):
    for j in range(i+1, N):
        weight = distance_matrix[i][j]
        edges.append((weight, i, j))

# Implementación de Union-Find para Kruskal
parent = [i for i in range(N)]

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]  # Compresión de caminos
        u = parent[u]
    return u

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        parent[u_root] = v_root
        return True
    return False

# Kruskal para encontrar el MST
mst_edges = []
edges.sort()
for weight, u, v in edges:
    if union(u, v):
        mst_edges.append((u, v))
        if len(mst_edges) == N - 1:
            break

node_labels = [chr(ord('A') + i) for i in range(N)]
print("Forma de cablear las colonias con fibra:")
for u, v in mst_edges:
    print(f"({node_labels[u]}, {node_labels[v]})")


# Problema 2: Resolver el problema del Viajante (TSP)
nodes = list(range(N))
start_node = 0
other_nodes = nodes[1:]

min_route = None
min_distance = float('inf')

for perm in itertools.permutations(other_nodes):
    route = [start_node] + list(perm) + [start_node]
    total_distance = 0
    for i in range(len(route)-1):
        u = route[i]
        v = route[i+1]
        total_distance += distance_matrix[u][v]
    if total_distance < min_distance:
        min_distance = total_distance
        min_route = route

print("\nRuta a seguir por el personal que reparte correspondencia:")
route_labels = [node_labels[u] for u in min_route]
print(' -> '.join(route_labels))


# Problema 3: Calcular el flujo máximo entre el nodo inicial y final
def bfs(C, F, s, t):
    n = len(C)
    parent = [-1]*n
    M = [0]*n
    M[s] = float('inf')
    queue = deque()
    queue.append(s)
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

def max_flow(C, s, t):
    n = len(C)
    F = [[0]*n for _ in range(n)]
    flow = 0
    while True:
        m, parent = bfs(C, F, s, t)
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

C = capacity_matrix
s = 0
t = N - 1
flow = max_flow(C, s, t)

print("\nValor de flujo máximo de información del nodo inicial al nodo final:")
print(flow)


# Problema 4: Calcular la distancia más corta a la nueva central
min_distance = float('inf')
for coord in central_coords:
    dx = coord[0] - new_central_coord[0]
    dy = coord[1] - new_central_coord[1]
    distance = math.hypot(dx, dy)
    if distance < min_distance:
        min_distance = distance

print("\nDistancia más corta entre la nueva central y la más cercana existente:")
print(min_distance)