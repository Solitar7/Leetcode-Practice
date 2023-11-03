class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<String>();
        int last = 0;
        int skip;
        for (int i = 0; i < target.length; i++){
            skip = target[i] - last - 1;
            for (int j = 0; j < skip; j++){
                result.add("Push");
                result.add("Pop");
            }
            result.add("Push");
            last = target[i];
        }
        return result;
    }
}
