#coding:utf-8

def mirrorTreeNode(root):
    if not root:
        return None
    left = mirrorTreeNode(root.left)
    right = mirrorTreeNode(root.right)
    root.left = right
    root.right = left
    return root



































