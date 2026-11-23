# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Deserialization 
class Codec:
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, output):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                output.append('None')
            else:
                output.append(str(root.val))
                rserialize(root.left, output)
                rserialize(root.right, output)
            return output
        
        return ','.join(rserialize(root, []))
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.popleft()
                return None
                
            root = TreeNode(int(l[0]))
            l.popleft()
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = deque(data.split(','))
        root = rdeserialize(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))