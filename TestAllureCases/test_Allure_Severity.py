# -*-coding:utf-8 -*-
# File : test_Allure_Severity.py
# @Time : 2021/1/5 17:28
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


@allure.feature("feature_severity")
@allure.story("story_severity")
@allure.severity("blocker")
def test_severity_blocker():
    """
    用例描述：@allure.severity() 用于描述用例级别-blocker，阻塞缺陷（功能未实现，无法下一步）
    运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
    如：pytest tests.py --allure-severities normal,critical
    """
    assert 0 == 0


@allure.feature("feature_severity")
@allure.story("story_severity")
@allure.severity("critical")
def test_severity_critical():
    """
    用例描述：@allure.severity() 用于描述用例级别- critical，严重缺陷（功能点缺失）
    运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
    如：pytest tests.py --allure-severities normal,critical
    """
    assert 0 == 0


@allure.feature("feature_severity")
@allure.story("story_severity")
@allure.severity("normal")
def test_severity_normal():
    """
    用例描述：@allure.severity() 用于描述用例级别- normal，一般缺陷（边界情况，格式错误）
    运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
    如：pytest tests.py --allure-severities normal,critical
    """
    assert 0 == 0


@allure.feature("feature_severity")
@allure.story("story_severity")
@allure.severity("minor")
def test_severity_minor():
    """
    用例描述：@allure.severity() 用于描述用例级别- minor，次要缺陷（界面错误与ui需求不符）
    运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
    如：pytest tests.py --allure-severities normal,critical
    """
    assert 0 == 0


@allure.feature("feature_severity")
@allure.story("story_severity")
@allure.severity("trivial")
def test_severity_trivial():
    """
    用例描述：@allure.severity() 用于描述用例级别- trivial，轻微缺陷（必须项无提示，或者提示不规范）
    运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
    如：pytest tests.py --allure-severities normal,critical
    """
    assert 0 == 0


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Severity.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")