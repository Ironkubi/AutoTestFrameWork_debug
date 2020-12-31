import time
import pytest


@pytest.fixture(scope="module", autouse=True)
def start(request):
    print('\n----��ʼִ��module----')
    print("module: %s \n----�ص���ҳ---" % request.module.__name__)
    print("----���������----")
    yield
    print("-----�������ԣ�end-----")


@pytest.fixture(scope="function", autouse=True)
def open_home(request):
    print("function: %s \n----�ص���ҳ---" % request.function.__name__)


def test_01():
    print("----����01-----")


def test_02():
    print("----����02-----")


def test_03():
    print("----����03-----")


if __name__ == "__main__":
    pytest.main(["-s", "test_AutoIsTrue.py"])
