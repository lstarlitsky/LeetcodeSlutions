保存上一个数字即可。
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num,i=-10001,0
        for n in nums:
            if n!=num:
                num=n
                nums[i]=num
                i+=1
        nums=nums[:i]
        return len(nums)
```