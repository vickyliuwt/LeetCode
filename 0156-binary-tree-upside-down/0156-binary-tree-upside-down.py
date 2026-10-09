class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
		# start from root
        cur, pre, preRight = root, None, None
        while cur:
			# temporarily store 'cur.left' and 'cur.right' ('cur.left' will be next 'cur')
            temp1, temp2 = cur.left, cur.right
			# modify parent-child links
            cur.left, cur.right = preRight, pre
			# go to next iteration
            cur, pre, preRight = temp1, cur, temp2
        return pre