"""
一个二维数组，每一行都只有0和1，前面部分是0，后一部分是1，
找到数组里面所有行中最左边的1所在的列数。
样例
给出 arr = [[0,0,0,1],[1,1,1,1]], 返回 0。
解释：
arr[1][0]为所有行中最左边的1，其所在的列为0。

给出 arr = [[0,0,0,1],[0,1,1,1]], 返回 1。
解释：
arr[1][1]为所有行中最左边的1，其所在的列为1。
"""

def getColumn(arr):

    
    for i in xrange(len(arr[0])):
        for j in xrange(len(arr)):
            if arr[j][i] == 1:
                print(i)
                return i


getColumn([[0,0,0,1],[0,1,1,1]])