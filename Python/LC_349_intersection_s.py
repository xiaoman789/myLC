"""
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

思路：
先把两个数组转换为set再转换为list减少重复元素
选择长度较小的数组a，遍历元素
如果a中的元素再b中出现
添加进结果数组
"""


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    list1 = list(set(nums1))
    list2 = list(set(nums2))
    ls = []
    if len(list1) <= len(list2):
        for i in list1:
            if i in list2:
                ls.append(i)
    else:
        for i in list2:
            if i in list1:
                ls.append(i)
    return ls

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))
