class Solution {
    public boolean checkPerfSq(int start, int end, int num) {
        if (end < start) {
            return false;
        }
        int mid=start + (end-start)/2;
        // System.out.println(mid);
        if (mid*mid == num) return true;
        else if (mid <= num/mid) {
            return checkPerfSq(mid+1 ,end, num);
        }
        else {
            return checkPerfSq(start, mid-1, num);
        }
    }
    public boolean isPerfectSquare(int num) {
        if (num==1) return true;
        return checkPerfSq(1, num/2, num);
    }
}