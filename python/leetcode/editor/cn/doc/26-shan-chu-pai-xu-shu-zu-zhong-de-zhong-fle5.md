# [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
***
### 思路
首先注意数组是有序的
1. 令索引 i 为慢指针，索引 j 为快指针，快指针正常遍历数组，一次走一步
2. 如果快指针和慢指针所指的元素不相同，证明慢指针所指元素的重复已结束，索引 i + 1，并把新的元素赋给索引 i 处
3. 也就是说，慢指针记录的是非重复元素的索引，最后返回非重复元素个数为 i + 1
### 代码
```Java []
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for(int j = 0; j < nums.length; j++){
            if(nums[j] != nums[i]){
                nums[++i] = nums[j];
            }
        }
        return i + 1;
    }
}
```
```Python3 []
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
```
**复杂度分析**
- 时间复杂度：*O(n)*
- 空间复杂度：*O(1)*
