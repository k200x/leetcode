#coding:utf-8

# 简易方法搞定约瑟夫环问题
a = [x for x in range(1, 31)]
del_number = 8  # 该删除的编号

for i in range(15):
    del a[del_number]
    del_number = (del_number + 8) % len(a)  # 关键





















