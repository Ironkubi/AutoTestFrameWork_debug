# -*-coding:utf-8 -*-
# File : test_Allure_Description.py
# @Time : 2021/1/5 18:38
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


# @allure.description() 用于描述用例，支持html显示
# https://www.how2xue.com/chat/subject/form/cd33908c9b5940ab9259e0eded5a85ad
# @allure.description(str）
# 在测试用例函数声明下方添加""" """
# @allure.description_html(str）：相当于传一个HTML代码组成的字符串，类似allure.attach()中传HTML
# 使用 allure.dynamic.description() 或 allure.dynamic.description_html() 动态更新描述
@allure.feature('test_module_用例描述')
@allure.story('test_story_01')
def test_12():
    """
    测试用例描述信息
    """
    assert 1

@allure.feature('test_module_description')
@allure.story('test_story_02')
@allure.description("测试用例描述信息")
def test_13():
    assert 1

@allure.feature('test_module_description')
@allure.story('test_story_03')
@allure.description_html("<head></head><body> 测试用例描述信息 </body>")
def test_14():
    assert 1

@allure.feature('test_module_description')
@allure.story('test_story_04')
@allure.description("测试用例描述信息")
def test_15():
    allure.dynamic.description("修改后的测试用例描述信息")
    assert 1


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Description.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")