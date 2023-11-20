class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int[] count = new int[3];
        int result = 0;
        int cost = 0;
        for (int i = 0; i < travel.length; i++){
            result = result + garbage[i].length();
            cost = cost + travel[i];
            if(garbage[i+1].contains("M")){
                count[0] = cost;
            }
            if(garbage[i+1].contains("P")){
                count[1] = cost;
            }
            if(garbage[i+1].contains("G")){
                count[2] = cost;
            }
        }
        result = result + garbage[garbage.length-1].length() + count[0] + count[1] + count[2];
        return result;
    }
}
