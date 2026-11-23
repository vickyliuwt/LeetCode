# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root):
        self.res = 0
        self.findLongestConsectiveHelper(root,0, 0)
        return self.res
    
    def findLongestConsectiveHelper(self, root,count, target):
        if not root:
            return
        elif root.val == target:
            count += 1
        
        else:
            count = 1
            
        self.res = max(self.res, count)
        
        self.findLongestConsectiveHelper(root.left, count, root.val+1)
        self.findLongestConsectiveHelper(root.right, count, root.val+1)
        