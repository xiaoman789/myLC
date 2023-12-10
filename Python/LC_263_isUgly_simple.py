"""
丑数 就是只包含质因数 2、3 和 5 的正整数。
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

示例 1：
输入：n = 6
输出：true
解释：6 = 2 × 3

示例 2：
输入：n = 1
输出：true
解释：1 没有质因数，因此它的全部质因数是 {2, 3, 5} 的空集。习惯上将其视作第一个丑数。

示例 3：
输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。


想法：
for循环
因数为  2
因数为  3
因数为  5
最后的因数不能为  质数
先定义质数的方法
"""
import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def isUgly1(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 0:
        print("Prime1")
        return False
    if n == 1:
        print("Prime2")
        return True
    while(n != 1):
        if n % 2 == 0:
            n = n//2
            print("Prime3")
            continue
        elif n % 3 == 0:
            n = n//3
            print("Prime4")
            print(n)
            continue
        elif n % 5 == 0:
            n = n//5
            print("Prime5")
            continue
        else:
            print("Prime6")
            return False
    return True

def isUgly(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    if n == 1:
        return True
    while(n != 1):
        if n % 2 == 0:
            n = n//2
            continue
        elif n % 3 == 0:
            n = n//3
            continue
        elif n % 5 == 0:
            n = n//5
            continue
        elif isPrime(n):
            return False
    return True
n = 14
print(isUgly1(n))