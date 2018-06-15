"""
给定一个长为n的数组Ages, 其中第i个元素表示第i个人的年龄。求这个n个人，发送的好友请求的总数。其中，
1. 如果Age(B) <= (1/2)Age(A) + 7, A不会给B发请求
2. 如果Age(B) > Age(A)， A不会给B发请求
3. 如果Age(B) < 100 and Age(A) > 100, A不会给B发请求
4. 不满足1，2，3，则A会给B发请求
样例
给出Ages = [10,39,50], 返回 1。
解释：
只有年龄为50的人会给年龄为39的人发送好友请求。
给出Ages = [101,79,102], 返回 1。
解释：
只有年龄为102的人会给年龄为101的人发送好友请求。
"""

def friendRequest(ages):
    count = 0
    for i,j in enumerate(ages):
        
        for x,y in enumerate(ages):
            print('比较开始',j,y,end='——————')
            if i != x:
                if j <= (1/2)*y +7:
                    print('{}<=(1/2)*{}+7'.format(j,y))
                    continue
                if j > y:
                    print('{}>{}'.format(j,y))
                    continue
                if j< 100 and y>100:
                    print('{}<100 and {}>100'.format(j,y))
                    continue
                print('比较通过，+1')
                count +=1
            else:
                print('比较者本身,忽略')
    return count

n = friendRequest([101,79,102])
