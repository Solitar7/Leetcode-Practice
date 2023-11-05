class Solution {
    public int getWinner(int[] arr, int k) {
        int curr = arr[0];
        int wins = 0;
        int i = 1;
        while (i < arr.length){
            if (curr > arr[i]){
                wins = wins + 1;
            }
            else{
                curr = arr[i];
                wins = 1;
            }
            if (wins == k){
                return curr;
            }
            i = i + 1;
        }
        return curr;
    }
}
