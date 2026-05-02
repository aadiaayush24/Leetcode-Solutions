class Solution {
    public boolean checkValid(int n) {
        boolean hasValidDigit= false;
        while(n!=0) {
            int r = n%10;
            if (r==3 || r==4 || r==7) {
                return false;
            }
            else if (r==2 || r==5 || r==6 || r==9) {
                hasValidDigit=true;
            }
            n= n/10;
        }
        return hasValidDigit;
    }
    public int rotatedDigits(int n) {
//        From the range of 1 to N, remove:
//        a) numbers having digit 3, 4, 7
//        b) numbers having only 0,1 and 8
    int count = 0; 
    for (int i=1; i<=n; i++) {
       if(checkValid(i)) {
        count++;
       }
    }
    return count;
    }
}