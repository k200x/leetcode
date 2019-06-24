#coding:utf-8

def inorderTraversal(root):
    stack = []
    sol = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:













