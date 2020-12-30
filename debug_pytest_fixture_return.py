import pytest


@pytest.fixture()
def need_data():
    return 2  # 返回数字2


class Test_F(object):
    def test_a(self, need_data):
        print("------->test_a")
        assert need_data != 3  # 拿到返回值做一次断言



@pytest.fixture(params=[1, 2, 3])
def need_data(request):  # 传入参数request 系统封装参数
    return request.param  # 取列表中单个值，默认的取值方式


class Test_G(object):
    def test_a(self, need_data):
        print("------->test_a")
        assert need_data != 3  # 断言need_data不等于3


if __name__ == '__main__':
    pytest.main(["-s",  "debug_pytest_fixture_return.py"])