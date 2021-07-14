# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。 
# 
#  回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 121
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
#  
# 
#  示例 4： 
# 
#  
# 输入：x = -101
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= x <= 231 - 1 
#  
# 
#  
# 
#  进阶：你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学 
#  👍 1540 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fun_1(self, x: int):
        if x < 0:
            return False
        else:
            base = 10
            xx = []
            while x // base > 0:
                xx.append(x % base)
                x //= base
            xx.append(x)
            for i in range(len(xx) // 2):
                if xx[i] != xx[-(i + 1)]:
                    return False
            else:
                return True

    def fun_2(self, x: int):
        if x < 0:
            return False
        else:
            xx = x
            base = 10
            y = 0
            while x // base > 0:
                y = y * 10 + x % base
                x //= base
            y = y * 10 + x % base
            # print(y)
            if y == xx:
                return True
            return False

    def fun_3(self, x: int):
        x_list = list(str(x))
        if x_list == x_list[::-1]:
            return True
        return False

    def isPalindrome(self, x: int) -> bool:
        return self.fun_3(x)

# leetcode submit region end(Prohibit modification and deletion)
