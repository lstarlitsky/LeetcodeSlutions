```java
class Solution {
    //KMP
    public int strStr(String haystack, String needle) {
        if(needle.length()==0){
            return 0;
        }
        if(haystack.length()==0){
            return -1;
        }
        int[] arr = getTempArr(needle.toCharArray());
        int i=0;
        int j=0;
        while(i<haystack.length() && j<needle.length()){
            if(haystack.charAt(i)==needle.charAt(j)){
                i++;
                j++;
            }else{
                if(j!=0){
                    j=arr[j-1];
                }else{
                    i++;
                }
            }
        }
        if(j==needle.length()){
            return i-j;
        }
        return -1;
    }

    public int[] getTempArr(char[] pattern){
        int[] arr = new int[pattern.length];
        int index = 0;
        for(int i=1;i<pattern.length;){
            if(pattern[index]==pattern[i]){
                arr[i]=index+1;
                index++;
                i++;
            }else{
                if(index != 0){
                    index = arr[index-1];
                }else{
                    arr[i]=0;
                    i++;
                }
            }
        }
        return arr;
    }
}