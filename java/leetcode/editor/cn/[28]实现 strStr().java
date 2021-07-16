//实现 strStr() 函数。 
//
// 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
//果不存在，则返回 -1 。 
//
// 
//
// 说明： 
//
// 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
//
// 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。 
//
// 
//
// 示例 1： 
//
// 
//输入：haystack = "hello", needle = "ll"
//输出：2
// 
//
// 示例 2： 
//
// 
//输入：haystack = "aaaaa", needle = "bba"
//输出：-1
// 
//
// 示例 3： 
//
// 
//输入：haystack = "", needle = ""
//输出：0
// 
//
// 
//
// 提示： 
//
// 
// 0 <= haystack.length, needle.length <= 5 * 104 
// haystack 和 needle 仅由小写英文字符组成 
// 
// Related Topics 双指针 字符串 字符串匹配 
// 👍 960 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int strStr(String haystack, String needle) {
        // 使用java中的indexof，380ms
        // return haystack.indexOf(needle);
        // BF 朴素匹配求解，348ms
        // return myFunc(haystack, needle);
        // kmp 算法求解，
        return kmp(haystack, needle);
    }

    private int myFunc(String haystack, String needle) {
        if (needle.equals("")) {
            return 0;
        }
        if (haystack.equals("")) {
            return -1;
        }
        int subStringLength = needle.length();
        for (int i = 0; i <= haystack.length() - subStringLength; i++) {
            if (haystack.charAt(i) == needle.charAt(0) && haystack.substring(i, i + subStringLength).equals(needle)) {
                return i;
            }
        }
        return -1;
    }

    /**
     * KMP算法实现
     *
     * @param haystack
     * @param needle
     * @return
     */
    private int kmp(String haystack, String needle) {
        if (needle.equals("")) {
            return 0;
        }
        if (haystack.equals("")) {
            return -1;
        }
        int[] next = kmpNextArray(needle);
        int i = 0;
        int j = 0;
        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            } else if (j == 0) {
                i++;
            } else {
                j = next[j];
            }
            if (j == needle.length() - 1) {
                return i - j;
            }
        }
        return -1;
    }


    /**
     * KMP算法中的模式串next数组求解
     *
     * @param needle
     * @return
     */
    private int[] kmpNextArray(String needle) {
        int[] next = new int[needle.length()];
        for (int i = 0; i < needle.length(); i++) {
            next[i] = kmpGetNextK(needle, i);
        }
        return next;
    }

    /**
     * 求解模式串p在索引j位置的next K 值
     *
     * @param p
     * @param j
     * @return
     */
    private int kmpGetNextK(String p, int j) {
        if (j == 0) {
            return -1;
        }
        if (j > 0) {
            int k = kmpGetNextK(p, j - 1);
            while (k >= 0) {
                if (p.charAt(j) == p.charAt(k)) {
                    return k + 1;
                } else {
                    k = kmpGetNextK(p, k);
                }
            }
        }
        return 0;

    }
}


//leetcode submit region end(Prohibit modification and deletion)
