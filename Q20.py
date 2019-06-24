#coding:utf-8

def func(ss):
    tmp_num = 0
    isPositive = 1

    if ss[0] == "+":
        pass
    elif ss[0] == "-":
        isPositive = -1

    total_str = ss[1:]

    level = 1
    for index in range(len(total_str) - 1, -1, -1):
        tmp_num += int(total_str[index]) * level
        level *= 10

    return tmp_num * isPositive

s = "-345"
print(func(s))






