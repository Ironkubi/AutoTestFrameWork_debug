# -*-coding:utf-8 -*-
# File : test_02.py
# @Time : 2020/12/26 9:09
# @Author : Sf
# version : python 3.7.8
import pytest


def test_02(login):
    print('\n------------------用例文件2测试用例2开始执行------------------')
    print('login after : in test_file_01->case test_01')
    print('-------------------用例文件2测试用例2执行结束------------------------')


if __name__ == "__main__":
    pytest.main(['-vs', 'test_02.py'])