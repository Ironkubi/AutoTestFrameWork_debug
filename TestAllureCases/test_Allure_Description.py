# -*-coding:utf-8 -*-
# File : test_Allure_Description.py
# @Time : 2021/1/5 18:38
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


@allure.feature("feature_Description")
@allure.story('story_Description')
def test_Description_01():
    """
    用例描述：在测试用例函数声明下方添加
    """
    assert 1


@allure.feature("feature_Description")
@allure.story('story_Description')
@allure.description("测试用例描述信息")
def test_Description_02():
    """
    用例描述：@allure.description() 用于描述用例，支持html显示
    """
    assert 1


@allure.feature('feature_Description')
@allure.story('story_Description')
@allure.description_html("<head></head><body> 测试用例描述信息 </body>")
def test_Description_03():
    """
    用例描述：@allure.description_html(str）：相当于传一个HTML代码组成的字符串，类似allure.attach()中传HTML
    """
    assert 1


@allure.feature('feature_Description')
@allure.story('story_Description')
@allure.description("测试用例描述信息")
def test_Description_04():
    """
    用例描述：使用 allure.dynamic.description() 或 allure.dynamic.description_html() 动态更新描述
    """
    allure.dynamic.description("修改后的测试用例描述信息")
    assert 1


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Description.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")