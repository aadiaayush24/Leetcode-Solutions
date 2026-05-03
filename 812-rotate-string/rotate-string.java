class Solution {
    public boolean rotateString(String s, String goal) {
        // Same order of characters in two strings, 
        // But multiple ocurences of same character allowed.
        
        for (int i=0; i<s.length(); i++) {
            String nStr = s.substring(i).concat(s.substring(0, i));
            
            if (goal.equals(nStr)) {
                return true;
            }
        }
        return false;
    }
}