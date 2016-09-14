public class Solution {
    public String simplifyPath(String path) {
        Stack<String> s = new Stack<String>();
        String[] words = path.splite("/");
        for(words : String str){
            if(str.length==0 ||str.equals(".")) continue;
            if(str.equals("..")){
                if(!s.isEmpty()) s.pop(); 
            }else{
                str.push(str);
            }
        }
        String ret = s.isEmpty()?"/":"";
        for(s:String t) ret += "/"+t;
        return ret;
    }
}