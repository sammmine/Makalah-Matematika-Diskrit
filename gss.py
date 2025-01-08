# Deque adalah struktur data seperti list,
# tapi bisa append & pop dari ujung kiri & kanan
from collections import deque

# Breadth First Search (BFS)
# untuk Glass Stepping Stones (GSS)
def bfs_GSS(GSS, vertex_start, vertex_end):
    queue = deque([[vertex_start]])
    visited = set()
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        if vertex == vertex_end:
            return path
        elif vertex not in visited:
            for neighbor in GSS.get(vertex, []):
                new_path = list(path) + [neighbor]
                queue.append(new_path)
            visited.add(vertex)
    return None

# Data Petak-Petak Kaca Kuat GSS
GSS = {
    (1, 0): [(2, 1)],
    (1, 1): [],
    (2, 0): [],
    (2, 1): [(3, 1)],
    (3, 0): [],
    (3, 1): [(4, 0)],
    (4, 0): [(5, 1)],
    (4, 1): [],
    (5, 0): [],
    (5, 1): [(6, 0)],
    (6, 0): [(7, 1)],
    (6, 1): [],
    (7, 0): [],
    (7, 1): [(8, 0)],
    (8, 0): [(9, 1)],
    (8, 1): [],
    (9, 0): [],
    (9, 1): []
}

# Simpul awal dan simpul akhir
vertex_start = (1, 0)
vertex_end = (9, 1)

# Jalur yang aman
jalur = bfs_GSS(GSS, vertex_start, vertex_end)
print("Jalur Aman:", jalur)





