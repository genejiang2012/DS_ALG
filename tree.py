'''
Author: Gene Jiang
Date: 2018-02-01 18:11:10
LastEditors: Gene Jiang
LastEditTime: 2021-02-01 19:27:38
Description: 
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