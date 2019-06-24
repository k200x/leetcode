#coding:utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        pre = post = head

        # 快指针先走k步
        for i in range(k):
            # 如果k大于链表长度，返回空
            if pre == None:
                return None
            pre = pre.next

        # 快慢指针同时往前走
        while pre != None:
            pre = pre.next  # 快指针
            post = post.next  # 慢指针
        return post


















