# -*-coding:utf-8 -*-
# File : test_Allure_Step.py
# @Time : 2021/1/5 18:46
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os

# @allure.step() 用于描述用例步骤
@allure.step("字符串相加：{0}，{1}")
# 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2


@allure.feature('test_module_step')
@allure.story('test_story_01')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_15():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


@allure.step("第一步")
def passing_step():
    pass


@allure.step("第二步")
def step_with_nested_steps():
    nested_step()


@allure.step("第三步")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("第四步{0}，{arg2}")
def nested_step_with_arguments(arg1, arg2):
    pass


# https://www.cnblogs.com/poloyy/p/12716659.html
@allure.feature('test_module_step')
@allure.story('test_story_02')
@allure.step("第五步")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()



@allure.step("打开网站首页")
def open():
    pass

@allure.step("输入账号、密码")
def input_UsernameAndPassWord():
    sendAndClickLogin("xiaoqiang", "1")

@allure.step("输入账号、密码{arg1}，{arg2}，并点击登录")
def sendAndClickLogin(arg1, arg2):
    pass

@allure.feature('test_module_step')
@allure.story('test_story_03')
@allure.step("验证登录过程")
def test_login():
    open()
    input_UsernameAndPassWord()


@allure.feature('test_module_step')
@allure.story('test_story_04')
# @pytest.mark.test 默认走conftest.py
def test_with_fixture_step(conftest_step):
    pass


# https://www.cnblogs.com/se7enjean/p/13513599.html
@allure.step('1、登录')
def login():
    pass

# @allure.epic()
@allure.severity('critical')
@allure.feature('test_module_step')
@allure.story('test_story_05')
@allure.title('用于描述用例名称')
def test_17():
    login()

    # 可以在用例内部编写用例步骤，等同于@allure.step()
    # 步骤必须写在方法内部，注意格式
    with allure.step('1、登录'):
        # allure.attach可以向报告中添加附件
        allure.attach.file('./test.png', " png 图片", allure.attachment_type.PNG)
    pass


if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Step.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")