"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
示例1:

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
"""



def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    key1= ['q','w','e','r','t','y','u','i','o','p'] 
    key2 = ['a','s','d','f','g','h','j','k','l'] # 10 18
    key3 = ['z','x','c','v','b','n','m']
    keylist = key1+key2+key3
    for i in words[:]:
        tf = ''
        for j in i:
            if keylist.index(j.lower()) > 18:
                tf = tf + 'c'
            elif keylist.index(j.lower()) < 10:
                tf = tf + 'a'
            else:
                tf = tf + 'b'
        if len(set(tf)) != 1 :
            words.remove(i)
    return words

n= findWords(["Hello", "Alaska", "Dad", "Peace"])
print(n)