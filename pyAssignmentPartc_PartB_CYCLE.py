class Graph:
    def __init__(self, v):
        # No. of vertices of graph
        self.v = v
        # Adjacency List
        self.adj = [0] * v
        for i in range(self.v):
            self.adj[i] = []

    def addEdge(self, i,j):
        self.adj[i].append(j)

    def isCyclic(self):
        visited = [False] * self.v
        helper = [False] * self.v
        for i in range(self.v):
            if visited[i] == False:
                ans = self.DFS(i,visited,helper)
                print(">>>"+str(i)+" "+str(visited)+" "+str(helper))
                if ans == True:
                    return True
        return False


    def DFS(self,i, visited,helper):
        visited[i] = True
        helper[i] = True
        neighbours = self.adj[i]
        for k in range(len(neighbours)):
            curr = neighbours[k]
            if helper[curr] == True:
                return True
            if visited[curr] == False:
                ans = self.DFS(curr,visited,helper)
                if ans == True:
                    return True
        helper[i] = False
        return False


if __name__ == "__main__":
    # No of nodes
    n = 33
    g = Graph(n)

    #g.addEdge(1,2)
    #g.addEdge(2,1)
    g.addEdge(2,3)
    #g.addEdge(3,4)
    #g.addEdge(4,3)
    g.addEdge(4,5)
    #g.addEdge(5,27)
    g.addEdge(6,3)
    g.addEdge(6,7)
    g.addEdge(8,7)
    g.addEdge(8,15)
    g.addEdge(9,5)
    g.addEdge(9,8)
    g.addEdge(10,9)
    g.addEdge(10,14)
    g.addEdge(11,10)
    g.addEdge(12,11)
    g.addEdge(12,24)
    #g.addEdge(13,14)
    #g.addEdge(14,13)
    g.addEdge(14,15)
    #g.addEdge(15,14)
    g.addEdge(15,16)
    g.addEdge(16,17)
    g.addEdge(17,18)
    g.addEdge(19,20)
    g.addEdge(19,18)
    g.addEdge(20,18)
    g.addEdge(21,20)
    g.addEdge(21,18)
    g.addEdge(21,22)
    g.addEdge(22,23)
    g.addEdge(23,24)
    g.addEdge(24,25)
    g.addEdge(25,26)
    #g.addEdge(26,23)
    g.addEdge(27,11)
    g.addEdge(28,21)
    g.addEdge(28,29)
    g.addEdge(30,29)
    g.addEdge(31,32)
    g.addEdge(31,30)
    g.addEdge(32,26)

if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")