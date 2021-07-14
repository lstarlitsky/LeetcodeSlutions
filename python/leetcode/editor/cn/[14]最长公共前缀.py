# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 1675 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(x) for x in strs])
        ret = ''
        for i in range(min_len):
            if all([x.startswith(strs[0][:i+1]) for x in strs]):
                ret = strs[0][:i+1]
            else:
                break
        return ret
# leetcode submit region end(Prohibit modification and deletion)
