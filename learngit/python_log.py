可变参数
def calc(*numbers):      #加*
    sum=0
    for n in numbers:
        sum = sum + n*n
    return sum

print calc(1,2)
print calc(1,2,3)

nums = [1,2,3]
print calc(*nums)       #想用list或tuple，加*



关键字参数
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

person('michael',20)

person('bob',35,city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)



有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2,c=3)----------------------------------------------------------------
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
func(1, 2, 3, 'a', 'b', 'c',x=99)
最神奇的是通过一个tuple和dict，你也可以调用该函数：
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。





slice:
>>> L[0:3]

>>> L[1:3]
['Sarah', 'Tracy']

Ç°11-20¸öÊý£º

>>> L[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Ç°10¸öÊý£¬Ã¿Á½¸öÈ¡Ò»¸ö£º

>>> L[:10:2]
[0, 2, 4, 6, 8]
ËùÓÐÊý£¬Ã¿5¸öÈ¡Ò»¸ö£º

>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]





#iterate

>>> for ch in 'ABC':
...     print ch
...
A
B
C


>>> for i, value in enumerate(['A', 'B', 'C']):
...     print i, value
...
0 A
1 B
2 C


>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print x, y
...
1 1
2 4
3 9





#list comprehension
notice  use []

>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


[1x1, 2x2, 3x3, ..., 10x10]:
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]


>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.iteritems():
...     print k, '=', v
... 
y = B
x = A
z = C

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']


>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']





//生成器
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x104feab40>

>>> g.next()
0
>>> g.next()
1
>>> g.next()
4
>>> g.next()
9
>>> g.next()
16
>>> g.next()
25
>>> g.next()
36
>>> g.next()
49
>>> g.next()
64
>>> g.next()
81
>>> g.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> g = (x * x for x in range(10))
>>> for n in g:
...     print n
...
0
1
4
9
16
25
36
49
64
81



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


使用生成器就像 实例化一个类，用对象调用：
>>> o = odd()
>>> o.next()

//生成器复杂例子
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)

    
注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：

首先调用c.next()启动生成器；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。




注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。
function name is also a var






map reduce in python
#can't filter map or different map

>>> def f(x):
...     return x * x
...
>>> map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]


>>> map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
['1', '2', '3', '4', '5', '6', '7', '8', '9']





//return grammar
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579




filter

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1

filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果: [1, 5, 9, 15]
把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
    return s and s.strip()

filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 结果: ['A', 'B', 'C']



//sort=

>>> sorted([36, 5, 12, 9, 21])
[5, 9, 12, 21, 36]



//sefdef   obey the order of value -1
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

>>> sorted([36, 5, 12, 9, 21], reversed_cmp)
[36, 21, 12, 9, 5]




return function
before
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function sum at 0x10452f668>
调用函数f时，才真正计算求和的结果：

>>> f()
25
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，
内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。

>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：

>>> f1()
9
>>> f2()
9
>>> f3()
9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

>>> def count():
...     fs = []
...     for i in range(1, 4):
...         def f(j):
...             def g():
...                 return j*j
...             return g
...         fs.append(f(i)) #f(i)  -> a j=i, g connect to that j,,each time j is a different j
...     return fs
... 
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9




unnamed function
>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x




由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

>>> def now():
...     print '2013-12-25'
...
>>> f = now
>>> f()
2013-12-25
函数对象有一个__name__属性，可以拿到函数的名字：

>>> now.__name__
'now'
>>> f.__name__
'now'





//decorator



import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)//执行待装饰函数
    return wrapper


@log
def now():
    print '2013-12-25'
~~把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)    now指向了log返回的wrapper,且wrappre改了名字为now

@log('execute')
def now():
    print '2013-12-25'
和两层嵌套的decorator相比，3层嵌套的效果是这样的：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
>>> now = log('execute')(now)




偏函数

关键字函数
>>> int('12345')
12345
但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565









import sys
导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。


#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()

当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

我们可以用命令行运行hello.py看看效果：

$ python hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!
如果启动Python交互环境，再导入hello模块：

$ python
Python 2.7.5 (default, Aug 25 2013, 00:04:04) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>>
导入时，没有打印Hello, word!，因为没有执行test()函数。

调用hello.test()时，才能打印出Hello, word!：

>>> hello.test()
Hello, world!



