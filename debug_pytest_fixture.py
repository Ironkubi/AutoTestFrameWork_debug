import pytest

"""
 #scope：被标记方法的作用域
 function" (default)：作用于每个测试方法，每个test都运行一次
"class"：作用于整个类，每个class的所有test只运行一次
 "module"：作用于整个模块，每个module的所有test只运行一次
 "session：作用于整个session(慎用)，每个session只运行一次
 params：(list类型)提供参数数据，供调用标记方法的函数使用
 autouse：是否自动运行,默认为False不运行，设置为True自动运行
 """


# class Test_A(object):
#     @pytest.fixture()
#     def before(self):
#         print("------->before")
#     def test_a(self,before): # ️ test_a方法传入了被fixture标识的函数，已变量的形式
#         print("------->test_a")
#         assert 1
#     def test_b(self,before):
#         print("------->test_b")
#         assert 1


# # fixture标记的函数可以应用于测试类外部
# @pytest.fixture()
# def before():
#     print("------->before")
#
# @pytest.mark.usefixtures("before")
# class Test_B(object):
#     def setup(self):
#         print("------->setup")
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#     def test_b(self):
#         print("------->test_b")
#         assert 1


# # 设置为默认运行
# @pytest.fixture(autouse=True)
# def before():
#     print("------->before")
#
# class Test_C(object):
#     def setup(self):
#         print("------->setup")
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#     def test_b(self):
#         print("------->test_b")
#         assert 1


# # 作用域设置为function，自动运行
# import pytest
# @pytest.fixture(scope='function',autouse=True)
# def before():
#     print("------->before")
#
# class Test_D(object):
#     def setup(self):
#         print("------->setup")
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#     def test_b(self):
#         print("------->test_b")
#         assert 1


# # 作用域设置为class，自动运行
# @pytest.fixture(scope='class',autouse=True)
# def before():
#     print("------->before")
#
# class Test_E(object):
#     def setup(self):
#         print("------->setup")
#
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#
#     def test_b(self):
#         print("------->test_b")
#         assert 1


# '''用例传fixture参数
# 方法一：先定义start功能 用例全部传start参数，调用该功能
#
# '''
# @pytest.fixture(scope="function")
# def start(request):
#     print("\n-----开始执行function-----")
#
# def test_a(start):
#     print("-----用例a执行-----")
#
# class Test_aaa():
#     def test_o1(self,start):
#         print("----用例01---------")
#
#     def test_02(self,start):
#         print("----用例02---------")



# '''装饰器usefixtures
# 方法二：使用装饰器@pytest.mark.usefixtures()修饰需要运行的用例
# '''
# @pytest.fixture(scope="function")
# def start():
#     print("\n-----开始执行function------")
#
# @pytest.mark.usefixtures("start")
# def test_a():
#     print("------用例a执行------")
#
# @pytest.mark.usefixtures("start")
# class Test_aaa():
#     def test_01(self):
#         print("------用例01-------")
#
#     def test_02(self):
#         print("------用例02-------")


'''
叠加fixture
如果class用例需要同时调用多个fixture，可以使用@pytest.mark.usefixtures()叠加。注意叠加顺序，先执行的放底层，后执行的放上层
'''

@pytest.fixture(scope="module")
def first():
    print("第一步：操作aaa")

@pytest.fixture(scope="module")
def second():
    print("第二步：操作bbb")

@pytest.mark.usefixtures("second")
@pytest.mark.usefixtures("first")
class TestFix():
    def test_1(self):
        print("用例1")
        assert 1==1

    def test_2(self):
        print("用例2")
        assert 2==2


if __name__ == '__main__':
    pytest.main(["-s",  "debug_pytest_fixture.py"])
