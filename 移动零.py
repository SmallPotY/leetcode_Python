"""
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

注意事项:

必须在原数组上操作，不要为一个新数组分配额外空间。
尽量减少操作总数。
 
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # if nums.count(0):   # 避免列表中没有0值时报错           
    #     tks = nums.index(0)      
    #     for i in range(tks,len(nums)):
    #         if nums[i] != 0:
    #             n = nums.index(0)
    #             nums[i], nums[n] = nums[n], nums[i]
    # return nums

    # 这样运行速度会快很多
    l = len(nums)
    i = 0
    for xxx in range(l):
        
        if nums[i] ==0 :
            nums.pop(i)
            nums.append(0)
            i -= 1
        i += 1
    return nums

n = moveZeroes([0,1,0,3,12])
print(n)