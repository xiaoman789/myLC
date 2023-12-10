"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
"""



def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_ls = [0]*26
    t_ls = [0]*26
    for i in range(0, len(s)):
        s_ls[ord(s[i]) - 97] += 1
        t_ls[ord(t[i]) - 97] += 1
    if s_ls == t_ls:
        return True
    return False


# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
# print(ord('a'))
print(isAnagram(s, t))
