'''
print("hello")

a = [1,3]
print(a[1])

aa = (1,2,[2,3,4])
print(aa[2])
'''
#推导式
#列表推导式
'''
aa = ['aa','bb','ccc']
b = [a.upper() for a in aa if len(a) <3]
print(b)
'''
#字典推导式
# bb = {"aa":12,"bb":33,"ccc":44}
# a = [bb.get(b) for b in bb.keys() if len(b)<3]
# print(a)
#集合推导式
# c = {i for i in range(30) if i%3 == 0}
# print(c)
#元组推导式
from traceback import print_exc


a = (x for x in range(1,10))
print(a)
print(tuple(a))


# 海象运算符 :=  可以在表达式内部给变量赋值
if (n := len("sdfs"))>3 :
        print(n)
        
# 数字类型可以分为整型，浮点型， 复数(complex) a+bj/complex(a,b)
x = 2+3j
print(x)


