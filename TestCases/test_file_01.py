# -*-coding:utf-8 -*-
# File : test_file_01.py
# @Time : 2020/12/26 9:08
# @Author : Sf
# version : python 3.7.8
# test_file_01.py
import pytest


def test_01(login):
    print('\n------------------用例文件1测试用例1开始执行------------------')
    print('login after : in test_file_01->case test_01')
    print('-------------------用例文件1测试用例1执行结束------------------------')


if __name__ == "__main__":
    pytest.main(['-vs', 'test_file_01.py'])
