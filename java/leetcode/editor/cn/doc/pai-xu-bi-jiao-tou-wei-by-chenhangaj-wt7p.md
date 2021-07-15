### 解题思路
此处撰写解题思路

### 代码

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        if(strs.length == 1) return strs[0];
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length-1];
        int i = 0;
        int n = Math.min(s1.length(),s2.length());
        for(;i < n;i++){
            if(s1.charAt(i) != s2.charAt(i)){
                break;
            }
        }
        if(i == 0) return "";
        return s1.substring(0,i);
    }
}
```