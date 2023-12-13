"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。


示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # 纵向扫描
    # 先对数组里的字符串排序，长度最小的字符串放在最前面
    strList = sorted(strs)
    for i in range(len(strList[0])):
        for j in range(len(strList)):
            if strList[j][i] != strList[0][i]:
                return strList[0][0:i]
    return ""

# strs = ["flower","flow","flight"]
strs = ["",""]
print(longestCommonPrefix(strs))