# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        check = [root]
        count = dict()
        while(len(check) > 0):
            current = check.pop()
            if (count.get(current.val) == None):
                count[current.val] = 1
            else:
                count[current.val] = count[current.val] + 1
            if not (current.left == None):
                check.append(current.left)
            if not (current.right == None):
                check.append(current.right)
        
        modeNum = 0
        mode = []
        for i in count.keys():
            if (count[i] > modeNum):
                modeNum = count[i]
                mode = [i]
            elif (count[i] == modeNum):
                mode.append(i)
        
        return mode
