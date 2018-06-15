"""
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。
注意这里下标的范围是 0 到 n-1。
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
"""
def twoSum(numbers, target):
    # write your code here
    for j, i in enumerate(numbers):
        keyv = target - i
        if keyv in numbers:
            for a,b in enumerate(numbers):
                if a != j and b == keyv:
                    return_list = [j,a] 
                    return return_list


print(twoSum([2,7,11,15], 9))