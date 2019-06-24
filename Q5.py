#coding:utf-8

ll = [3,4,5,6,7,2,1,10]

def process(arr, length):
    tmp_arr = sorted(arr)
    return tmp_arr[0: length]

print(process(ll, 4))


