from collections import deque

class TopologicalSort:
    def __init__(self, adj):

        self.adj = adj
        self.deg = {node: 0 for node in self.adj}
        
        for node in self.adj:
            for neighbor in self.adj[node]:
                if neighbor not in self.deg:
                    self.deg[neighbor] = 0
                self.deg[neighbor] += 1

    def topology(self):

        self.topo = deque()
        self.graph = []
        
        for i in self.deg:
            if self.deg[i] == 0:
                self.topo.append(i)

        while self.topo:
            curr_node = self.topo.popleft()
            self.graph.append(curr_node)
            
            for new_node in self.adj.get(curr_node, []):
                self.deg[new_node] -= 1
                if self.deg[new_node] == 0:
                    self.topo.append(new_node)
                    
        if len(self.graph) != len(self.deg):
            print("graph has cycle")
            return []
        for i in range(len(self.graph)):
            print(self.graph[i], end=" ")
        return self.graph
