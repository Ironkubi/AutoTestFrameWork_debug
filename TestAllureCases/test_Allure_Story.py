# -*-coding:utf-8 -*-
# File : test_Allure_Story.py
# @Time : 2020/12/31 9:08
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


@allure.feature('feature_story')
@allure.story('story_01')
def test_story_01():
    """
    用例描述：@allure.story() ,用于描述feature的用户场景，即测试需求
    在运行 pytest 时添加选项 --allure-stories; 如：pytest tests.py --allure-stories story_01
    """
    assert 0 == 0


@allure.feature('feature_story')
@allure.story('story_02')
def test_story_02():
    """
    用例描述：@allure.story() ,用于描述feature的用户场景，即测试需求
    在运行 pytest 时添加选项 --allure-stories; 如：pytest tests.py --allure-stories story_02
    """
    assert 0


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Story.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")