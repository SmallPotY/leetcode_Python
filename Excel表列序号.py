"""
与 Excel表列名称 问题类似。

给定一个Excel表格中的列名称，返回其相应的列序号。

示例:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
def titleToNumber(s):
    abc = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
    }
    a = 0
    for i in range(len(s)):
        a = a + (26 ** i) * abc.get(s[::-1][i])
    return a

N = titleToNumber('C')
print(N)