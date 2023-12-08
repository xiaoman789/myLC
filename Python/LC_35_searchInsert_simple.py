def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while(left <= right):
        middle = (left + right)//2
        if(target<nums[middle]):
            right = middle - 1
        elif(target>nums[middle]):
            left = middle + 1
        else:
            return middle
    return -1
def searchInsert(nums, target):
    i = binarySearch(nums,target)
    if(i>-1):
        return i
    else:
        return len(nums)

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))