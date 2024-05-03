class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        countV1, countV2 = version1.count('.'), version2.count('.')
        v1, v2 = [], []
        str1, str2 = '', ''
        for c in version1:
            if c != '.':
                str1 = str1 + c
            else:
                v1.append(int(str1))
                str1 = ''
        v1.append(int(str1))

        for c in version2:
            if c != '.':
                str2 = str2 + c
            else:
                v2.append(int(str2))
                str2 = ''
        v2.append(int(str2))
            
        if len(v1) < len(v2): 
            while( (len(v1)) != len(v2) ):
                v1.append(0)

        elif len(v1) > len(v2):
            while( (len(v1)) != len(v2) ):
                v2.append(0)
        
        for i in range(0, len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v2[i] > v1[i]:
                return -1
        
        return 0



