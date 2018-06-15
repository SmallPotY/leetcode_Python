"""
给定两个字符串, A 和 B。
的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true
示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """      
        if A == "" and B == "":
            return True      
        elif A =="" and B != "":
            return False
        elif A != "" and B == "":
            return False
            
        A = list(A)
        for i in range(len(A)):
            A.append(A.pop(0))
            if ''.join(A) == B:
                return True
        return False


    # 牛逼的思路:
    # return len(A) == len(B) and B in A + A


N = rotateString('abcde ','abced')
print(N)