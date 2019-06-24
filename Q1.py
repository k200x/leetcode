#coding:utf-8

# class BSTreeNode(object):
#     def __init__(self, value, leftNode=None, rightNode=None):
#         self.m_nValue = value
#         self.m_pLeft = leftNode
#         self.m_pRight = rightNode
#
#     def __cmp__(self, other):
#         if self.m_nValue == other.m_nValue:
#             return 0
#         elif self.m_nValue < other.m_nValue:
#             return -1
#         else:
#             return 1
#
#     def __lt__(self, other):
#         if self.m_nValue < other.m_nValue:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self.m_nValue > other.m_nValue:
#             return True
#         else:
#             return False
#
#     def __eq__(self, other):
#         if self.m_nValue == other.m_nValue:
#             return True
#         else:
#             return False
#
#     def __le__(self, other):
#         if self.m_nValue <= other.m_nValue:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         if self.m_nValue >= other.m_nValue:
#             return True
#         else:
#             return False


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def inOrderBSTree(self, root):
        if root == None:
            return

        self.inOrderBSTree(root.lchild)

        root.lchild = self.pEnd
        if None == self.pEnd:
            self.pHead = root
        else:
            self.pEnd.rchild = root
        self.pEnd = root

        self.inOrderBSTree(root.rchild)









