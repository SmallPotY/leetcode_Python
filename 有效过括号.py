class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            '(':')',
            '[':']',
            '{':'}'
            }

        s = list(s.replace(' ',''))
        if len(s)==1:
            return False
        z = []
        for j, i in enumerate(s):
            if dic.get(i):
                z.append(i)
            else:
                if not z:
                    return False
                if dic.get(z[-1]) != i:
                    return False
                z.pop()
        if len(z):
            return False
        else:
            return True