别名
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
这样就可以优先导入cStringIO。如果有些平台不提供cStringIO，还可以降级使用StringIO。导入cStringIO时，用import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作。

还有类似simplejson这样的库，在Python 2.6之前是独立的第三方库，从2.6开始内置，所以，会有这样的写法：

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5







OO
use object to imp func ,use func to imp class 

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'


如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
>>> bart._Student__name
'Bart Simpson'
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。




多态
def run_twice(animal):
    animal.run()
    animal.run()

>>> run_twice(Dog())
Dog is running...
Dog is running...

>>> run_twice(Animal())
Animal is running...
Animal is running...

>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...

你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思


>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True


>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True


能用type()判断的基本类型也可以用isinstance()判断：

>>> isinstance('a', str)
True
>>> isinstance(u'a', unicode)
True
>>> isinstance('a', unicode)
False
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：

>>> isinstance('a', (str, unicode))
True
>>> isinstance(u'a', (str, unicode))
True


/////////获得对象的所有属性和方法
使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

//获得对象的方法：或属性
//测试对象信息

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81

可以传入一个default参数，如果属性不存在，就返回默认值：

>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404



/////@property
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth
上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。




__slot__
限制绑定
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

>>> class Student(object):
...     pass
...
然后，尝试给实例绑定一个属性：

>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print s.name
Michael
还可以尝试给实例绑定一个方法：

>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25









///动态绑定

//////////给类动态绑定方法：class Student

1MethodType
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = MethodType(set_score, None, Student)

2直写
直接类名.字段 = method
class A（object）:
         pass
#要给A加一个属性score,值为60
A.score=60
这样一来，A的所有实例及A子类的所有实例都有属性score且值为60
这个score可以等于一个方法，比如现在有个方法fuc
  #注意，如果要让这个方法可以被额外赋予到类上，方法的写法必须跟类里面的方法的写法一 致，即第一个参数为self
def fuc(self,arg): 
      print arg
#给类A增加方法fuc
A.score=fuc

3setattr
setattr( A, 'd', 1)
或者
setattr( a1.__class__, 'd', 1)

//////////给实例绑定
1MethodType

>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果25

2 直写
a1 = A()
a1.c = 1
这里我们定义了一个类A，还有一个实例a1。a1.c = 1 只是增加实例的属性而不是增加类的属性。

3setattr(obj, 'y', 19)
setattr似乎只能绑定属性，无法绑定方法
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19


由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性










为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：

>>> class Student(object):
...     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
...
然后，我们试试：

>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'









__iter__ 

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值


__getitem__

要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
现在，就可以按下标访问数列的任意一项了：

>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
573147844013817084101




__getattribute__
rest api





error and debug
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

上面的代码在计算10 / 0时会产生一个除法运算错误：

try...
except: integer division or modulo by zero
finally...
END
从输出可以看到，当错误发生时，后续语句print 'result:', r不会被执行，except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行。然后，程序继续按照流程往下走。


try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print 10 / n
运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行



Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。





//序列化与反序列化jsonJSON
d = dict(name='Bob', age=20, score=88)
import json
json_str=json.dumps(d)
d2=json.loads(json_str)
d2 is a dict
d2['name']


f=open('json','w')
json.dump(d,f)//content recognized
f.close()

f = open('json','r')
d3=json.load(f)
d3 is a dict



def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))





//or
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))



module inside is a func, after import, call that func: module_name.func





//初始数据库

//用connector.connect连接ip：port：user：pwd
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')




//global
如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，
而是 全局 的。我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外的变量赋值的。

你可以使用定义在函数外的变量的值（假设在函数内没有同名的变量）。
然而，我并不鼓励你这样做，并且你应该尽量避免这样做，因为这使得程序的读者会不清楚这个变量是在哪里定义的。
使用global语句可以清楚地表明变量是在外面的块定义的。




//for两个变量
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print i, value
...
0 A
1 B
2 C
上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print x, y
...
1 1
2 4
3 9



When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.

>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():
...     print k, v
...
gallahad the pure
robin the brave




//with
with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。


//ORM

# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='3', name='cina')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
#session.close()





//liao orm


from transwarp.orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()
注意到定义在User类中的__table__、id和name是类的属性，不是实例的属性。所以，在类级别上定义的属性用来描述User对象和表的映射关系，而实例属性必须通过__init__()方法去初始化，所以两者互不干扰：

