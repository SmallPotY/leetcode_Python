"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = []
        base = ord('A')
        while n:
            n, r = divmod(n-1, 26)
            result.append(chr(base+r))
        return ''.join(result[::-1])