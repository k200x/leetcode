#coding:utf-8

import copy

class MaxHeap(object):
    def __init__(self, arr):
        self.data = copy.copy(arr)
        self.count = len(self.data)
        i = self.count / 2
        while i >= 1:
            self.shiftDown(i)
            i -= 1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        # 插入元素入堆
        self.data.append(item)
        self.count += 1
        self.shiftup(self.count)

    def shiftup(self, count):
        # 将插入的元素放到合适位置，保持最大堆
        while count > 1 and self.data[(count / 2) - 1] < self.data[count - 1]:
            self.data[(count / 2) - 1], self.data[count - 1] = self.data[count - 1], self.data[(count / 2) - 1]
            count /= 2

    def extractMax(self):
        # 出堆
        if self.count > 0:
            ret = self.data[0]
            self.data[0], self.data[self.count - 1] = self.data[self.count - 1], self.data[0]
            self.data.pop()
            self.count -= 1
            self.shiftDown(1)
            return ret

    def shiftDown(self, count):
        # 将堆的索引位置元素向下移动到合适位置，保持最大堆
        while 2 * count <= self.count:
            # 证明有孩子
            j = 2 * count
            if j + 1 <= self.count:
                # 证明有右孩子
                if self.data[j] > self.data[j - 1]:
                    j += 1
            if self.data[count - 1] >= self.data[j - 1]:
                # 堆的索引位置已经大于两个孩子节点，不需要交换了
                break
            self.data[count - 1], self.data[j - 1] = self.data[j - 1], self.data[count - 1]
            count = j

class MinHeap(object):
    def __init__(self):
        self.data = []
        self.count = len(self.data)

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        # 插入元素入堆
        self.data.append(item)
        self.count += 1
        self.shiftup(self.count)

    def shiftup(self, count):
        # 将插入的元素放到合适位置，保持最小堆
        while count > 1 and self.data[(count / 2) - 1] > self.data[count - 1]:
            self.data[(count / 2) - 1], self.data[count - 1] = self.data[count - 1], self.data[(count / 2) - 1]
            count /= 2

    def extractMin(self):
        # 出堆
        if self.count > 0:
            ret = self.data[0]
            self.data[0], self.data[self.count - 1] = self.data[self.count - 1], self.data[0]
            self.data.pop()
            self.count -= 1
            self.shiftDown(1)
            return ret

    def shiftDown(self, count):
        # 将堆的索引位置元素向下移动到合适位置，保持最小堆
        while 2 * count <= self.count:
            # 证明有孩子
            j = 2 * count
            if j + 1 <= self.count:
                # 证明有右孩子
                if self.data[j] < self.data[j - 1]:
                    j += 1
            if self.data[count - 1] <= self.data[j - 1]:
                # 堆的索引位置已经小于两个孩子节点，不需要交换了
                break
            self.data[count - 1], self.data[j - 1] = self.data[j - 1], self.data[count - 1]
            count = j

# 1.设计一个魔方(六面)的程序。
# 2.有一千万条短信，有重复，以文本文件的形式保存，一行一条，有重复。
# 请用 5 分钟时间，找出重复出现最多的前 10 条。
# 3.收藏了 1 万条 url，现在给你一条 url，如何找出相似的 url。(面试官不解释何为相似)





