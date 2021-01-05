# -*-coding:utf-8 -*-
# File : test_Allure_Testcase.py
# @Time : 2021/1/5 18:54
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os

# https://www.how2xue.com/chat/subject/form/cd33908c9b5940ab9259e0eded5a85ad
# 也可以将作为输入参数，与提供的问题链接模板一起使用。链接模板在 --allure-link-patternPytest 的配置选项中指定，类型与链接模板使用冒号分割，类型可以是 link、issue、testcase
# pytest directory_with_tests/ --alluredir=/tmp/my_allure_report --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
# 以上示例中 allure.issue 的链接地址则为 http://www.mytesttracker.com/issue/140
# 为了将 allure 报告和测试管理系统集成，可以使用 link、issue、testcase
# link(url, link_type, name=None)：提供链接地址
# issue(url, name=None)：提供带有小错误图标的链接
# testcase(url, name=None)：
# issue 和 tescase 其实也是调用的 link，只是 LinkType 不一样，使用以上装饰器将在测试报告的“链接”部分中提供网址的可点击链接
@allure.feature('test_module_testcase')
@allure.story('test_story_01')
@allure.testcase('https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637', 'Test case title')
def test_with_testcase():
    pass



if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Testcase.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")