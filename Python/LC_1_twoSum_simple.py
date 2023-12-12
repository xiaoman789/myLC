"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""

"""
思路1：暴力 两层for循环
"""
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

"""
思路2：使用哈希
在字典中存储刚刚遍历过的数字
然后在每次访问的时候，查看字典中是否有target-nums[i]的元素存在
相当于两数之和，我在遍历一个数的同时在字典中寻找另一个数
"""
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsMap = dict()
    for i in range(len(nums)):
        if target-nums[i] in numsMap.keys():
            return [numsMap[target-nums[i]],i]
        else:
            numsMap[nums[i]] = i

nums = [3,2,4]
target = 6
print(twoSum2(nums, target))