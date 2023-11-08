class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if ((sx == fx) && (sy == fy) && (t == 1)){
            return false;
        }
        int XD = Math.abs(sx - fx);
        int YD = Math.abs(sy - fy);
        if ((XD <= t) && (YD <= t)){
            return true;
        }
        return false;
    }
}
