#coding:utf-8

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

n0 = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
n0.left = n1
n0.right = n2


# 1.求二叉树的最大深度
def maxDepth(node):
    if not node:
        return 0
    left = maxDepth(node.left)
    right = maxDepth(node.right)
    return max(left, right) + 1

# 2.求二叉树的最小深度
def getMin(root):
    if not root:
        return 999
    if not root.left and not root.right:
        return 1
    return min(getMin(root.left), getMin(root.right)) + 1

def getMinDepth(root):
    if not root:
        return 0
    return getMin(root)

# 3.求二叉树中节点的个数
def numOfTreeNode(root):
    if not root:
        return 0
    left = numOfTreeNode(root.left)
    right = numOfTreeNode(root.right)
    return left + right + 1

# 4.求二叉树中叶子节点的个数
def numsOfNochildNode(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return numsOfNochildNode(root.left) + numsOfNochildNode(root.right)

# 5.求二叉树中第K层节点的个数
def numsOfkLevelTreeNode(root, k):
    if (not root) or k < 1:
        return 0
    if k == 1:
        return 1
    numsLeft = numsOfkLevelTreeNode(root.left, k-1)
    numsRight = numsOfkLevelTreeNode(root.right, k-1)
    return numsLeft + numsRight

# 6.判断二叉树是否是平衡二叉树



# 8.判断两个二叉树是否完全相同
def isSameTreeNode(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    left = isSameTreeNode(t1.left, t2.left)
    right = isSameTreeNode(t1.right, t2.right)
    return left and right

# 9.两个二叉树是否互为镜像
def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

# 10.翻转二叉树or镜像二叉树
def mirrorTreeNode(root):
    if not root:
        return None
    left = mirrorTreeNode(root.left)
    right = mirrorTreeNode(root.right)
    root.left = right
    root.right = left
    return root

# 12.二叉树的前序遍历
def preOrder2(root, result):
    if not root:
        return None
    result.append(root.val)
    preOrder2(root.left, result)
    preOrder2(root.right, result)

def preOrderReverse(root):
    result = []
    preOrder2(root, result)
    return result

# 13.二叉树的中序遍历
def inOrder2(root, result):
    if not root:
        return None
    result.append(root.val)
    preOrder2(root.left, result)
    preOrder2(root.right, result)

def inOrder(root):
    result = []
    inOrder2(root, result)
    return result

# 14.二叉树的后序遍历
def postOrder2(root, result):
    if not root:
        return None
    postOrder2(root.left, result)
    postOrder2(root.right, result)
    result.append(root.val)

def postOrder(root)
    result = []
    postOrder2(root, result)
    return result























