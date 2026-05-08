class PrimsMST:
    def __init__(self, adj, num_vertices):
        self.adj = adj
        self.n = num_vertices

    def prim(self, source):
        
        # initialize all distances to infinity
        D = {v: float('inf') for v in self.adj}
        parent = {v: None for v in self.adj}
        visited = set()
        
       
        D[source] = 0
        
        while len(visited) < self.n:
            
            # pick unvisited vertex with minimum distance
            u = None
            for v in self.adj:
                if v not in visited:
                    if u is None or D[v] < D[u]:
                        u = v
            
            # add u to visited
            visited.add(u)
            
            # update neighbors of u
            for neighbor, weight in self.adj[u]:
                if neighbor not in visited:
                    if weight < D[neighbor]:
                        D[neighbor] = weight
                        parent[neighbor] = u
        
        
        total_weight = 0
        print("MST Edges:")
        for v in parent:
            if parent[v] is not None:
                print(parent[v], "--", v, " weight:", D[v])
                total_weight += D[v]
        print("Total Weight:", total_weight)
