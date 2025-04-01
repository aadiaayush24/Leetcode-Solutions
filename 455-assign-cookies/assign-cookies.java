class Solution {
    public int satisfy(int childIndex, int cookieIndex, int[] g, int[] s){
        if (cookieIndex == -1 || childIndex == -1)  {
            return 0;
        }
        if (g[childIndex] > s[cookieIndex]) {
            return satisfy(childIndex - 1, cookieIndex, g, s);
        }
        else {
            return 1 + satisfy(childIndex - 1, cookieIndex - 1, g, s);
        }
    }
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        return satisfy(g.length-1,s.length-1, g, s);
    }
}