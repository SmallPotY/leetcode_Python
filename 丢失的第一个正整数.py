"""
给出一个无序的整数数组，找出其中没有出现的最小正整数。
样例
如果给出 [1,2,0], return 3
如果给出 [3,4,-1,1], return 2
"""

def firstMissingPositive(A):
    if A:
        maxa = max(A)


        B = list(range(1,maxa+1))    
        print('生成列表B',B)
        print('原始列表A',A)
        z = set(A)
        x = set(B)

        c = x.difference(z)
        print('列表B中有而A没有',c)
        if c:
            for i in c:
                if i >0 :
                    print('i>0',i)
                    return i
        else:
            print('c为空',maxa)
            if maxa < 0:
                return 1
            else:
                return maxa + 1


    return 1

n = firstMissingPositive([-4,-2])
print('结果是',n)
