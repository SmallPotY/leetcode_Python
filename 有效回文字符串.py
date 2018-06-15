"""
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。
样例
"A man, a plan, a canal: Panama" 是一个回文。

"race a car" 不是一个回文。
"""
def isPalindrome(s):
    slist = list(s)
    for i in slist[:]:
        if not i.isalnum():
            slist.remove(i)
        else:
            slist
    a = ''.join(slist).upper()
    b = a[::-1]
    if a == b:
        return "是一个回文。"
    else:
        return False
        

print(isPalindrome('A man,a pl an, acanal:   Panama'))