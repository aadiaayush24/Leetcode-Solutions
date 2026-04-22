class Solution {
    static class Pair {
        int val, idx;
        Pair(int val, int idx) {
            this.val=val;
            this.idx=idx;
        }
    }

    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>(Collections.nCopies(n, 0));
        Pair[] arr = new Pair[n];

        for (int i=0; i<n; i++) {
            arr[i] = new Pair(nums[i], i);
        }
        mergeSort(arr, 0, n-1, result);
        return result;
    }

    public void mergeSort(Pair[] arr, int left, int right, List<Integer> result) {
        if (left >= right) return;

        int mid = left+(right-left)/2;
        mergeSort(arr, left, mid, result);
        mergeSort(arr, mid+1, right, result);
        merge(arr, left, mid, right, result);
    }

    public void merge(Pair[] arr, int left, int mid, int right, List<Integer> result) {
        Pair[] temp=new Pair[right-left+1];

        int i=left, j=mid+1, k=0;
        int rightCount=0;
        while (i<=mid && j<=right) {
            if (arr[j].val < arr[i].val) {
                temp[k++]=arr[j++];
                rightCount++;
            }
            else {
                result.set(arr[i].idx, result.get(arr[i].idx)+rightCount);
                temp[k++] = arr[i++];
            }
        }
        while (i <= mid) {
            result.set(arr[i].idx, result.get(arr[i].idx)+rightCount);
            temp[k++]=arr[i++];
        }
        while (j <= right) {
            temp[k++]=arr[j++];
        }

        for (int p=0; p<k; p++) {
            arr[left+p] = temp[p];
        }
    }
}