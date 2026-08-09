# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        h = {None: 0}                       # 字典：节点 → 高度；空节点高度 0
        stack = [(root, False)]             # (节点, 它的孩子处理完了吗)
        while stack:
            node, processed = stack.pop()   # 弹出栈顶
            if processed:                   # 孩子都算完了 → 现在轮到我（后序！）
                lh, rh = h[node.left], h[node.right]
                if abs(lh - rh) > 1:
                    return False
                h[node] = 1 + max(lh, rh)
            else:                           # 第一次见到我 → 先安排孩子
                stack.append((node, True))          # 我自己排在【后面】
                if node.left:  stack.append((node.left, False))
                if node.right: stack.append((node.right, False))
        return True