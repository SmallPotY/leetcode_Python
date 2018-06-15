"""
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。
样例
给出 [1,2,2,1,3,4,3]，返回 4
"""
def singleNumber(A):
    for i in set(A):
        if A.count(i) == 1:
            return i

print(singleNumber([1,2,2,1,3,4,3]))