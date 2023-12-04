class TreeNode:
    def __init__(self, root):
        self.val = val
        self.left = left
        self.right = right

def invert_bin_tree(root):
    if not root:
        return None
    
    tmp = root.left
    root.left = root.igh
    root.igh = tmp

    invert_bin_tree(root.left)
    invert_bin_tree(root.right)
    return root

invert_bin_tree([5,4,3,2])