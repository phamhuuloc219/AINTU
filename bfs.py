# from utils.readfile_bfdfs import readFile
#
# def checkIn(list, point):
#     for i in range(len(list)):
#         if point in list:
#             return True
#     return False
#
# def BFS(adj, start, stop):
#     # Khởi tạo giá trị
#     OPEN = []  # Tập các đỉnh tiềm năng
#     CLOSE = []  # Tập các đỉnh đã xét
#     Tn = [] # Tập các đỉnh đang xét
#     curr = start
#     OPEN.append(start) # chèn start vào cuói OPEN
#
#      # trong khi OPEN còn đỉnh để xét
#     while len(OPEN) > 0:
#         curr = OPEN.pop(0) # Lấy ra đầu OPEN 1 đỉnh
#         print(f"curr: {curr}")
#         CLOSE.append(curr)
#         Tn = [] #clear Tn
#         Parent = [-1] * n  # khoi tao parent -1 n lan
#
#         if curr == stop:
#             print("Goal reached!")
#             # in ra đường đi từ stop tới start
#             path = []
#             for i in range(n):
#
#             return
#
#         for neighbor in range(n): # xét các đỉnh kề
#             if adj[curr][neighbor] == 1 and checkIn(OPEN, neighbor) == False and checkIn(CLOSE, neighbor) == False:
#                 Tn.append(neighbor) # Thêm các đỉnh kề vào danh sách Tn
#                 OPEN.append(neighbor) # Thêm các đỉnh kề vào OPEN
#                 Parent[neighbor] = curr
#
#         print(f"Tn: {Tn}")
#         print(f"CLOSE: {CLOSE}")
#         print(f"OPEN: {OPEN}")
#     print("Goal unreachable!")
#
# def main():
#     n, adj = readFile('inputs/bfs.adj')
#     print(f"Number of node: {n}")
#     for i in range(n):
#         print(f"Node {i}: {adj[i]}")
#     BFS(adj, 0, 6)
# if __name__ == '__main__':
#     main()

from utils.readfile_bfsdfs import readfile
from utils.graph import *

def checkin(list, point):
    for i in range(len(list)):
        if list[i] == point:
            return True
    return False


def BFS(adj, start, stop):
    # khoi tao cac gia tri
    OPEN = []  # tap cac dinh tiem nang
    CLOSE = []  # tap cac dinh da xet
    Tn = []     # tap cac dinh ke cua dinh dang xet
    Parent = [-1] * n   # khoi tao parent = -1 -1 -1 .. -1

    OPEN.append(start)   # chen start vao cuoi OPEN

    while len(OPEN) > 0:    # OPEN con dinh de xet
        curr = OPEN.pop(0)   # Lay ra dau OPEN 1 dinh
        print(f"curr: {curr}")
        CLOSE.append(curr)  # them dinh dang xet vao CLOSE
        Tn = [] # clear Tn

        if curr == stop:
            print("Goal reach!")
            # in ra duong di tu Stop - Start
            path = []  # duong di cua do thi
            idx = stop
            while idx != -1:
                path.append(idx)
                idx = Parent[idx]

            path.reverse()
            print(path)
            return

        # nguoc lai thi xet cac dinh ke
        for neighbor in range(n):
            if adj[curr][neighbor] == 1 and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                Tn.append(neighbor) # them cac dinh ke vao danh sach Tn
                OPEN.append(neighbor)   # them cac dinh ke vao OPEN
                Parent[neighbor] = curr

        print(f"Tn: {Tn}")
        print(f"CLOSE: {CLOSE}")
        print(f"OPEN: {OPEN}")
        print(f"Parent: {Parent}")

    print("Goal Unreach!")

if __name__ == '__main__':
    n, adj = readfile('inputs/bfs.adj')

    print(f"Number of nodes: {n}")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    BFS(adj, 0, 6)
    draw_graph(adj)
    draw_directed_graph(adj)