class Node:
    def __init__(self,data):
        self.data = data
        self.one = None
        self.two = None

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ends = dict()
        for i in adjacentPairs:
            if ((i[0] in ends) and (i[1] in ends)):
                ends[i[0]].two = ends[i[1]]
                ends[i[1]].two = ends[i[0]]
                ends.pop(i[0])
                ends.pop(i[1])
            elif ((i[0] not in ends) and (i[1] not in ends)):
                ends[i[0]] = Node(i[0])
                ends[i[1]] = Node(i[1])
                ends[i[0]].one = ends[i[1]]
                ends[i[1]].one = ends[i[0]]
            elif ((i[0] not in ends) and (i[1] in ends)):
                ends[i[0]] = Node(i[0])
                ends[i[0]].one = ends[i[1]]
                ends[i[1]].two = ends[i[0]]
                ends.pop(i[1])
            else:
                ends[i[1]] = Node(i[1])
                ends[i[1]].one = ends[i[0]]
                ends[i[0]].two = ends[i[1]]
                ends.pop(i[0])
        result = []
        keys = list(ends.keys())
        curr = ends[keys[0]]
        result.append(curr.data)
        prev = curr.data
        if (curr.one == None):
            curr = curr.two
        else:
            curr = curr.one
        while (not curr == None):
            result.append(curr.data)
            if (curr.one.data == prev):
                prev = curr.data
                curr = curr.two
            else:
                prev = curr.data
                curr = curr.one
        return result
