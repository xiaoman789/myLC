"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

示例 1：
输入：s = "hello"
输出："holle"

示例 2：
输入：s = "leetcode"
输出："leotcede"
"""

# 双指针法
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    sList = list(s)
    Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    VowelsList = []
    # 先扫描一遍哪些位置上是元音元素
    for i in range(len(s)):
        if s[i] in Vowels:
            VowelsList.append(i)

    left = 0
    right = len(VowelsList) - 1
    while (left < right):
        temp = sList[VowelsList[left]]
        sList[VowelsList[left]] = sList[VowelsList[right]]
        sList[VowelsList[right]] = temp
        left += 1
        right -= 1
    s = "".join(sList)
    return s
s = "hello"
print(reverseVowels(s))