# 创建实例:
user = User(id=123, name='Michael')
# 存入数据库:
user.insert()




首先要定义的是所有ORM映射的基类Model：

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，所以又可以像引用普通字段那样写：

>>> user['id']
123
>>> user.id
123






class sessionmaker(_SessionClassMethods):
    """A configurable :class:`.Session` factory.

    The :class:`.sessionmaker` factory generates new
    :class:`.Session` objects when called, creating them given
    the configurational arguments established here.

    e.g.::

        # global scope
        Session = sessionmaker(autoflush=False)

        # later, in a local scope, create and use a session:
        sess = Session()

    Any keyword arguments sent to the constructor itself will override the
    "configured" keywords::

        Session = sessionmaker()

        # bind an individual session to a connection
        sess = Session(bind=connection)

    The class also includes a method :meth:`.configure`, which can
    be used to specify additional keyword arguments to the factory, which
    will take effect for subsequent :class:`.Session` objects generated.
    This is usually used to associate one or more :class:`.Engine` objects
    with an existing :class:`.sessionmaker` factory before it is first
    used::

        # application starts
        Session = sessionmaker()

        # ... later
        engine = create_engine('sqlite:///foo.db')
        Session.configure(bind=engine)

        sess = Session()

    .. seealso:

        :ref:`session_getting` - introductory text on creating
        sessions using :class:`.sessionmaker`.

    """

    def __init__(self, bind=None, class_=Session, autoflush=True,
                 autocommit=False,
                 expire_on_commit=True,
                 info=None, **kw):
        """Construct a new :class:`.sessionmaker`.

        All arguments here except for ``class_`` correspond to arguments
        accepted by :class:`.Session` directly.  See the
        :meth:`.Session.__init__` docstring for more details on parameters.

        :param bind: a :class:`.Engine` or other :class:`.Connectable` with
         which newly created :class:`.Session` objects will be associated.
        :param class_: class to use in order to create new :class:`.Session`
         objects.  Defaults to :class:`.Session`.
        :param autoflush: The autoflush setting to use with newly created
         :class:`.Session` objects.
        :param autocommit: The autocommit setting to use with newly created
         :class:`.Session` objects.
        :param expire_on_commit=True: the expire_on_commit setting to use
         with newly created :class:`.Session` objects.
        :param info: optional dictionary of information that will be available
         via :attr:`.Session.info`.  Note this dictionary is *updated*, not
         replaced, when the ``info`` parameter is specified to the specific
         :class:`.Session` construction operation.

         .. versionadded:: 0.9.0

        :param \**kw: all other keyword arguments are passed to the
         constructor of newly created :class:`.Session` objects.

        """
        kw['bind'] = bind
        kw['autoflush'] = autoflush
        kw['autocommit'] = autocommit
        kw['expire_on_commit'] = expire_on_commit
        if info is not None:
            kw['info'] = info
        self.kw = kw
        # make our own subclass of the given class, so that
        # events can be associated with it specifically.
        self.class_ = type(class_.__name__, (class_,), {})    //sessionmaker的make之处

    def __call__(self, **local_kw):
        """Produce a new :class:`.Session` object using the configuration
        established in this :class:`.sessionmaker`.

        In Python, the ``__call__`` method is invoked on an object when
        it is "called" in the same way as a function::

            Session = sessionmaker()
            session = Session()  # invokes sessionmaker.__call__()

        """
        for k, v in self.kw.items():
            if k == 'info' and 'info' in local_kw:
                d = v.copy()
                d.update(local_kw['info'])
                local_kw['info'] = d
            else:
                local_kw.setdefault(k, v)
        return self.class_(**local_kw)       //Session对象执行类的__call__时，即Session(...)时，返回cl_类实例

    def configure(self, **new_kw):
        """(Re)configure the arguments for this sessionmaker.

        e.g.::

            Session = sessionmaker()

            Session.configure(bind=create_engine('sqlite://'))
        """
        self.kw.update(new_kw)

    def __repr__(self):
        return "%s(class_=%r,%s)" % (
            self.__class__.__name__,
            self.class_.__name__,
            ", ".join("%s=%r" % (k, v) for k, v in self.kw.items())
        )


Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)



s1 = Session()

print type(Session)

print type(session)

print type(s1)

