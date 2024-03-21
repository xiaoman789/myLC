"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true
"""

from collections import Counter
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransomNoteList = list(ransomNote)
    magazineList = list(magazine)
    mCount = Counter(magazineList)
    # print(magazineList)
    # print(ransomNoteList)
    # print(mCount)
    for i in ransomNoteList:
        print(i)
        if mCount[i] == 0 or i not in magazineList:
            return False
        mCount[i]  -= 1
        print(mCount)
    return True

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))