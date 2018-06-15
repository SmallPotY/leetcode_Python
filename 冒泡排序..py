"""冒泡排序"""
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        # write your code here
        l_len = len(A)

        while True:
            ok = 1
            for i in range(l_len-1):
                if A[i] > A[i+1]:
                    A[i],A[i+1] = A[i+1],A[i]
                    ok = 0          
            if ok == 1:
                break
        return A
arr = Solution()
print(arr.sortIntegers([3,2,1]))