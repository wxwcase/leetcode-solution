import java.util.*;

public class Solution {
    public static void main(String[] args) {
        test();
    }
    
    public static void test() {
        Solution sol = new Solution();
        String s1 = "({}[]())";
        String s2 = "(){}[][)";
        String s3 = "]";
        String s4 = "]]";
        System.out.println(sol.isValid(s1));
        System.out.println(sol.isValid(s2));        
        System.out.println(sol.isValid(s3));
        System.out.println(sol.isValid(s4));
    }
}

class ValidParentheses {
    /**
     * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
     * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
     */
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) {
            return false;
        }
        String left = "({[";
        String right = ")}]";
        LinkedList<Character> stack = new LinkedList<>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (left.indexOf(c) != -1) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    char r = stack.pop();
                    if (right.indexOf(c) != left.indexOf(r)) {
                        return false;
                    }
                }
            }
        }
        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}