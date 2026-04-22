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
        int[] result = new int[n];
        Arrays.fill(result, 0);
        Pair[] arr = new Pair[n];

        for (int i=0; i<n; i++) {
            arr[i] = new Pair(nums[i], i);
        }
        mergeSort(arr, 0, n-1, result);
        List<Integer> res=Arrays.stream(result).boxed().toList();
        return res;
    }

    public void mergeSort(Pair[] arr, int left, int right, int[] result) {
        if (left >= right) return;

        int mid = left+(right-left)/2;
        mergeSort(arr, left, mid, result);
        mergeSort(arr, mid+1, right, result);
        merge(arr, left, mid, right, result);
    }

    public void merge(Pair[] arr, int left, int mid, int right, int[] result) {
        Pair[] temp=new Pair[right-left+1];

        int i=left, j=mid+1, k=0;
        int rightCount=0;
        while (i<=mid && j<=right) {
            if (arr[j].val < arr[i].val) {
                temp[k++]=arr[j++];
                rightCount++;
            }
            else {
                result[arr[i].idx] += rightCount;
                temp[k++] = arr[i++];
            }
        }
        while (i <= mid) {
            result[arr[i].idx] += rightCount;
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