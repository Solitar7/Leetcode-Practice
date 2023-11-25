class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        int absSum = 0;
        int[] result = new int[n];
        for(int i = 0; i < nums.length; i++){
            absSum = absSum + nums[i];
        }
        for(int i = 0; i < nums.length; i++){
            result[i] = absSum + i * nums[i] - (n-i) * nums[i];
            absSum = absSum - 2 * nums[i];
        }
        return result;
    }
}
