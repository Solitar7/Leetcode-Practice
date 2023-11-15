class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);
        int count = 1;
        for (int i = 1; i < arr.length; i++){
            if (arr[i] > count){
                count = count + 1;
            }
        }
        return count;
    }
}
