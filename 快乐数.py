"""
写一个算法来判断一个数是不是"快乐数"。
一个数是不是快乐是这么定义的：
对于一个正整数，每一次将该数替换为他每个位置上的数字的平方和，
然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。
如果可以变为1，那么这个数就是快乐数。
非快乐数最终总会进入到此循环中 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 
"""
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        while n != 1 and n != 4:
            li = str(n)
            n = 0
            for i in li:
                i = int(i) ** 2
                n += i
        if n == 1:
            return True
        else:
            return False
    