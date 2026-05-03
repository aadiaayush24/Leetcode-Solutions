class Solution {
    public boolean rotateString(String s, String goal) {
        // Same order of characters in two strings, 
        // But multiple ocurences of same character allowed.
        if (s.length() != goal.length()) return false;
        String allComb = s.concat(s);
        if (allComb.contains(goal)) {
            return true;
        }
        return false;
    }
}