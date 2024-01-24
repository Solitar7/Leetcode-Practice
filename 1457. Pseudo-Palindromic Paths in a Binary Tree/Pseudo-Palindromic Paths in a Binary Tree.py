# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = []
        count = dict()
        for i in range(0,10):
            count[i] = 0
        count[root.val] = 1
        result = 0
        paths.append((root,count))
        while len(paths) > 0:
            curr = paths.pop()
            if curr[0].left == None and curr[0].right == None:
                odd = 0
                for i in curr[1]:
                    odd += curr[1][i] % 2
                if odd < 2:
                    result += 1
            else:
                if curr[0].left != None:
                    copy = dict()
                    for i in curr[1]:
                        copy[i] = curr[1][i]
                    copy[curr[0].left.val] += 1
                    paths.append((curr[0].left,copy))
                if curr[0].right != None:
                    copy = dict()
                    for i in curr[1]:
                        copy[i] = curr[1][i]
                    copy[curr[0].right.val] += 1
                    paths.append((curr[0].right,copy))
        return result
