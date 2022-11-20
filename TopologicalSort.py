# The topological sort algorithm takes a directed graph and 
# returns an array of the nodes where each node appears before all the nodes it points to. 
# The ordering of the nodes in the array is called a topological ordering. 

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = dict() # Dictionary to store graph
        for i in range(self.V):
            self.graph[i] = []

    # Adds an edge to an undirected graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Performs topological sort on the graph
    def sortNodes(self):
        in_degree = [0]*(self.V) # Stores in-degree of all nodes

        # Traverse adjacency lists to fill indegrees of nodes
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create a queue and append all nodes with indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        
        count = 0
        sorted_nodes = []

        # Remoove nodes from queue and add to sorted_nodes
        # Check if adjacent nodes of removed node become 0
        # If so add them to queue
        while queue:
            u = queue.pop(0)
            sorted_nodes.append(u)
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
                    queue.sort()
                    
            count += 1

        # Check for cycles
        if count != self.V:
            print("A cycle exists in the graph")
            exit()
        else:
            return sorted_nodes


if __name__ == '__main__':
    edges = [[0, 1], [0, 3], [3, 1], [3, 4], [4, 5], [1, 2]]
    nodes = 6

    # Construct graph 
    g = Graph(nodes)
    for u,v in edges:
        g.addEdge(u,v)

    sorted_nodes = g.sortNodes()

    print(sorted_nodes)