public class Solution {
    public int strStr(String haystack, String needle) {
        if(haystack =="" || needle=="" )return 0;
        for(int i =0;;i++){
            for(int j = 0;;j++){
                if(needle.length()==j) return i;
                if(haystack.length()==i+j) return -1;
                if(needle.charAt(j)!=haystack.charAt(i+j)) break;
            }
        }
        return -1;
    }
}