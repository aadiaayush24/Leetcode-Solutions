class Solution {
    public int[] separateDigits(int[] nums) {
        List<Integer> digits = new ArrayList<>();

        for (int i=nums.length-1; i>=0; i--) {
            int num=nums[i];
            while (num!=0) {
                digits.add(num%10);
                num/=10;
            }
        }
        Collections.reverse(digits);
        int[] res=digits.stream().mapToInt(i -> i).toArray();
        return res;
    }
}