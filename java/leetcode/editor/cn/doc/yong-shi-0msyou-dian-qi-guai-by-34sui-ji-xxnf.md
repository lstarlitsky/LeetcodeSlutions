### 解题思路
此处撰写解题思路
![image.png](https://pic.leetcode-cn.com/1626170633-GVIchn-image.png)

### 代码

```java
class Solution {
 public static String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length==0){
            return "";
        }
        String tmp = strs[0];
        for (int i = 0; i < strs.length; ++i) {
            tmp = getLongestCommonPrefixFromTwoStrings(tmp,strs[i]);
        }
        return tmp;
    }

    public static String getLongestCommonPrefixFromTwoStrings(String str1,String str2){
        if(str1==null||str2==null||str1==""||str2=="") return "";
        int min = Math.min(str1.length(), str2.length());
        int i;
        for (i = 0; i < min; i++) {
            if(str1.charAt(i) != str2.charAt(i)) {
                break;
            }
        }

        return str1.substring(0,i);
    }
}
```