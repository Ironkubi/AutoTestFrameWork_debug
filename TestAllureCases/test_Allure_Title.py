# -*-coding:utf-8 -*-
# File : test_Allure_Title.py
# @Time : 2021/1/5 18:34
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


# @allure.title() 用于描述用例名称
# https://www.how2xue.com/chat/subject/form/cd33908c9b5940ab9259e0eded5a85ad
"""使用@allure.title 装饰器使测试标题更具可读性"""
@allure.feature('test_module_title')
@allure.story('test_story_01')
@allure.title("This test has a custom title")
def test_09():
    assert 1

# 使用参数占位符获取参数
@allure.feature('test_module_title')
@allure.story('test_story_02')
@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [(2, 2, 4), (1, 2, 5)])
def test_10(param1, param2, expected):
    assert param1 + param2 == expected

@allure.feature('test_module_title')
@allure.story('test_story_03')
@allure.title("This title will be replaced in a test body")
def test_11():
    assert 1
    # 动态更新 title
    allure.dynamic.title('After a successful test finish, the title was replaced with this line.')


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Title.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")