"""
给一字符串数组, 将 错位词(指相同字符不同排列的字符串) 分组
给出 strs = ["eat", "tea", "tan", "ate", "nat", "bat"],
返回 
[
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
"""
def groupAnagrams(strs):
    new_strs = []
    return_strs = []
    for i in strs:
        a = list(i)
        a.sort()
        a = "".join(a)
        new_strs.append(a)
    
    for i in set(new_strs):
        strs_item =[]
        for j in strs:
            q = list(j)
            q.sort()
            if "".join(q) == i:
                strs_item.append(j)
        return_strs.append(strs_item)

    return return_strs



groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])