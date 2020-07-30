## 106. Construct Binary Tree from Inorder and Postorder Traversal
- Given inorder and postorder traversal of a tree, construct the binary tree.
- Inorder: Left node -> Root -> Right node
- Postorder: Left node -> Right node -> Root

The logic of this program:
1. Build a dict to store the index of each element in inorder list
2. Set four variables as pointers to these two lists, `in_begin`, `in_end`, `pos_begin`, `pos_end`.
3. The end of the postorder list is the root, find its index in inorder list. The left elements in inorder list belong to left side and the same to the right side.
4. So we need to change the value of these four variables.
    
    Left: `in_begin` equals to 0 at first, `in_end` = index, `pos_begin` = 0 at first, `pos_end`= `pos_begin+index-in_begin` (the length of the left side is index-in_begin)
    
    Right: `in_begin` = index+1, `in_end` = l at first,  `pos_begin` = `pos_begin+index-in_begin` (the length of the left side is index-in_begin), `pos_end` = pos_end -1 (the last element is the root)

```
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
```
