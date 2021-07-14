### 解题思路
对每个字符判断其与右侧字符的大小，大的加，小的减

### 代码

```python3
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roma_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(s) == 1:
            return  roma_map[s]

        for i in range(len(s)-1):
            if roma_map[s[i]] >= roma_map[s[i+1]]:
                res += roma_map[s[i]]
            else:
                res -= roma_map[s[i]]
        return res + roma_map[s[-1]]
```