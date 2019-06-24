#coding:utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 从上往下分层打印二叉树
class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []

        res = []
        cur_stack = [root]

        while cur_stack:
            nxt_stack = []
            for i in cur_stack:
                if i.left:
                    nxt_stack.append(i.left)
                if i.right:
                    nxt_stack.append(i.right)
                res.append(i.val)
            cur_stack = nxt_stack

        return res

    def dfs(self, root):
        res = []
        if root is None:
            return res
        q = []
        q.append(root)
        while len(q) > 0:
            r = q.pop()
            if r.left is not None:
                q.append(r.left)
            if r.right is not None:
                q.append(r.right)
            res.append(r.value)

        return res

    def bfs(self, root):
        res = []
        if root is None:
            return res
        q = []
        q.append(root)
        while len(q) > 0:
            r = q.pop()
            res.append(r.value)
            if r.left is not None:
                q.append(r.left)
            if r.right is not None:
                q.append(r.right)

        return res


















