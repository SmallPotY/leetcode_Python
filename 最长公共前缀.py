"""
给k个字符串，求出他们的最长公共前缀(LCP)
样例
在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"
"""

def longestCommonPrefix(strs):
    LCP = []
    lenlist = [len(i) for i in strs]
    
    for j in range(min(lenlist)):
        dc = []
        for i in strs:
            # print(i[j])
            dc.append(i[j])
        if len(set(dc)) == 1:
            # print(set(dc),i[j])
            LCP.append(i[j])
        else:
            return ''.join(LCP)

    return ''.join(LCP)

n = longestCommonPrefix(["A","A"] )
print(n)