from utils.checkin import exist
from utils.graph import draw_graph, draw_directed_graph
from utils.readfile import read_adj, read_h


def Branch_Bound(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float('inf')] * len(adj)
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
                # m: Không thuộc OPEN và CLOSE
                if f[curr]<fmin and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]
                    Parent[neighbor] = curr

                # m: Thuộc OPEN
                if f[curr]<fmin and exist(OPEN, neighbor) == True:
                    g_new = g[curr] + adj[curr][neighbor]
                    f_new = g_new + h[neighbor][1]
                    if f_new < f[neighbor]:
                        g[neighbor] = g_new
                        f[neighbor] = f_new
                        print(f"cap nhat gia tri f({neighbor}), g({neighbor}):")
                        print(f"g_new({neighbor}): {g_new}, f_new({neighbor}): {f_new}")
                        Parent[neighbor] = curr  # Cập nhật lại Parent và không đưa vào Tn

                # m: Không thuộc về OPEN nhưng thuộc về CLOSE
                if f[curr]<fmin and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == True:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + adj[curr][neighbor]
                    f[neighbor] = g[neighbor] + h[neighbor][1]

        print(f"Tn: {Tn}")
        # Chèn Tn vào đầu OPEN
        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        # Sắp xếp OPEN tăng dần theo f
        OPEN_sorted = sorted(OPEN, key=lambda x: f[x], reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN sorted: {OPEN}")
        print(f"g: {g}")
        print(f"f: {f}")
        print(f"Parent: {Parent}")

        # Reset Tn
        Tn = []

    # Kiểm tra giá trị flag
    if flag == False:
        print(f"Không tìm thấy đường đi {start} -> {stop}")
    else:
        print(f"Tìm thấy đường đi {start} -> {stop}")
        path = []
        idx = stop
        while idx != start:
            path.insert(0, idx)  # chèn vào đầu path
            idx = Parent[idx]
        path.insert(0, start)
        print(f"path: {path}")

# def Branch_Bound(adj, start, stop):
#     OPEN = []
#     CLOSE = []
#     Tn = []
#     Parent = [-1] * len(adj)
#     g = [float('inf')] * len(adj)
#     f = [float('inf')] * len(adj)
#
#     # Step 0:
#     OPEN.append(start)
#     g[start] = 0
#     f[start] = h[start][1]
#     flag = False
#     fmin = float('inf')
#
#     while len(OPEN) > 0:
#         curr = OPEN.pop(0)
#         print(f"curr: {curr}")
#         CLOSE.append(curr)
#         print(f"CLOSE: {CLOSE}")
#         if curr == stop:
#             flag = True
#             if f[curr] < fmin:
#                 fmin = f[curr]
#
#         for neighbor in range(len(adj)):
#             if adj[curr][neighbor] != 0:
#                 # Check if the node is not in OPEN and CLOSE
#                 if f[curr] < fmin and not exist(OPEN, neighbor) and not exist(CLOSE, neighbor):
#                     Tn.append(neighbor)
#                     g[neighbor] = g[curr] + adj[curr][neighbor]
#                     f[neighbor] = g[neighbor] + h[neighbor][1]
#                     Parent[neighbor] = curr
#
#                 # If the neighbor is already in OPEN, check for a better path
#                 elif f[curr] < fmin and exist(OPEN, neighbor):
#                     g_new = g[curr] + adj[curr][neighbor]
#                     f_new = g_new + h[neighbor][1]
#                     if f_new < f[neighbor]:
#                         g[neighbor] = g_new
#                         f[neighbor] = f_new
#                         Parent[neighbor] = curr
#
#         print(f"Tn: {Tn}")
#         # Add new nodes to OPEN and sort by f value
#         OPEN.extend(Tn)
#         OPEN = sorted(OPEN, key=lambda x: f[x])  # Sort OPEN by f values in ascending order
#         print(f"OPEN: {OPEN}")
#
#         print(f"g: {g}")
#         print(f"f: {f}")
#         print(f"Parent: {Parent}")
#
#         # Reset Tn
#         Tn = []
#
#     # Check if a path was found
#     if not flag:
#         print(f"No path found from {start} to {stop}")
#     else:
#         print(f"Path found from {start} to {stop}")
#         path = []
#         idx = stop
#         while idx != start:
#             path.insert(0, idx)  # Insert at the beginning of the path
#             idx = Parent[idx]
#         path.insert(0, start)
#         print(f"Path: {path}")

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