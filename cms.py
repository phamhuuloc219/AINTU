from utils.checkin import exist
from utils.graph import draw_graph, draw_directed_graph
from utils.readfile import read_adj, read_h


def CMS(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float ('inf')] * len(adj)

    # Step 0:
    OPEN.append(start)
    g[start] = h[start][1]

    while len(OPEN) > 0:
        curr = OPEN.pop(0)
        print(f"curr: {curr}")
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")

        if curr == stop:
            print(f"Tim thay duong di {start} -> {stop}")
            path = []
            idx = stop
            while idx!= -1:
                path.insert(0, idx)     # chen vao dau path
                idx = Parent[idx]
            print(f"path: {path}")
            return

        for neighbor in range(len(adj)):
            if adj[curr][neighbor] == 1 and exist(CLOSE, neighbor) == False:
                if exist(OPEN, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + h[neighbor][1]
                    Parent[neighbor] = curr
                else:   # dinh da thuoc OPEN, chi cap nhat gnew khong dua vao Tn
                    g_tam = g[curr] + h[neighbor][1]
                    if g_tam < g[neighbor]:
                        g[neighbor] = g_tam
                        Parent[neighbor] = curr
        print(f"Parent: {Parent}")
        print(f"Tn: {Tn}")

        # Chen Tn vao dau OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Sap xep OPEN tang dan theo h
        OPEN_sorted = sorted(OPEN, key=lambda x: g[x], reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN sorted: {OPEN}")
        print(f"g: {g}")

        # Reset Tn
        Tn = []

    # OPEN = 0
    print(f"Khong tim thay duong di {start} -> {stop}")


if __name__ == '__main__':
    n, adj = read_adj('inputs/cms.adj')
    h = read_h('inputs/cms.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic: {h}")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"{adj[i]}")

    CMS(adj, 0, 9)

    # Ve do thi
    draw_graph(adj)
    draw_directed_graph(adj)