import  os
def readfile(filename):
    if not os.path.exists(filename):
        print('File does not exist')
        return None
    with open(filename, 'r') as f:
        n = int(f.readline().strip())

        adj = []
        for idx in range(n):
            line = list(map(int, f.readline().strip().split()))
            adj.append(line)
    return n, adj