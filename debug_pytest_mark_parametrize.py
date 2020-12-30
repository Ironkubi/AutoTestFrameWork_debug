import pytest


class Test_A(object):
    def setup_class(self):
        print("\n------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a",[3,6]) # a参数被赋予两个值，函数会运行两遍
    def test_a(self,a): # 参数必须和parametrize里面的参数一致
        print("test data:a=%d"%a)
        assert a%3 == 0


class Test_B(object):
    def setup_class(self):
        print("\n------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a,b",[(1,2),(0,3)]) # 参数a,b均被赋予两个值，函数会运行两遍
    def test_a(self,a,b): # 参数必须和parametrize里面的参数一致
        print("test data:a=%d,b=%d"%(a,b))  # 运行第一次取值 a=1,b=2,# 运行第二次取值 a=0,b=3
        assert a+b == 3


def return_test_data():
    return [(1,2),(0,3)]


class Test_C(object):
    def setup_class(self):
        print("\n------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a,b",return_test_data()) # 使用函数返回值的形式传入参数值
    def test_a(self,a,b):
        print("test data:a=%d,b=%d"%(a,b))    # 运行第一次取值 a=1,b=2,# 运行第二次取值 a=0,b=3
        assert a+b == 3


if __name__ == '__main__':
    pytest.main(["-s", "debug_pytest_mark_parametrize.py"])