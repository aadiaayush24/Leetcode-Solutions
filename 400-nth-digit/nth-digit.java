class Solution {
    public int findNthDigit(int n) {
        long start = 1, count = 9, d = 1;

        while (n > count*d) {
            n -= (count*d++);
            count *= 10;
            start *= 10;
        }

        long number = start + (n-1)/d;
        int digitIndex = (int)((n-1)%d);
        
        return String.valueOf(number).charAt(digitIndex) - '0';
    }
}