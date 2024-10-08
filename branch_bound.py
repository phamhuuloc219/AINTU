from utils.checkin import exist
from utils.graph import draw_graph, draw_directed_graph
from utils.readfile import read_adj, read_h


def Branch_Bound(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float ('inf')] * len(adj)
    f = [float('inf')] * len(adj)

    # Step 0:
    OPEN.append(start)
    g[start] = 0
    f[start] = h[start][1]
    flag = False
    fmin = float('inf')

    while len(OPEN) > 0:
        curr = OPEN.pop(0)
        print(f"curr: {curr}")
        CLOSE.append(curr)
        print(f"CLOSE: {CLOSE}")
        if curr == stop:
            flag = True
            if f[curr] < fmin: fmin = f[curr]

        for neighbor in range(len(adj)):
            if adj[curr][neighbor] !=0:
                # m: khong thuoc OPEN va CLOSE
                if f[curr]<fmin and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    Parent[neighbor] = curr

                # m: thuoc OPEN (khong quan tam den CLOSE)
                if f[curr]<fmin and exist(OPEN, neighbor) == True:
                    g_new = g[curr] + adj[curr][neighbor]
                    f_new = g_new + h[neighbor][1]
                    if f_new < f[neighbor]:
                        g[neighbor] = g_new
                        f[neighbor] = f_new
                        print(f"cap nhat gia tri f({neighbor}), g({neighbor}):")
                        print(f"g_new({neighbor}): {g_new}, f_new({neighbor}): {f_new}")
                        Parent[neighbor] = curr  # cap nhat lai Parent va khong dua vao Tn

                # m: khong thuoc ve OPEN nhung thuoc ve CLOSE
                if f[curr]<fmin and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == True:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]

        print(f"Tn: {Tn}")
        # Chen Tn vao dau OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Sap xep OPEN tang dan theo f
        OPEN_sorted = sorted(OPEN, key=lambda x: f[x], reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN sorted: {OPEN}")
        print(f"g: {g}")
        print(f"f: {f}")
        print(f"Parent: {Parent}")

        # Reset Tn
        Tn = []

    # kiem tra gia tri flag
    if flag==False:
        print(f"Khong tim thay duong di {start} -> {stop}")
    else:
        print(f"Tim thay duong di {start} -> {stop}")
        path = []
        idx = stop
        while idx != start:
            path.insert(0, idx)  # chen vao dau path
            idx = Parent[idx]
        path.insert(0, start)
        print(f"path: {path}")


if __name__ == '__main__':
    n, adj = read_adj('inputs/branch_bound.adj')
    h = read_h('inputs/branch_bound.h')
    print(f"Number of nodes: {n}")
    print(f"Heuristic: {h}")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"{adj[i]}")

    Branch_Bound(adj, 0, 6)
    # Ve do thi
    draw_graph(adj)
    draw_directed_graph(adj)