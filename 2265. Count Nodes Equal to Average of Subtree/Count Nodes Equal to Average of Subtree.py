# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        checklist = dict()
        dfs = [root]
        while (len(dfs) > 0):
            current_node = dfs.pop()
            checklist[current_node] = False
            if (current_node.left != None):
                dfs.append(current_node.left)
            if (current_node.right != None):
                dfs.append(current_node.right)

        dfs = [root]
        node_total = [root.val]
        node_count = [1]
        while (len(dfs) > 0):
            left_node = dfs[-1].left
            right_node = dfs[-1].right
            if (left_node != None):
                if (not checklist[left_node]):
                    dfs.append(left_node)
                    node_total.append(left_node.val)
                    node_count.append(1)
                    continue
            if (right_node != None):
                if (not checklist[right_node]):
                    dfs.append(right_node)
                    node_total.append(right_node.val)
                    node_count.append(1)
                    continue
            current_node = dfs.pop()
            current_total = node_total.pop()
            current_count = node_count.pop()
            if (current_total // current_count == current_node.val):
                result = result + 1
            checklist[current_node] = True
            if ((len(node_total) > 0) and (len(node_count) > 0)):
                node_total[-1] = node_total[-1] + current_total
                node_count[-1] = node_count[-1] + current_count
        return result
