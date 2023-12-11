"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。


示例 1：
输入：n = 19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

示例 2：
输入：n = 2
输出：false
"""

"""
思路；暴力解法
"""

# 暴力解法：
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    ls = list(map(int, list(str(n))))
    for i in range(100):
        s = 0
        print(ls)
        for j in range(len(ls)):
            s += ls[j]**2
        if s == 1:
            return True
        print(s)
        ls = list(map(int, list(str(s))))
    return False


n = 2
print(isHappy(n))

