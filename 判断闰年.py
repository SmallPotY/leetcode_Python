"""
判断给出的年份 n 是否为闰年. 如果 n 为闰年则返回 true

 注意事项
闰年是包含额外一天的日历年. 
如果年份可以被 4 整除且不能被 100 整除 或者 可以被 400 整除, 那么这一年为闰年. --wikipedia
样例
给出 n = 2008 返回 true 
给出 n = 2018 返回 false
"""

def isLeapYear(n):
    if n % 400 == 0 :
        return True
    if n % 4 == 0 :
        if n % 100 != 0:
            return True
    return False


print(isLeapYear(1900))