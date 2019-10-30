def courseOrder(prerequisites):
        cycle = False
        nodeState = {} # 0 = unseen, 1 = seen, 2 = explored
        for course in prerequisites:
            nodeState[course] = 0
        validOrder = []
        for course in prerequisites:
            if nodeState[course] == 0:
                nodeState[course] == 1
                cycle = dfs(course, prerequisites, nodeState, validOrder)
            if cycle:
                break
        return validOrder if not cycle else []
    
def dfs(node, adjList, nodeState, stack):
    for neighbor in adjList[node]:
        if nodeState[neighbor] == 0:
            nodeState[neighbor] = 1
            if dfs(neighbor, adjList, nodeState, stack):
                return True
        elif nodeState[neighbor] == 1:
            return True
        #elif nodeState[neighbor] == 2: pass
    stack.append(node)
    nodeState[node] = 2
    return False


if __name__ == '__main__':
    prereqs = {
        'CSC400': ['CSC100'],
        'CSC300': ['CSC200', 'CSC400'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    print(courseOrder(prereqs))
