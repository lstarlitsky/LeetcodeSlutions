# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−2^31, 2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2^31 <= x <= 2^31 - 1 
#  
#  Related Topics 数学 
#  👍 2590 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fun_1(self, x: int) -> int:
        if x < 0:
            x = list(str(abs(x)))
            x.reverse()
            y = int("".join(x)) * -1
        else:
            x = list(str(x))
            x.reverse()
            y = int("".join(x))
        if -2147483648 <= y <= 2147483646:
            return y
        else:
            return 0

    def fun_2(self, x: int) -> int:
        """
        # 输入：x = 123
        # 输出：321
        # 输入：x = -123
        # 输出：-321
        Args:
            x:

        Returns:

        """
        y = 0
        while 1:
            if x >= 0:
                item = x % 10
                y = y * 10 + item
                x = x // 10
            else:
                item = x % -10
                y = y * 10 + item
                x = -(x // -10)
            if not x:
                break
        if -2147483648 <= y <= 2147483646:
            return y
        else:
            return 0

    def reverse(self, x: int) -> int:
        return self.fun_1(x=x)

# leetcode submit region end(Prohibit modification and deletion)
