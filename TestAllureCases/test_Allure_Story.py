# -*-coding:utf-8 -*-
# File : test_Allure_Story.py
# @Time : 2020/12/31 9:08
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


@allure.feature('test_module_story')
@allure.story('test_story_01')
def test_03():
    """
    用例描述：在运行 pytest 时添加选项 --allure-stories
    pytest tests.py --allure-stories story1,story_2
    """
    assert 0

@allure.feature('test_module_story')
@allure.story('test_story_02')
def test_04():
    """
    用例描述：在运行 pytest 时添加选项 --allure-stories
    pytest tests.py --allure-stories story1,story_2
    """
    assert 0 == 0



if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Story.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")