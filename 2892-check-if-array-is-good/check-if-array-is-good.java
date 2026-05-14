class Solution {
    public boolean isGood(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        // int[] freq=new int[];
        // Arrays.fill(map, 0);
        int maxElem=0;

        for (int num: nums) {
            if (num>maxElem) {
                maxElem=num;
            }
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        if (map.get(maxElem)!=2) {
            return false;
        }
        
        for (int i=1; i<maxElem; i++) {
            if (map.getOrDefault(i, 0) != 1) {
                return false;
            }
        }
        return true;
    }
}