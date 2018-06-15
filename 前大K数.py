"""
实现一个数据结构，提供下面两个接口
1.add(number) 添加一个元素
2.topk() 返回前K大的数

s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]

"""

class Solution():
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.klist = []
        self.k = k
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        self.klist.append(num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        self.klist.sort(reverse=True)
        if len(self.klist) > self.k:
            return self.klist[:self.k]
        else:
            return self.klist

s = Solution(3)
s.add(3)
s.add(10)
print(s.topk())

s.add(1000)
s.add(-99)
print(s.topk())

s.add(4)
print(s.topk())