def is_safe(node, color, graph, colors):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, m, colors, node):
    if node == len(graph):
        return True

    for color in range(m):
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if graph_coloring_util(graph, m, colors, node + 1):
                return True
            colors[node] = -1  # backtrack

    return False

def graph_coloring(graph):
    n = len(graph)
    colors = [-1] * n  # Inicializar colores de nodos como no asignados
    m = n  # Número máximo de colores es igual al número de nodos

    if not graph_coloring_util(graph, m, colors, 0):
        print("No es posible asignar colores a los nodos")
        return

    print("Asignación de colores a los vértices:")
    for i in range(n):
        print(f"Vértice: {i}, Color asignado: {colors[i]}")

n = int(input("Número de nodos: "))
print("Introduce la matriz de adyacencias (separada por espacios):")
graph = [list(map(int, input().split())) for _ in range(n)]

graph_coloring(graph)
