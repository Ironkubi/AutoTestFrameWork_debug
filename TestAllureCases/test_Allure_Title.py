# -*-coding:utf-8 -*-
# File : test_Allure_Title.py
# @Time : 2021/1/5 18:34
# @Author : Sf
# version : python 3.7.8

import allure
import pytest
import os



@allure.feature("feature_title")
@allure.story("story_title_01")
@allure.title("This test has a custom title")
def test_title_01():
    """
    用例描述：@allure.title(), 用于描述用例名称
    """
    assert 1


# 使用参数占位符获取参数
@allure.feature("feature_title")
@allure.story("story_title_02")
@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize("param1,param2,expected", [(2, 2, 4), (1, 2, 5)])
def test_title_02(param1, param2, expected):
    """
    用例描述：@allure.title() 用于描述用例名称，使用参数占位符获取参数
    """
    assert param1 + param2 == expected


@allure.feature("feature_title")
@allure.story("story_title_03")
@allure.title("This title will be replaced in a test body")
def test_title_03():
    """
    用例描述：@allure.title() 用于描述用例名称，动态更新 title
    """
    assert 1
    allure.dynamic.title("After a successful test finish, the title was replaced with this line.")


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Title.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")