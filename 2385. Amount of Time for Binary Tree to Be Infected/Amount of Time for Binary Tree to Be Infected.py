# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        paths = [("",root)]
        required = None
        while len(paths) > 0:
            new_paths = []
            for path,node in paths:
                if node.val == start:
                    required = path
                    break
                if node.left != None:
                    new_paths.append((path+"l",node.left))
                if node.right != None:
                    new_paths.append((path+"r",node.right))
            if required != None:
                break
            paths = new_paths
        
        time = 0
        check = root
        while len(required) > 0:
            if required[0] == "l":
                time = max(time,len(required)+self.depth(check.right))
                check = check.left
            else:
                time = max(time,len(required)+self.depth(check.left))
                check = check.right
            required = required[1:]
        return max(time,self.depth(check)-1)
    
    def depth(self,node: Optional[TreeNode]) -> int:
        d = 0
        check = []
        if node != None:
            check.append(node)
        while len(check) > 0:
            next_check = []
            for i in check:
                if i.left != None:
                    next_check.append(i.left)
                if i.right != None:
                    next_check.append(i.right)
            check = next_check
            d += 1
        return d