# <class 'sqlalchemy.orm.session.sessionmaker'>
# <class 'sqlalchemy.orm.scoping.scoped_session'>
# <class 'sqlalchemy.orm.session.Session'>



//静态方法
既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
从它们的使用上来看,
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。



问题can not assign to function call
user = session.query(User).filter(User.id = user_id)
解决办法
user = session.query(User).filter(User.id == user_id)



//关于实例动态加载的缺点
使用wtf form时
class userform(form):
    name1 = StringField()

user = userform()
user.name2 = StringField()
此时的name2不具有name1的某些属性，属于unbound，不可转化为<imput>,name1可以

在对象上动态添加的属性，不具备某些原生的类的属性的特性
需在类上添加属性，然后再实例化


names = session.query()"alice,bob"
name = name[0]"alice"
userform.name = scjb
不会动态加userform.alice







////元类与动态类，动态加载属性已在前边说明
# http://jianpx.iteye.com/blog/908121



// metaclass的相关知识

This variable can be any callable accepting arguments for name, bases, and dict. 
Upon class creation, the callable is used instead of the built-in type().

metaclass允许你创建类或者修改类
1. what is metaclass?
1.1 在wiki上面，metaclass是这样定义的：In object-oriented programming, 
a metaclass is a class whose instances are classes. 
Just as an ordinary class defines the behavior of certain objects, 
a metaclass defines the behavior of certain classes and their instances.
 
也就是说metaclass的实例化结果是类，而class实例化的结果是instance。我是这么理解的：
metaclass是类似创建类的模板，所有的类都是通过他来create的(调用__new__)，这使得你可以自由的控制
创建类的那个过程，实现你所需要的功能。

如何使用metaclass
2.1 用类的形式
2.1.1 类继承于type, 例如： class Meta(type):pass
2.1.2 将需要使用metaclass来构建class的类的__metaclass__属性（不需要显示声明，直接有的了）赋值为Meta（继承于type的类）



__new__(cls, name, bases, attrs)
cls: 将要创建的类，类似与self，但是self指向的是instance，而这里cls指向的是class
name: 类的名字，也就是我们通常用类名.__name__获取的。
bases: 基类
attrs: 属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）。



























————————————————————————————————————————————————————————————————————————————————————
基本语法补充
  if name[:3] == 'Abc':  


update()方法的语法：
dict.update(dict2)
参数
dict2 -- 这是被添加dict到的词典

#__doc__属性
print type.__doc__


error：RuntimeError: dictionary changed size during iteration

for aname, avalue in attrs.iteritems():
    if aname == "subdict":  # value is a dict{checkgui:checkbox}
        attrs.update(avalue)


'builtin_function_or_method' object has no attribute '__getitem__'
attrs.pop['subdict'] -> attrs.pop('subdict')


//遍历属性

假设你有一个类如
>>> class Cls(object):
...     foo = 1
...     bar = 'hello'
...     def func(self):
...         return 'call me'
...
>>> obj = Cls()

调用Dir的对象返回给您该对象的所有属性，包括Python的特殊属性。虽然有些对象的属性是可赎回的，

等方法。
>>> dir(obj)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar', 'foo', 'func']


你总是可以过滤出特别的方法使用的列表。
>>> [a for a in dir(obj) if not a.startswith('__')]
['bar', 'foo', 'func']

或如果你喜欢

地图/过滤器。
>>> filter(lambda a: not a.startswith('__'), dir(obj))
['bar', 'foo', 'func']


如果你想过滤的方法，你可以使用内置的可作为一个检查。
>>> [a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj,a))]
['bar', 'foo']

你也可以检查你的类及其亲本利用之间的差异。
>>> set(dir(Cls)) - set(dir(object))
set(['__module__', 'bar', 'func', '__dict__', 'foo', '__weakref__'])



//python //groupby




subtasks=http_get_from_server(URL_RUNNING_SUBS)
subtasks = sorted(subtasks,key=lambda x: x['sub_name'] )
for k, group in groupby(subtasks, lambda x: x['sub_name']):
    name_subs[k]=list(group)



//os 读git comment

git_path = r'C:\Users\ypang3\Documents\Work\test-service\1026\AutoTest'
os.path.exists(git_path):
retval = os.getcwd()
os.chdir(git_path)
log = os.popen('git log --pretty=format:"%an,%h,%cr,%cd,%s" -1').read()
os.chdir(retval)