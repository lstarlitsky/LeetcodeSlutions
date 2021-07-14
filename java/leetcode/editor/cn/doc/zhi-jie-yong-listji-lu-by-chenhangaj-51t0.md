### 解题思路
暴力遍历每个数位上的数字

### 代码

```java
class Solution {
    public int reverse(int x) {
        long res = 0;
        int a = Math.abs(x);
        while(a > 0){
            int mod = a % 10;
            a /= 10;
            res = res*10+mod;
        }
        res = x < 0 ? -res : res;
        return res > Integer.MAX_VALUE || res < Integer.MIN_VALUE ? 0 : (int)res;
    }
}
```