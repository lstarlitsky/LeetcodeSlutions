### 解题思路


### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #建立建立dummy节点
        dummy = ListNode(0)
        dummy.next = head
        #建立双指针
        pre = dummy
        cur = dummy
        #cur指针先走先走n+1步
        for i in range(n+1):
            cur = cur.next
        #两个指针一起动,until cur == None
        while cur != None:
            cur = cur.next
            pre = pre.next
        #赋值
        pre.next = pre.next.next

        return dummy.next
```