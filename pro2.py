class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):
        # instantiate graph object with graph topology, heuristic values, and start node
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}

    def applyAOStar(self):
        # start a recursive AO* algorithm
        self.aoStar(self.start, False)

    def getNeighbors(self, v):
        # gets the neighbors of a given node
        return self.graph.get(v, '')

    def getStatus(self, v):
        # return the status of a given node
        return self.status.get(v, 0)

    def setStatus(self, v, val):
        # set the status of a given node
        self.status[v] = val

    def getHeuristicNodeValue(self, n):
        # return the heuristic value of a given node
        return self.H.get(n, 0)

    def setHeuristicNodeValue(self, n, value):
        # set the revised heuristic value of a given node
        self.H[n] = value

    def printSolution(self):
        # print the solution graph
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinimumCostChildNodes(self, v):
        # computes the minimum cost of child nodes of a given node v
        minimumCost = 0
        costToChildNodeListDict = {minimumCost: []}
        flag = True

        for nodeInfoTupleList in self.getNeighbors(v):
            cost = 0
            nodeList = []

            for c, weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)

            if flag:
                minimumCost = cost
                costToChildNodeListDict[minimumCost] = nodeList
                flag = False
            else:
                if minimumCost > cost:
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList

        return minimumCost, costToChildNodeListDict[minimumCost]

    def aoStar(self, v, backTracking):
        # AO* algorithm for a start node and backTracking status flag
        if self.getStatus(v) >= 0:
            minimumCost, childNodeList = self.computeMinimumCostChildNodes(v)
            self.setHeuristicNodeValue(v, minimumCost)
            self.setStatus(v, len(childNodeList))

            solved = True

            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved & False

            if solved:
                self.setStatus(v, -1)
                self.solutionGraph[v] = childNodeList

            if v != self.start and backTracking:
                self.aoStar(self.parent[v], True)

            if not backTracking:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)

# Instantiate Graph objects and apply the AO* algorithm
h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}

G1 = Graph(graph1, h1, 'A')
G1.applyAOStar()
G1.printSolution()

h2 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph2 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}

G2 = Graph(graph2, h2, 'A')
G2.applyAOStar()
G2.printSolution()
