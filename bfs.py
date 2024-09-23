from utils.readfile_bfdfs import readFile
def main():
    n, adj = readFile('inputs/bfs.adj')
    print(f"Number of node: {n}")
if __name__ == '__main__':
    main()