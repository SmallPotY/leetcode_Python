"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        yhsj = [[1],[1,1]]

        if numRows:
            if numRows == 1:
                return [[1]]
            elif numRows == 2:
                return yhsj
            else:
                for i in range(3,numRows+1):
                    klb = [1,]
                    k =0
                    for j in range(1, i-1):
                        a = yhsj[i-2][k] 
                        b = yhsj[i-2][k+1]
                        k = k+1
                        klb.append(a+b)
                    klb.append(1)
                    yhsj.append(klb)

                return yhsj
        else:
            return []