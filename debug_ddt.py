"""
一般进行接口测试时，每个接口的传参都不止一种情况，一般会考虑正向、逆向等多种组合。所以在测试一个接口时通常会编写多条case，而这些case除了传参不同外，其实并没什么区别。
这个时候就可以利用ddt来管理测试数据，提高代码复用率。
※但要注意：正向和逆向的要分开写※
安装：pip install ddt
四种模式：第一步引入的装饰器 @ ddt；导入数据的 @ data；拆分数据的 @ unpack；导入外部数据的 @ file_data
"""
# 一、读取元组数据

# 一定要和单元测试框架一起用
import unittest, os
from ddt import ddt, data, unpack, file_data


'''NO.1单组元素'''
@ddt
class Testwork(unittest.TestCase):

    @data(1, 2, 3)
    def test_01(self, value):  # value用来接收data的数据
        print(value)


if __name__ == '__main__':
    unittest.main()
# 结果：
# 1
# 2
# 3



'''NO.2多组未分解元素'''
@ddt
class Testwork(unittest.TestCase):

    @data((1, 2, 3), (4, 5, 6))
    def test_01(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
# 结果：
# (1, 2, 3)
# (4, 5, 6)



'''NO.3多组分解元素'''
@ddt
class Testwork(unittest.TestCase):

    @data((1, 2, 3), (4, 5, 6))
    @unpack  # 拆分数据
    def test_01(self, value1, value2, value3):  # 每组数据有3个值，所以设置3个形参
        print(value1)

if __name__ == '__main__':
    unittest.main()
# 结果：
# 1
# 2
# 3
# 4
# 5
# 6

# #############################################################
# 二、读取列表数据
import unittest, os
from ddt import ddt, data, unpack, file_data

'''NO.1单组元素和多组元素未分解都一样,下面看嵌套，考眼力了~'''
@ddt
class Testwork(unittest.TestCase):

    @data([{'name': 'lili', 'age': 12}, {'sex': 'male', 'job': 'teacher'}])
    # @unpack
    def test_01(self, a):
        print(a)


if __name__ == '__main__':
    unittest.main()
# 结果：
# [{'name': 'lili', 'age': 12}, {'sex': 'male', 'job': 'teacher'}]
# ※上面结果可以看出：无法运用到requests数据请求中，所以不是很实用※


'''NO.2多组元素分解'''
@ddt
class Testwork(unittest.TestCase):

    @data([{'name': 'lili', 'age': 12}, {'sex': 'male', 'job': 'teacher'}])
    @unpack
    def test_01(self, a, b):
        print(a, b)


if __name__ == '__main__':
    unittest.main()
# 结果：
# {'name': 'lili', 'age': 12}
# {'sex': 'male', 'job': 'teacher'}
# ※拆分后的运行结果，不带有[]，拆分是将列表中的2个字典拆分，所以有2个数据※


##############################################################
# 3、读取字典数据

import unittest, os
from ddt import ddt, data, unpack, file_data

'''※字典的读取比较特殊，因为在拆分的时候，形参和实参的key值要一致，否则就报错※'''

'''NO.1单组数据'''
@ddt
class Testwork(unittest.TestCase):

    @data({'name': 'lili', 'age': '16'}, {'sex': 'female', 'job': 'nurser'})
    # @unpack
    def test_01(self, a):
        print(a)


if __name__ == '__main__':
    unittest.main()
# 结果：
# {'name': 'lili', 'age': '16'}
# {'sex': 'female', 'job': 'nurser'}
# ※以上运行的结果数据，就可以用来作为requests的请求参数
# ~！※

'''NO.2多数据拆分，重点来了'''
@ddt
class Testwork(unittest.TestCase):

    @data({'name': 'lili', 'age': '16'}, {'name': 'female', 'age': 'nurser'})
    @unpack
    def test_01(self, name, age):
        print(name, age)


if __name__ == '__main__':
    unittest.main()
# 结果：
# lili 16
# female nurser
# ※重点来了：首先结果展示的数据是字典里的value，没有打印key的值；其次 @ data里的数据key值和def方法里的形参
# 名称一定要一致，否则，打印的时候，就会报莫名的参数错误，这里就不做展示，爱学习的同学可以尝试一下
# ~！※

####################################################################
# 4、读取文件数据
import unittest, os
from ddt import ddt, data, unpack, file_data

'''数据格式必须为json，且必须为双引号的键值对形式，如果不是json格式，有列表等其它格式嵌套的话，无论是
否有@unpack，形参和参数数量都要和key值相等'''

@ddt
class testwork(unittest.TestCase):
    testdata = [{'a': 'lili', 'b': 12}, {'a': 'sasa', 'b': 66}]

    @data(*testdata)
    # @unpack
    def test_01(self, value):
        print(value)

    @file_data(os.getcwd() + '/jsonll.txt')
    def test_02(self, value2):
        print(value2)


if __name__ == '__main__':
    unittest.main()
# 结果：
# {'a': 'lili', 'b': 12}
# {'a': 'sasa', 'b': 66}
# nick
# male
# 29