from PrimsMST import PrimsMST

if __name__ == "__main__":
    with open("inputForPrim.txt", "r") as f:   
        input_data = f.read().split()

    idx = 0
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
