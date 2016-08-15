public class Solution {
    public static int ladderLength(String beginWord, String endWord, Set<String> wordList) {
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        wordList.remove(beginWord);
        int length = 1;
        while(!queue.isEmpty()){
            int count = queue.size();
            for(int k=0;k<count;k++){
                String word = queue.poll();
                if(word.equals(endWord)) return length;
                for(int i=0;i<word.length();i++){
                    for(char c='a';c<='z';c++){
                        char[] chars = word.toCharArray();
                        if(chars[i]==c) continue;
                        chars[i]=c;
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
}