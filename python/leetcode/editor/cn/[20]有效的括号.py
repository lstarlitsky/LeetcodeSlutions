# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "([)]"
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "{[]}"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由括号 '()[]{}' 组成 
#  
#  Related Topics 栈 字符串 
#  👍 2489 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                # 这里要考虑下右括号比左括号多的情况
                if len(stack) and stack[-1] == left[right.index(char)]:
                    stack.pop(-1)
                else:
                    return False
        # 左括号未被完全闭合
        if len(stack) > 0:
            return False
        return True
                
# leetcode submit region end(Prohibit modification and deletion)
