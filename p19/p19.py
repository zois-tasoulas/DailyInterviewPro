class graphNode():
    def __init__(self, identifier, adjList=None, visited=False):
        self.id = identifier
        if adjList is None:
            lst = []
        self.adjList = lst
        self.visited = visited

    def addAdjNode(self, nodesTuple):
        for member in nodesTuple:
            self.adjList.append(member)

    def findCycle(self):
        nodeQueue = []
        self.visited = True
        nodeQueue.append(self)
        return traversalDFS(nodeQueue)

def traversalDFS(queue):
    addedBy = {}
    while queue != []:
        currentNode = queue.pop()
        for member in currentNode.adjList:
            if currentNode.id in addedBy and member.id == addedBy[currentNode.id]:
                continue
            if member.visited:
                return True
            member.visited = True
            addedBy[member.id] = currentNode.id
            queue.append(member)
    return False

if __name__ == '__main__':
    n0 = graphNode(0)
    n1 = graphNode(1)
    n2 = graphNode(2)
    n3 = graphNode(3)
    n4 = graphNode(4)
    n5 = graphNode(5)
    n6 = graphNode(6)
    n7 = graphNode(7)
    n0.addAdjNode((n1, n2))
    n1.addAdjNode((n3, n4, n0))
    n2.addAdjNode((n0, n6))
    n3.addAdjNode((n1,))
    n4.addAdjNode((n5, n1, n7, n6))
    n5.addAdjNode((n4,))
    n6.addAdjNode((n4, n2))
    n7.addAdjNode((n4,))
    if n0.findCycle():
        print("The graph has a cycle")
    else:
        print("The graph does not have a cycle")
