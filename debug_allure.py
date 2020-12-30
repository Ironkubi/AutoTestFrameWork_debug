# coding=utf-8
import allure
import pytest
import time
import os

# @allure.feature()用于描述被测试产品需求
# @allure.story() 用于描述feature的用户场景，即测试需求
# @allure.title() 用于描述用例名称
# @allure.step() 用于描述用例步骤
# @allure.description() 用于描述用例，支持html显示
# allure.attach() 用于添加附件
# @allure.severity() 用于描述用例级别
#
# - blocker　 阻塞缺陷（功能未实现，无法下一步）
# - critical　　严重缺陷（功能点缺失）
# - normal　　 一般缺陷（边界情况，格式错误）
# - minor　 次要缺陷（界面错误与ui需求不符）
# - trivial　　 轻微缺陷（必须项无提示，或者提示不规范）

@allure.feature("Allure测试标签")
class TestAllure:

    def setup(self):
        self.result = None

    def teardown(self):
        desc = "<font color='red'>实际结果:</br> </font>{}".format(self.result)
        allure.dynamic.description(desc)

    @allure.title("测试用例1")
    @allure.description("测试用例1描述")
    def test_01(self):
        print('----------test1---------')
        self.result = "test1"

    @allure.title("测试用例2")
    def test_02(self):
        print('-----------test2-----------')
        self.result = "test2"

    @allure.title("测试用例3")
    def test_03(self):
        print('----------test3------------')
        self.result = "test3"


if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "debug_allure.py", "--alluredir", "./temp"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./temp/ -o ./report/ --clean")
