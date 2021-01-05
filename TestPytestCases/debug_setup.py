# coding=utf-8
import pytest


# 类和方法
def setup_module():
    print("\nsetup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器\n")

def teardown_module():
    print("\nteardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行\n")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')


class TestCase(object):
    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后\n")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')


class Test_ABC(object):
    # 函数级开始
    def setup(self):
        print("setup：每个用例开始前都会执行")
    # 函数级结束
    def teardown(self):
        print("teardown：每个用例结束前都会执行")
    def test_a(self):
        print("正在执行------->test_five")
        assert 1
    def test_b(self):
        print("正在执行------->test_six")


if __name__ == '__main__':
    pytest.main(["-s",  "debug_setup.py"])
