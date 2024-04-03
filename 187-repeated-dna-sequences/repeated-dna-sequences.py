class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = {}
        for pos in range(len(s)-9):
            seq = s[pos:pos+10]
            print(seq)
            if seq in dna.keys():
                dna[seq] += 1
            else:
                dna [seq] = 1
        
        res = [key for key, val in dna.items() if val > 1]
        return res