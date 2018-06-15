"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
"""
import datetime

def findMaxConsecutiveOnes(nums):
    
    n = "".join([str(i) for i in nums])
    n = n.split('0')
    return max([len(i) for i in n])
    


"""
例子
def findMaxConsecutiveOnes(nums):
    result=0
    j=0
    for num in nums:
        if num==1:
            j=j+1
            if j>=result:
                result=j
        else:
            j=0
    return result

"""



n = findMaxConsecutiveOnes([1,1,0,1,1,1])
print(n)