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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<TreeNode*> one;
        vector<TreeNode*> two;
        vector<int> leafOne;
        vector<int> leafTwo;
        one.push_back(root1);
        two.push_back(root2);
        TreeNode current;
        while(!one.empty()){
            current = *one[one.size()-1];
            one.pop_back();
            if (current.left == NULL && current.right == NULL){
                leafOne.push_back(current.val);
            }
            else{
                if (current.left != NULL){
                    one.push_back(current.left);
                }
                if (current.right != NULL){
                    one.push_back(current.right);
                }
            }
        }
        while(!two.empty()){
            current = *two[two.size()-1];
            two.pop_back();
            if (current.left == NULL && current.right == NULL){
                leafTwo.push_back(current.val);
            }
            else{
                if (current.left != NULL){
                    two.push_back(current.left);
                }
                if (current.right != NULL){
                    two.push_back(current.right);
                }
            }
        }
        if (leafOne.size() != leafTwo.size()){
            return false;
        }
        for(int i = 0; i < leafOne.size(); i++){
            if (leafOne[i] != leafTwo[i]){
                return false;
            }
        }
        return true;
    }
};
