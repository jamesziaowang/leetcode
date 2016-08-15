public class Solution {
    public static int ladderLength(String beginWord, String endWord, Set<String> wordList) {
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        wordList.remove(beginWord);
        int length = 1;
        while(!queue.isEmpty()){
            int count = queue.size();
            for(int k=0;i<count;k++){
                String word = queue.poll();
                if(word.equals(endWord)) return length;
                char[] chars = word.toCharArray();
                for(int i=0;i<chars.length;i++){
                    for(char j='a';j<='z';j++){
                        if(chars[i]==j) continue;
                        chars[i]=j;
                        String newWord = new String(chars);
                        if(wordList.contains(newWord)){
                            queue.add(newWord);
                            wordList.remove(newWord);
                        }
                    }
                }
            }
            length++;
        }
        return 0;
    }
    public static void main(String[] args){
        Set<String> wordList = new HashSet<String>();
        wordList.add("a");
        wordList.add("b");
        wordList.add("c");
        int ret = ladderLength("a","c",wordList);
        System.out.println(ret);
    }
}