# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node == None:
                return ""
            result = str(node.val)
            if node.left == None and node.right == None:
                return result
            result = result + "("
            result = result + dfs(node.left)
            result = result + ")"
            if node.right == None:
                return result
            result = result + "("
            result = result + dfs(node.right)
            result = result + ")"
            return result
        return dfs(root)
            
