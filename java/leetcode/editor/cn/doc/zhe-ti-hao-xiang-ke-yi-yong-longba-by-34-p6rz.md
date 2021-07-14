### 解题思路
执行用时 :8 ms, 在所有 Java 提交中击败了100%的用户

### 代码

```java
class Solution {
    public static boolean isPalindrome(int x) {
        int original = x;
        if (x<0) return false;
        long res = 0;
        while (x != 0){
            long digital = x % 10;
            x = x / 10;
            res = res * 10 + digital;
        }
        return res == original?true:false;
    }
}
```