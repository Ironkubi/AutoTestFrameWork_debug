# -*-coding:utf-8 -*-
# File : conftest.py
# @Time : 2020/12/31 13:40
# @Author : Sf
# version : python 3.7.8
import allure

import pytest

@allure.step
def step_login():
    pass

@pytest.fixture()
def conftest_step():
    step_login()
