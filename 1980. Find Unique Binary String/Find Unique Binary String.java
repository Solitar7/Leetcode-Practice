class Solution {
    public String findDifferentBinaryString(String[] nums) {
        String result = "";
        for (int i = 0; i < nums.length; i++){
            if (nums[i].charAt(i) == '0'){
                result = result + "1";
            }
            else{
                result = result + "0";
            }
        }
        return result;
    }
}
