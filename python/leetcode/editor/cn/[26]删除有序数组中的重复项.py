# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。 
# 
#  不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。 
# 
#  
# 
#  说明: 
# 
#  为什么返回数值是整数，但输出的答案是数组呢? 
# 
#  请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。 
# 
#  你可以想象内部操作如下: 
# 
#  
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3 * 104 
#  -104 <= nums[i] <= 104 
#  nums 已按升序排列 
#  
# 
#  
#  Related Topics 数组 双指针 
#  👍 2104 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fun_1(self, nums: List[int]) -> int:
        # 首先，nums 已按升序排列，所以使用双指针中的快慢指针；
        # 快指针每次移动一位，慢指针只有在快慢指针对应数不相同时才移动；
        slow = 0
        fast = 1
        while 1:
            if fast > len(nums) - 1:
                break
            if nums[slow] == nums[fast]:
                del nums[fast]  # 这里删除之后，fast索引位对应的数将是下一位了
            else:
                slow += 1
                fast += 1
        return len(nums)

    def fun_2(self, nums: List[int]) -> int:
        # 这个也没有原地修改数组
        num, i = -10001, 0
        for n in nums:
            if n != num:
                num = n
                nums[i] = num
                i += 1
        nums = nums[:i]
        return len(nums)

    def fun_3(self, nums: List[int]) -> int:
        # 这个方法只是将去重后的数写到了原列表的前部，尾部是存在多余数的？
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        return self.fun_1(nums)

# leetcode submit region end(Prohibit modification and deletion)
