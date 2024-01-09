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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<TreeNode> one = new ArrayList<TreeNode>();
        ArrayList<TreeNode> two = new ArrayList<TreeNode>();
        one.add(root1);
        two.add(root2);
        ArrayList<Integer> leafOne = new ArrayList<Integer>();
        ArrayList<Integer> leafTwo = new ArrayList<Integer>();
        TreeNode current;
        while (one.size() > 0){
            current = one.remove(one.size()-1);
            if (current.left == null && current.right == null){
                leafOne.add(current.val);
            }
            else{
                if (current.left != null){
                    one.add(current.left);
                }
                if (current.right != null){
                    one.add(current.right);
                }
            }
        }
        while (two.size() > 0){
            current = two.remove(two.size()-1);
            if (current.left == null && current.right == null){
                leafTwo.add(current.val);
            }
            else{
                if (current.left != null){
                    two.add(current.left);
                }
                if (current.right != null){
                    two.add(current.right);
                }
            }
        }
        if(leafOne.size() != leafTwo.size()){
            return false;
        }
        for (int i = 0; i < leafOne.size(); i++){
            if (leafOne.get(i) != leafTwo.get(i)){
                return false;
            }
        }
        return true;
    }
}
