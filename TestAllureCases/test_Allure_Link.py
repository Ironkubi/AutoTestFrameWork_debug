# -*-coding:utf-8 -*-
# File : test_Allure_Link.py
# @Time : 2021/1/5 18:52
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os


@allure.feature("feature_link")
@allure.story('story_link_01')
@allure.link('https://www.baidu.com', name='百度一下')
def test_link_01():
    """
    为了将 allure 报告和测试管理系统集成，可以使用 link、issue、testcase
    link(url, link_type, name=None)：提供链接地址
    issue(url, name=None)：提供带有小错误图标的链接
    testcase(url, name=None)：
    issue 和 tescase 其实也是调用的 link，只是 LinkType 不一样，使用以上装饰器将在测试报告的“链接”部分中提供网址的可点击链接
    """
    pass


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Link.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")