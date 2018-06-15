"""
给出两个数组a，b。a[i]代表第i部影片的版权费，b[i]代表第i部影片能卖的钱，
现在本金k，问最后最多能赚多少钱。
（每部影片只需要买一次版权，只能卖一次。）
样例:
给出 a = [3,1,5], b = [4,3,100], k = 1，返回 4。
解释：
先买第2部影片，再卖出，再买第1部影片，再卖出，最后本金变为4。

给出 a = [3,1,5], b = [4,3,100], k = 10，返回 108。
解释：
将全部影片买下，卖出，最后本金变为108。
"""

def bigBusiness(a, b, k):
    n = list(zip(a,b))          # 版权与利润  
    m = [(x[1]-x[0],x[0]) for x in n]      # 利润与前提

    while m:

        if k < min([ i[1] for i in m]):
            break
        mnbrak = 0
        for j,i in enumerate(m):
            # print('索引项{},利润{},需要本金{},当前本金{}'.format(j,i[0],i[1],k))
            if i[0] > 0:
                if k >= i[1]:
                    # print('有利润,本金够，计算k值并弹出')
                    k = k + i[0]
                    m.pop(j)
                    break
                else:
                    # print("本金不够，先跳过")
                    mnbrak = 1
            else:
                # print('没利润，弹出')
                m.pop(j)
                break
    print('=====')
    print('最终本金',k)
    return k

bigBusiness([3,1,5], [4,3,100], 1)