# -*-coding:utf-8 -*-
# File : test_Allure_Features.py
# @Time : 2020/12/31 8:40
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


# @allure.feature()用于描述被测试产品需求
@allure.feature('test_module_feature')
def test_01():
    """
    用例描述：在运行 pytest 时添加选项--allure-feature
    pytest tests.py --allure-feature feature1
    """
    assert 0

@allure.feature('test_module_feature')
def test_02():
    """
    用例描述：在运行 pytest 时添加选项--allure-feature
    pytest tests.py --allure-feature feature1
    """
    assert 0 == 0



if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Features.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")
