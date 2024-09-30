from utils.readfile_bfsdfs import read_adj
from utils.checkin import exist
from utils.graph import *


def DFS(adj, start, stop):
    OPEN = []   # tap cac dinh can xem xet
    CLOSE = []  # tap cac dinh da xet
    Tn = []     # tap cac dinh ke voi dinh dang xet
    Parent = [-1]*n # mang co n phan tu, moi ptu co gia tri la 1

    # Khoi tao cac gia tri
    OPEN.append(start)      # dua dinh start vao cuoi OPEN
    print(f"OPEN: {OPEN}")
    print(f"Parent: {Parent}")

    while len(OPEN) > 0:    # OPEN khac rong
        curr = OPEN.pop(0)     # lay ra tu dau OPEN
        print(f"curr: {curr}")

        if curr == stop:
            print("Tim thay duong di ngan nhat")
            # in ra lo trinh tu start - stop
            path = []
            idx = stop
            while idx != -1:
                path.append(idx)
                idx = Parent[idx]
            path.reverse()
            print(f"path: {path}")
            return

        # nguoc lai: n khong phai la STOP
        CLOSE.append(curr)  # dua n vao tap CLOSE
        print(f"CLOSE: {CLOSE}")

        # tim cac dinh ke cua n
        Tn = []     # reset Tn
        for neighbor in range(n):
            if adj[curr][neighbor] == 1 and exist(OPEN, neighbor) == False and exist(CLOSE, neighbor) == False:
                Tn.append(neighbor)
                Parent[neighbor] = curr
        print(f"Tn: {Tn}")
        print(f"Parent: {Parent}")

        # OPEN = OPEN + Tn    # Noi Tn vao sau OPEN: BFS
        OPEN = Tn + OPEN      # Noi Tn vao sau OPEN: DFS
        print(f"OPEN: {OPEN}")

    print("Khong tim thay duong di")


if __name__ == '__main__':
    n, adj = read_adj('inputs/bfs.adj')
    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"{adj[i]}")

    DFS(adj, 0, 6)
    draw_graph(adj)
    draw_directed_graph(adj)
