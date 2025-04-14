package LeetCode.stack;

import java.util.Stack;

public class ValidParentheses {

    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i)=='(' || s.charAt(i)=='{' || s.charAt(i)=='[') {
                stk.push(s.charAt(i));
            }
            else {
                if (stk.isEmpty()) {
                    return false;
                }
                char c = stk.pop();
                if (c == '(' && s.charAt(i)!=')')
                    return false;
                else if (c == '{' && s.charAt(i) != '}')
                    return false;
                else if (c == '[' && s.charAt(i) != ']')
                    return false;
            }


        }

        return stk.isEmpty();
    }
}
