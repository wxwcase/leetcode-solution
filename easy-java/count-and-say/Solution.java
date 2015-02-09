import java.util.*;

public class Untitled {
    public static void main(String[] args) {
        test();
    }
    
    public static void test() {
        Solution sol = new Solution();
        int a1 = 1;
        int a2 = 3;
        int a3 = 5;
        int a4 = 6;
        int a5 = 21;
        System.out.println(sol.countAndSay(a1));
        System.out.println(sol.countAndSay(a2));
        System.out.println(sol.countAndSay(a3));
        System.out.println(sol.countAndSay(a4));                        
        System.out.println(sol.countAndSay(a5));
    }
}

class Solution {
    /**
     * The count-and-say sequence is the sequence of integers beginning as follows:
     *  1, 11, 21, 1211, 111221, ...
     *  1 is read off as "one 1" or 11.     
     *  11 is read off as "two 1s" or 21.
     *  21 is read off as "one 2, then one 1" or 1211.
     * Given an integer n, generate the nth sequence
     */
    public String countAndSay(int n) {
        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                list.add("1");
            } else {
                list.add(next(list.get(i - 1)));
            }
        }
        return list.get(n - 1);
    }
    private String next(String s) {
        String result = "";
        int count = 1;
        char last = s.charAt(0);
        if (s.length() == 1) {
            return "" + count + last;
        }
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == last) {
                count++;
            } else {
                result = result + count + last;
                last = s.charAt(i);
                count = 1;
            }
        }
        return result + count + last;
    }
}