# -*-coding:utf-8 -*-
# File : Allure_Features.py
# @Time : 2020/12/31 8:40
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
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

"""
在运行 pytest 时添加选项 --allure-stories、--allure-feature
pytest tests.py --allure-stories story1,story_2 --allure-feature feature1
"""
@allure.feature('test_module_feature')
def test_01():
    """
    用例描述：Test case 01
    """
    assert 0

@allure.feature('test_module_feature')
def test_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0

@allure.feature('test_module_story')
@allure.story('test_story_01')
def test_03():
    """
    用例描述：Test case 01
    """
    assert 0

@allure.feature('test_module_story')
@allure.story('test_story_02')
def test_04():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


"""
运行指定严重程度的用例，可以在运行 pytest 命令时添加选项--allure-severities
如：pytest tests.py --allure-severities normal,critical
"""
@allure.feature('test_module_severity')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_05():
    """
    用例描述：Test case 01
    """
    assert 0

@allure.feature('test_module_severity')
@allure.story('test_story_01')
@allure.severity('critical')
def test_06():
    """
    用例描述：Test case 02
    """
    assert 0 == 0

@allure.feature('test_module_severity')
@allure.story('test_story_02')
@allure.severity('normal')
def test_07():
    """
    用例描述：Test case 03
    """
    assert 0

@allure.feature('test_module_severity')
@allure.story('test_story_02')
@allure.severity('minor')
def test_08():
    """
    用例描述：Test case 04
    """
    assert 0 == 0



# https://www.how2xue.com/chat/subject/form/cd33908c9b5940ab9259e0eded5a85ad
"""使用@allure.title 装饰器使测试标题更具可读性"""
@allure.feature('test_module_title')
@allure.story('test_story_01')
@allure.title("This test has a custom title")
def test_09():
    assert 1

# 使用参数占位符获取参数
@allure.feature('test_module_title')
@allure.story('test_story_02')
@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [(2, 2, 4), (1, 2, 5)])
def test_10(param1, param2, expected):
    assert param1 + param2 == expected

@allure.feature('test_module_title')
@allure.story('test_story_03')
@allure.title("This title will be replaced in a test body")
def test_11():
    assert 1
    # 动态更新 title
    allure.dynamic.title('After a successful test finish, the title was replaced with this line.')



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

@allure.feature('test_module_用例描述')
@allure.story('test_story_02')
@allure.description("测试用例描述信息")
def test_13():
    assert 1

@allure.feature('test_module_用例描述')
@allure.story('test_story_03')
@allure.description_html("<head></head><body> 测试用例描述信息 </body>")
def test_14():
    assert 1

@allure.feature('test_module_用例描述')
@allure.story('test_story_04')
@allure.description("测试用例描述信息")
def test_15():
    allure.dynamic.description("修改后的测试用例描述信息")
    assert 1



""""""
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
def test_case_10():
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



# https://www.how2xue.com/chat/subject/form/cd33908c9b5940ab9259e0eded5a85ad
# 也可以将作为输入参数，与提供的问题链接模板一起使用。链接模板在 --allure-link-patternPytest 的配置选项中指定，类型与链接模板使用冒号分割，类型可以是 link、issue、testcase
# pytest directory_with_tests/ --alluredir=/tmp/my_allure_report --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
# 以上示例中 allure.issue 的链接地址则为 http://www.mytesttracker.com/issue/140
# 为了将 allure 报告和测试管理系统集成，可以使用 link、issue、testcase
# link(url, link_type, name=None)：提供链接地址
# issue(url, name=None)：提供带有小错误图标的链接
# testcase(url, name=None)：
# issue 和 tescase 其实也是调用的 link，只是 LinkType 不一样，使用以上装饰器将在测试报告的“链接”部分中提供网址的可点击链接

@allure.feature('test_module_link')
@allure.story('test_story_01')
@allure.link('https://www.baidu.com', name='百度一下')
def test_with_link():
    pass

@allure.feature('test_module_issue')
@allure.story('test_story_01')
@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue():
    pass

@allure.feature('test_module_testcase')
@allure.story('test_story_01')
@allure.testcase('https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637', 'Test case title')
def test_with_testcase():
    pass



""""""
# 添加附件
@allure.feature('test_module_attach')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_attachments():
    # 在测试报告中画了一个html页面
    allure.attach('<head></head><body><strong>HTML页面，HelloWorld！</strong> </body>', 'Attach with HTML type',
                  allure.attachment_type.HTML)
    # 添加一个html附件
    # allure.attach.file('./report.html', attachment_type=allure.attachment_type.HTML)
    # 添加一个图片附件
    allure.attach.file('./test.jpg',"图片美女", allure.attachment_type.JPG)


@allure.feature('test_module_attach')
@allure.story('test_story_02')
@allure.severity('blocker')
# @pytest.mark.test
def test_attach():
    allure.attach('A text attacment in module scope fixture', 'text 附件', allure.attachment_type.TEXT)
    # 使用 html 可以方便自定义测试报告
    allure.attach('<head></head><body> a page </body>', " html ", allure.attachment_type.HTML)
    allure.attach.file('./1.png', " png 图片", allure.attachment_type.PNG)
    assert 1

# https://www.cnblogs.com/poloyy/p/12716659.html
# @pytest.fixture
# def attach_file_in_module_scope_fixture_with_finalizer(request):
#     allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)
#
#     def finalizer_module_scope_fixture():
#         allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',
#                       allure.attachment_type.TEXT)
#     request.addfinalizer(finalizer_module_scope_fixture)
#
# def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
#     pass
#
# def test_multiple_attachments():
#     allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
#     allure.attach.file('./reports.html', attachment_type=allure.attachment_type.HTML)


print("1")
# https://www.cnblogs.com/se7enjean/p/13513599.html
@allure.step('1、登录')
def login():
    pass

# @allure.epic()
@allure.severity('critical')
@allure.feature('用于描述被测试产品需求')
@allure.story('用于描述feature的用户场景，即测试需求')
@allure.title('用于描述用例名称')
def test_01():
    login()

    # 可以在用例内部编写用例步骤，等同于@allure.step()
    # 步骤必须写在方法内部，注意格式
    with allure.step('1、登录'):
        # allure.attach可以向报告中添加附件
        allure.attach.file('./test.png', " png 图片", allure.attachment_type.PNG)
    pass


def test02():
    allure.dynamic.severity('critical')
    allure.dynamic.feature('用于描述被测试产品需求')
    allure.dynamic.story('用于描述feature的用户场景，即测试需求')
    allure.dynamic.title('用于描述用例名称')
    allure.dynamic.description('这是用例描述')
    pass



@allure.feature("test_module_class")
class TestAllure:

    def setup(self):
        self.result = None

    def teardown(self):
        desc = "<font color='red'>实际结果:</br> </font>{}".format(self.result)
        allure.dynamic.description(desc)

    @allure.title("测试用例7")
    @allure.description("测试用例1描述")
    def test_case_16(self):
        # print('----------test16---------')
        self.result = "test16"

    @allure.title("测试用例8")
    def test_case_17(self):
        # print('-----------test17-----------')
        self.result = "test17"

    @allure.title("测试用例9")
    def test_case_18(self):
        # print('----------test18------------')
        self.result = "test18"


if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "Allure_Features.py", "--alluredir", "./Allure-Results"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./allure-results/ -o ./Allure-Report/ --clean")
