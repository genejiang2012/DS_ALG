'''
Author: gene.jiang
Date: 2024-10-21 20:00:48
LastEditors: gene.jiang
LastEditTime: 2024-10-21 20:02:24
Description: file content
FilePath: \DS_ALG\tree.py
'''

from typing import *

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traverse(self, root: TreeNode) -> List[int]:
        def preoder(root: TreeNode):
            if not root: 
                return 

            res.append(root.val)
            preoder(root.left)
            preoder(root.right)
        
        res = []
        preoder(root)
        return res

root = [1, None, 2, 3]
print(Solution().preorder_traverse(root))