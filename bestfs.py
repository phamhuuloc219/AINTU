from utils.checkin import exist
from utils.graph import draw_graph, draw_directed_graph
from utils.readfile import read_adj, read_h


def BestFirstSearch(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * (len(adj))

    # Step 0:
    OPEN.append(start)

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
            if adj[curr][neighbor] == 1 and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == False:
                Tn.append(neighbor)
                Parent[neighbor] = curr

        print(f"Tn: {Tn}")

        # Chen Tn vao dau OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Sap xep OPEN tang dan theo h
        OPEN_sorted = sorted(OPEN, key=lambda x: h[x][1], reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN sorted: {OPEN}")

        # Reset Tn
        Tn = []

    # OPEN = 0
    print(f"Khong tim thay duong di {start} -> {stop}")


if __name__ == '__main__':
    n, adj = read_adj('inputs/bestfs.adj')
    h = read_h('inputs/bestfs.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic: {h}")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"{adj[i]}")

    BestFirstSearch(adj, 0, 6)
    # Ve do thi
    draw_graph(adj)
    draw_directed_graph(adj)