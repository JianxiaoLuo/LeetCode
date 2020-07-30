# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        l = len(inorder)
        
        # index start from 0
        dic = {elem: it for it, elem in enumerate(inorder)} 
        
        def helper(in_begin, in_end, pos_begin, pos_end):
            if pos_end - pos_begin <= 0: return None
            
            index = dic[postorder[pos_end-1]]
            
            node = TreeNode(postorder[pos_end-1])
            node.left = helper(in_begin, index, pos_begin, pos_begin+index-in_begin)
            node.right = helper(index+1, in_end, pos_begin+index-in_begin, pos_end-1)
            
            return node
            
        return helper(0, l, 0, l)
