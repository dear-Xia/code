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

'''
    数字运算
    abs(x) 返回整数绝对值
    ceil(x) 返回上整数
    exp(x) 返回e的x次幂
    fabs(x) 返回数字的绝对值
    floor(x) 返回数字的下整数
    (x>y)-(x<y)  x<y->-1 x==y->0 x>y->1
    log(x) 10为底的log 
    log10(x)
    max(a,b,c)
    min(a,b,c)
    modf(x)返回x的整数部分和小数部分，浮点型表示出来
    pow(x,y) x的y次方
    round(s,[,n]) 返回浮点数x的四舍五入值，n表示小数点后几位
    sqrt(x) 平方根
    
    随机函数
    choice（seq） 从序列的元素中随机选择一个元素
    randrange([start],stop,[step])
    random()
    seed([x])
    shuffle(list) 将序列的所有元素随机排序
    uniform(x...y) 随机生成下一个实数
    
    三角函数
    acos(x) 反余弦
    asin(x) 反正弦
    atan(x) 反正切
    atan2(y,x) 返回给定的x以及y坐标值的反正切
    cos(x) 余弦
    hypot(x,y) 返回欧几里得范数 sqrt(x*x+y*y)
    sin(x)正弦
    tan(x)正切
    degrees(弧度转角度)
    radians(x)角度转为弧度
    
'''

'''
    字符串：
        %c  格式化字符及其ASCII码
        %s  格式化字符串
        %d  格式化整数
        %u  格式化无符号整数
        %o  格式化无符号八进制
        %x  格式化无符号十六进制
        %X  格式化无符号十六进制大写
        %f  格式化浮点数子，可指定小数点后的精度
        %e  用科学计数法格式化浮点数
        %E  同上
        %g  %f和%e的简写
        %G  
        %p  用十六进制数格式化变量的地址
    
        *
        -
        +
        <sp> 
        #
        0
        %
        (var) 
        m.n. 
        
        
    函数：
        capitalize()  首字符大写
        center(width,fillchar) 居中-距离，填充字符
        count(str,beg=0,end=len(str))  str出现的次数
        byte.dencode(encoding="utf-8",errors="static") 
        encode(encoding="utf-8",errors="static")
        endswith(suffix,beg=0,end=len(str))
        expandtabs(tabsize=8)
        find(str,beg=0,end=len(string))
        index(str,beg=0,end=len(str))
        isalnum()
        isalpha()
        isdigit()
        islower()
        isnumeric()
        isspace()
        istitle()
        isupper()
        join(seq)
        len(str)
        ljust(width[,fillchar])
        lower()
        lstrip()
        maketrans()
        max(str)
        min(str)
        replace(old,new[,max])
        rfind(str,beg=0,end=len(str))
        rindex(str,beg=0,end=len(str))
        rjust(width[,fillchar])
        rstrip()
        split(str="",num=string.count(str))
        splitlines([keepends])
        startswith(substr,beg=0,end=len(str))
        strip([chars])
        swapcase()
        title()
        translate(table,deletechats="")
        upper()
        Zfill(width)
        isdecimal()
        
        
'''

'''
元组
    ()表示 tuple  不可变
    tuple(iterable) 可迭代序列转为元组
    del tup 
    

'''
'''
列表
    []表示
    append 
    del 
    +  *  和字符串类似
    operator模块的eq方法可以比较列表
    list(seq)将元组转为列表
    count(obj )计算个数
    extend(seq)-追加一个序列
    pop（）-顶部删除 
    remove()-尾部删除
    reverse()
    sort(key = None,reverse = false)
    copy()
    clear()
    
    
'''

'''
字典
    {key:value ,key:value }
    dict内建函数创建字典
    key in dict true表示存在
    dict.items() 以列表安徽一个视图对象
    dict.keys() 返回一个视图对象
    dict.values()
    dict1.update(dict2) 把dict2的键值对更新到1中
    popitem() 删除最后一个键值对
    
    
    
'''

'''
集合
    {} 无序不重复的序列
    set() 两种创建方式
    update(xxx) 可以添加多个数据  add()
    discard(xx) 移除，元素不存在不报错，remove 
    pop() 随机删除
    difference() 返回多个集合的差集
    difference_update() 移除集合中交集的元素
    union() 返回两个集合的交集
    issupperset() 判断参数是否是指定的子集
    issubset()
    intersection() 返回集合的交集
    intersction_update() 返回集合的交集
    isdisjoint() 判断两个集合是否包含相同的元素  true/false 
    issubset() 是否是子集
    isuperset() 参数是前面的子集 
'''


'''
迭代器
   访问元素集合的一种方式 
   iter(xx) 创建一个迭代器对象
   next()   获取下一个元素
   
   一个类作为一个迭代器使用需要实现   _iter_()-返回一个迭代器对象,_next_()-返回一个迭代器对象 两个方法
   stopIteration异常用于表示迭代的完成，方式出现无限循环
   else:
      raise StopIteration
      指定触发停止循环
生成器：
    使用了yield的函数被称为生成器(generator)
    返回一个迭代器
    每次遇到yield函数会暂停并保存当前运行信息，返回yield值，并在下一个next方法时，从当前位置继续运行
   
'''
