# -*-coding:utf-8 -*-
# File : debug_pytest-ordering.py
# @Time : 2020/12/30 17:16
# @Author : Sf
# version : python 3.7.8
# test_login.py

# 方式一
# 第一个执行：@ pytest.mark.first
# 第二个执行：@ pytest.mark.second
# 倒数第二个执行：@ pytest.mark.second_to_last
# 最后一个执行：@pytest.mark.last
# 方式二
# 第一个执行：@ pytest.mark.run('first')
# 第二个执行：@ pytest.mark.run('second')
# 倒数第二个执行：@ pytest.mark.run('second_to_last')
# 最后一个执行：@ pytest.mark.run('last')
# 方式三
# 第一个执行：@ pytest.mark.run(order=1)
# 第二个执行：@ pytest.mark.run(order=2)
# 倒数第二个执行：@ pytest.mark.run(order=-2)
# 最后一个执行：@ pytest.mark.run(order=-1)

# pip install pytest-ordering
import pytest

# test_login.py
@pytest.mark.run(order=1)
def test_login02():
    assert 1 == 1

@pytest.mark.run(order=2)
def test_login01():
    assert True


# test_project.py
@pytest.mark.run(order=1)
def test_01():
    assert True

# test_three.py
def test_02():
    assert True


