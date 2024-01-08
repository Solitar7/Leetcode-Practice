# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        check = [root]
        result = 0
        while len(check) > 0:
            current = check.pop()
            if current.val < low or current.val > high:
                pass
            else:
                result += current.val
            if current.left != None:
                check.append(current.left)
            if current.right != None:
                check.append(current.right)
        return result
