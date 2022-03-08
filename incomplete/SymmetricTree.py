'''
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def set_node(self, left, right):
        self.left = left
        self.right = right
        return self

    def __str__(self):
        return str(self.val)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root.left, root.right)

    def traverse(self, subNode1, subNode2):
        if not subNode1 and not subNode2:
            return True
        elif (subNode1 and not subNode2) or (not subNode1 and subNode2) or (subNode1.val != subNode2.val):
            return False
        # if not self.traverse(subNode1.left, subNode2.right): return False
        left = self.traverse(subNode1.left, subNode2.right)
        right = self.traverse(subNode1.right, subNode2.right)
        return left and right

# def craeteNode(val,left,right):
#     return Node()
# [2,3,3,4,5,null,4]

#             2
#     3               3
# 4       5       null    4
def createTree():
    arr = [1, 2, 2, 3, 4, 4, 3]
    # return TreeNode(2).set_node(TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    return TreeNode(arr[0]).set_node(TreeNode(arr[1], TreeNode(arr[3]), TreeNode(arr[4])),
                                     TreeNode(arr[2], TreeNode(arr[5]), TreeNode(arr[6])))
    # TreeNode(val=arr[0]).set_node(left=TreeNode(arr[1]).set_node(),right=TreeNode(arr[2]))
    # return node


print(Solution().isSymmetric(root=createTree()))
