class Solution {
    public int findKthPositive(int[] arr, int k) {
        int pos=1;
        int i=0;
        while (i<arr.length && k!=0) {
            if (arr[i] != pos) {
                k--;
            }
            else {
                i++;
            }
            // System.out.println("i: "+i+" pos:"+pos+" k:"+k);
            pos++;
        }
        while (k!=0) {
            k--;
            pos++;
            // System.out.println("pos:"+pos+" k:"+k);
        }
        return pos-1;

    }
}