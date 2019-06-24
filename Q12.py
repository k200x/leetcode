#coding:utf-8

# class Jingtai(object):
#     Count = 0
#
# Ja1 = Jingtai()
# Ja2 = Jingtai()
# Ja2.Count = 1
# print(Ja2.Count, Ja1.Count)

# class Foo(object):
#     count = 0
#
# f1 = Foo()
# f2 = Foo()
# Foo.count = 1
# print(f1.count, f2.count)

class Foo(object):
    _count = 0

    @property
    def count(self):
        return Foo._count

    @count.setter
    def count(self, num):
        Foo._count = num

f1 = Foo()
f2 = Foo()
print(f1.count, f1._count, f2.count, f2._count)

f1.count = 1
print(f1.count, f1._count, f2.count, f2._count)

















