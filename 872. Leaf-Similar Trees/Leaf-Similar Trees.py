# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        one = [root1]
        two = [root2]
        leaf_one = []
        leaf_two = []
        while len(one) > 0:
            current = one.pop()
            if current.left == None and current.right == None:
                leaf_one.append(current.val)
            else:
                if current.left != None:
                    one.append(current.left)
                if current.right != None:
                    one.append(current.right)
        while len(two) > 0:
            current = two.pop()
            if current.left == None and current.right == None:
                leaf_two.append(current.val)
            else:
                if current.left != None:
                    two.append(current.left)
                if current.right != None:
                    two.append(current.right)
        return leaf_one == leaf_two
