from TopologicalSort import *

if __name__ == "__main__":
    with open("E:\DataStructure2\ds2lab4\inputForTopologicalSort.txt", "r") as f:
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
