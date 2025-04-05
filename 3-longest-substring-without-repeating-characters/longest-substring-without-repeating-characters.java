class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> letCount = new HashMap<>();
        int left = 0;
        int maxLength = 0;
        for (int right = 0; right < s.length(); right++)    {
            char c = s.charAt(right);
            if (letCount.containsKey(c))   {
                int remCharInd = letCount.get(c);
                while (left <= remCharInd)  {
                    letCount.remove(s.charAt(left++));
                } 
            }
            letCount.put(c, right);
            maxLength = Math.max(right - left + 1, maxLength);
        }
        return maxLength;

    }
}