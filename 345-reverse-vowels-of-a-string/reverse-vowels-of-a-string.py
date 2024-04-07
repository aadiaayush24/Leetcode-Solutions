class Solution:
    def reverseVowels(self, s: str) -> str:
        def swap(l, r):
            t = s[l]
            s[l] = s[r]
            s[r] = t
        s =list(s)
        l = len(s)
        left = 0
        rep = []
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        while (left < l):
            if s[left] in vowels:
                rep.append(left)
            left +=1
        
        while (len(rep) > 1):
            swap(rep.pop(), rep.pop(0))
        return ''.join(s)
            
            
