class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int result = 0;
        int i = piles.length / 3;
        while(i < piles.length){
            result = result + piles[i];
            i = i + 2;
        }
        return result;
    }
}
