/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        std::vector<TreeNode*> check;
        int result = 0;
        check.push_back(root);
        while (!check.empty()){
            TreeNode* current = check[check.size()-1];
            check.pop_back();
            if (current -> val >= low && current -> val <= high){
                result += current -> val;
            }
            if (current -> left != NULL){
                check.push_back(current -> left);
            }
            if (current -> right != NULL){
                check.push_back(current -> right);
            }
        }
        return result;
    }
};
