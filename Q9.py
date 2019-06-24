#coding:utf-8

class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

n0 = Node(8)
n1 = Node(6)
n2 = Node(10)

n3 = Node(5)
n4 = Node(7)
n5 = Node(9)
n6 = Node(11)

n0.left = n1
n0.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6

cmp_ll = [5, 7, 6, 9, 11, 10, 8]
ll = []


def process(root):
    if not root:
        return
    process(root.left)
    process(root.right)
    ll.append(root.val)

process(n0)

print(ll == cmp_ll)




