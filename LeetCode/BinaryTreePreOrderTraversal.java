package LeetCode;

import java.util.*;



public class BinaryTreePreOrderTraversal {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

    }

    class Solution {
        public List<Integer> preorderTraversal(TreeNode root) {
            List<Integer> answer = new ArrayList<>();
            if (root == null) {
                return answer;
            }

            TreeNode node = root;
            answer = preOrder(answer, node);
            return answer;
        }

        public List<Integer> preOrder(List<Integer> list, TreeNode node) {
            list.add(node.val);
            if (node.left != null) {
                preOrder(list, node.left);
            }
            if (node.right != null) {
                preOrder(list, node.right);
            }
            return list;
        }
    }

}
