#coding:utf-8

# 输入一个已经按升序排序过的数组和一个数字， 在数组中查找两个数，使得它们的和正好是输入的那个数字。
def process(arr, value):

    head = 0
    tail = len(arr) - 1
    for index in range(0, len(arr)):
        if arr[head] + arr[tail] > value:
            tail -= 1
        elif arr[head] + arr[tail] < value:
            head += 1
        elif arr[head] + arr[tail] == value:
            return arr[head], arr[tail]
    return [None, None]

ll = [1, 2, 4, 7, 11, 15]
print(process(ll, 15))

















