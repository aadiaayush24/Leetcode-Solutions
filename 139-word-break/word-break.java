class Solution {
    public boolean checkWordInDictionary(String word, Map<String, Boolean> visited, Set<String> wordSet)    {
        if (word.isEmpty()) {
            return true;
        }
        if (visited.containsKey(word))  {
            return visited.get(word);
        }
        StringBuilder subWord = new StringBuilder();
        for (int i = 0; i < word.length(); i++)   {
            subWord.append(word.charAt(i));
            if (wordSet.contains(subWord.toString()))    {
                visited.put(subWord.toString(), true);
                if (i+1 == word.length()) {
                    return true;
                }
                if (checkWordInDictionary(word.substring(i+1), visited, wordSet))  {
                    return true;
                }
            }
            else    {
                visited.put(subWord.toString(), false);
            }
        }
        return false;
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        Map<String, Boolean> visited = new HashMap<String, Boolean>();
        Set<String> wordSet = new HashSet<String>(wordDict);
        return checkWordInDictionary(s, visited, wordSet);
    }
}