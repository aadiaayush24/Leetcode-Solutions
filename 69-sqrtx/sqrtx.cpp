class Solution {
public:
    bool isSquareGreaterThanN(long x, long k) {
        if (k*k >= x)   {
            return true;
        }
        return false;
    }
    int mySqrt(int x) {
        long start = 1;
        long end = x;

        while (start <= end)    {
            long mid = start + (end-start)/2;
            if (isSquareGreaterThanN(x, mid))   {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }
        if (static_cast<long>(start*start) == static_cast<long>(x))   {
            return start;
        } 
        return start-1;
    }
};