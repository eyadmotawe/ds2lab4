from TopologicalSort import *
from PrimsMST import PrimsMST

def run_topological_sort():
    with open("E:\\DataStructure2\\ds2lab4\\inputForTopologicalSort.txt", "r") as f:
        input_data = f.read().split()
    
    if input_data:
        n = int(input_data[0])
        m = int(input_data[1])
        
        adj = {i: [] for i in range(1, n + 1)}
        
        idx = 2
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            adj[u].append(v)
            idx += 2
            
        ts = TopologicalSort(adj)
        ts.topology()

def run_mst():
    with open("E:\DataStructure2\ds2lab4\inputForPrim.txt", "r") as f:   
        input_data = f.read().split()

    idx = 0
    if not input_data:
        return
        
    n = int(input_data[idx]); idx += 1  # number of vertices
    m = int(input_data[idx]); idx += 1  # number of edges
    s = int(input_data[idx]); idx += 1  # source vertex

    adj = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u = int(input_data[idx]);     idx += 1
        v = int(input_data[idx]);     idx += 1
        w = int(input_data[idx]);     idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))  

    mst = PrimsMST(adj, n)
    mst.prim(s)

if __name__ == "__main__":
    print("Which algorithm would you like to run?")
    print("1: Topological Sort")
    print("2: Minimum Spanning Tree (Prim's Algorithm)")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        run_topological_sort()
    elif choice == '2':
        run_mst()
    else:
        print("Invalid choice. Please enter 1 or 2.")
