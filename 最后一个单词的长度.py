"""
给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。
样例
给定 s = "Hello World"，返回 5。

"""

def lengthOfLastWord(s):
    # write your code here
    s = s.strip()
    s = s.split(' ')
    return len(s[-1])