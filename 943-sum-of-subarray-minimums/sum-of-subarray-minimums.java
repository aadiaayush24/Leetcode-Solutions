class Solution {
    public int[] getNSE(int[] arr, int n) {
        int[] nse = new int[n];
        Deque<Integer> dq = new ArrayDeque<Integer>();

        for(int i = n-1; i>=0; i--) {
            while (!dq.isEmpty() && arr[dq.peekLast()] >= arr[i]) {
                dq.removeLast();
            }
            if (dq.isEmpty()) {
                nse[i] = n;
            }
            else {
                nse[i] = dq.peekLast();
            }
            dq.add(i);
        }
        return nse;
    }

    public int[] getPSE(int[] arr, int n) {
        int[] pse = new int[n];
        Deque<Integer> dq = new ArrayDeque<Integer>();

        for(int i = 0; i<n; i++) {
            while (!dq.isEmpty() && arr[dq.peekLast()] > arr[i]) {
                dq.removeLast();
            }
            if (dq.isEmpty()) {
                pse[i] = -1;
            }
            else {
                pse[i] = dq.peekLast();
            }
            dq.add(i);
        }
        return pse;
    }
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] nse = getNSE(arr, n);
        int[] pse = getPSE(arr, n);
        long res = 0;
        final long MOD = 1_000_000_007;
        for (int i = 0; i<n; i++) {
            long left = nse[i]-i;
            long right = i-pse[i];
            long numElems = (right*left)%MOD;
            long contrib = (numElems*arr[i])%MOD;
            res = (long)((res + contrib)%MOD);
        }
        return (int)res;

    }
}