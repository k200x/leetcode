#coding:utf-8

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.target = []

    def MaxDistance(self, root):
        if not root:
            return 0







