### 解题思路
a指针先走n步，然后一起走，当a走到终点则b的下一个节点就是要删的节点
注意如果要删的是第一个节点，那么a会指向null，此时直接返回head.next即可

### 代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //双指针
        ListNode a = head;
        ListNode b = head;
        while(a != null || b != null){
            while(n > 0 && a != null){
                a = a.next;
                n--;
            }
            if(a != null){
                if(a.next == null){
                    b.next = b.next.next;
                    break;
                }
                a = a.next;
                b = b.next;
            }else{
                return head.next;
            }
        }
        return head;
    }
}
```