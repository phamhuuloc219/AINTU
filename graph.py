import networkx as nx
import matplotlib.pyplot as plt


# DO THI VO HUONG
def draw_graph(adj):
    # Khoi tao do thi
    G = nx.Graph()

    # Xac dinh so dinh
    n = len(adj)

    # Tao anh xa tu cac so (0, 1, 2, ...) thanh cac ky tu (A, B, C, ...)
    labels = {i: chr(65 + i) for i in range(n)}  # 65 = ASCII 'A'

    # Them cac canh vao do thi cua ma tran ke
    for i in range(n):
        for j in range(i, n):
            if adj[i][j] == 1:
                G.add_edge(labels[i], labels[j])

    # Ve do thi vo huong
    pos = nx.spring_layout(G)  # Tinh cac vi tri de ve do thi
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, edge_color='gray')

    plt.show()


# DO THI CO HUONG
def draw_directed_graph(adj):
    # Khoi tao di thi
    G = nx.DiGraph()

    # Xac dinh so dinh
    n = len(adj)

    # Tao anh xa tu cac so (0, 1, 2, ...) thanh cac ky tu (A, B, C, ...)
    labels = {i: chr(65 + i) for i in range(n)}  # 65 la ma ASCII cua 'A'

    # Them cac canh tu cac dinh da co
    for i in range(n):
        for j in range(n):  # Trong đồ thị có hướng, xét tất cả các cặp (i, j)
            if adj[i][j] == 1:
                G.add_edge(labels[i], labels[j])

    # Ve do thi co huong
    pos = nx.spring_layout(G)  # Tinh vi tri cac dinh de ve do thi
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, edge_color='gray', arrows=True)

    plt.show()