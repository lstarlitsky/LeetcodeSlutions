# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
#  Related Topics 链表 双指针 
#  👍 1453 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 利用快慢指针，快指针便利整条链表，慢指针保持在 (快指针 - n - 1) 的位置
        # 先建立头节点
        tmpNode = ListNode(0)
        tmpNode.next = head
        # 快慢指针
        slow = tmpNode
        fast = tmpNode
        fast_index = -1
        while fast.next:
            fast_index += 1
            if fast_index >= n:
                # print(fast_index)
                slow = slow.next
                # print(f"slow={slow.val}")
            fast = fast.next
        slow.next = slow.next.next
        return tmpNode.next
# leetcode submit region end(Prohibit modification and deletion)
