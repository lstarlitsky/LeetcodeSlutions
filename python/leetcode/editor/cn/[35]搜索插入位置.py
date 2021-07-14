# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 963 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def binary_search(self, arr: List[int], target: int, l: int, r: int) -> int:
        if r >= l:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                return self.binary_search(arr, target, mid + 1, r)
            else:
                return self.binary_search(arr, target, l, mid - 1)
        else:
            return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 特殊情况
        if not nums or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # 二分查找
        ret = self.binary_search(arr=nums, target=target, l=0, r=len(nums))
        return ret


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().searchInsert(nums=[1, 3, 5, 6, 7, 9, 10, 15, 20, 21, 23, 25], target=11))
