#coding:utf-8

# 设计包含min函数的栈
class Stack:
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop(-1)

    def peek(self):
        return self.l[-1]

    def min(self):
        return min(self.l)

s = Stack()
s.push(10)
s.push(2)
s.push(5)
print(s.min())
