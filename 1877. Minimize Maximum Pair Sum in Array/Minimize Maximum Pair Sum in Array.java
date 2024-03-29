class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int maxSum = 0;
        int n = nums.length;
        for (int i = 0; i < n/2; i++){
            if (maxSum < (nums[i] + nums[n-1-i])){
                maxSum = nums[i] + nums[n-1-i];
            }
        }
        return maxSum;
    }
}
