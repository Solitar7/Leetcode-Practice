class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int maxL = -1;
        int minR = -1;
        if (right.length != 0){
            minR = right[0];
            for (int i = 0; i < right.length; i++){
                if (minR > right[i]){
                    minR = right[i];
                }
            }
        }
        if (left.length != 0){
            maxL = left[0];
            for (int i = 0; i < left.length; i++){
                if (maxL < left[i]){
                    maxL = left[i];
                }
            }
        }
        if (minR == -1){
            return maxL;
        }
        int result = n - minR;
        if (result < maxL){
            result = maxL;
        }
        return result;
    }
}
