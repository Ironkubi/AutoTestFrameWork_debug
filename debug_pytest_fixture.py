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


class Test_A(object):
    @pytest.fixture()
    def before(self):
        print("------->before")
    def test_a(self,before): # ️ test_a方法传入了被fixture标识的函数，已变量的形式
        print("------->test_a")
        assert 1
    def test_b(self,before):
        print("------->test_b")
        assert 1


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


if __name__ == '__main__':
    pytest.main(["-s",  "debug_pytest_fixture.py"])
