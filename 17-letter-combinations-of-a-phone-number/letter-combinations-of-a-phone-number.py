class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def nextLetter(index, word = []):
            if index == len(digits):
                words.append(''.join(word))
                return
            else:
                for i in key_map[int(digits[index])]:
                    word.append(i)
                    nextLetter(index+1, word)
                    word.pop()
                return

        if not digits:
            return []
        key_map = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        key_map = {key: list(value) for key, value in key_map.items()}
        words = []
        nextLetter(0)
        return words



        