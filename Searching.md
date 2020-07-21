## 107.Binary Tree Level Order Traversal II
- Breath First Search.
    
    Start from the root, search its every leave and mark them as the `next level list`, then assign the `current level` with `next level list`, repeat the process until there is no more node in `current level list`.
    
    At the same time, record the value of `current list` node into a list.
    

## 79. Word Search (DFS)
- Q: Why I uesd list.copy, then change the new list, the old_list is changed as well?

- One way to avoid that problem is to use another variable `tmp` to store the former value, after deep searching for this location, restore the value.

```tmp = board[i][j]
                    board[i][j] = '$'
                    if dfs(i-1, j, index+1) or dfs(i+1, j, index+1) or dfs(i, j-1, index+1) or dfs(i, j+1, index+1):         
                        return True
                    board[i][j] = tmp```
