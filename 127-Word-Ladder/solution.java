public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordList) {
        if(wordList.size() <= 0) return 0;
        LinkedList<Node> queue = new LinkedList<Node>();
        queue.push(new Node(beginWord,1));
        while(!queue.isEmpty()){
            Node top = queue.pop();
            if(top.word.equals(endWord)) return top.len;
            
            for(int i=0; i<top.word.length();i++){
                char[] charArray = top.word.toCharArray();
                for(char c ='a'; c<='z';c++){
                    charArray[i] = c;
                    String newWord = new String(charArray);
                    if(wordList.contains(newWord)){
                        queue.push(new Node(newWord,top.word.len+1));
                        newWord.remove(newWord);
                    }
                }
            }
        }
        return 0;
    }
    
    static class Node{
        String word;
        int len;
        public Node(String t_word, int t_len){
            word = t_word;
            len = t_len;
        }
    }
}