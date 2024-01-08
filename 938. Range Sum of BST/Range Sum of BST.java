/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        ArrayList<TreeNode> check = new ArrayList<TreeNode>();
        int result = 0;
        check.add(root);
        while (!check.isEmpty()){
            TreeNode current = check.remove(check.size()-1);
            if (current.val >= low && current.val <= high){
                result += current.val;
            }
            if (current.left != null){
                check.add(current.left);
            }
            if (current.right != null){
                check.add(current.right);
            }
        }
        return result;
    }
}
