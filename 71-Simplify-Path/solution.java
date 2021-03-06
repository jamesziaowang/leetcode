public class Solution {
    public String simplifyPath(String path) {
        Stack<String> s = new Stack<String>();
        String[] words = path.split("/");
        for(String str : words){
            if(str.length()==0 ||str.equals(".")) continue;
            if(str.equals("..")){
                if(!s.isEmpty()) s.pop(); 
            }else{
                s.push(str);
            }
        }
        String ret = s.isEmpty()?"/":"";
        for(String t:s) ret += "/"+t;
        return ret;
    }
}