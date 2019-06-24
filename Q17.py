#coding:utf-8

# 题目:在一个字符串中找到第一个只出现一次的字符。

ss = "abaccdeff"
d = {}

for s in ss:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

print(d)
min_pair = min(zip(d.values(), d.keys()))
print(min_pair[1])

















