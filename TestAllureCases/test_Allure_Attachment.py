# -*-coding:utf-8 -*-
# File : test_Allure_Attachment.py
# @Time : 2021/1/5 18:48
# @Author : Sf
# version : python 3.7.8
import allure
import pytest
import os



# allure.attach() 用于添加附件
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



if __name__ =="__main__":
    # 执行pytest单元测试，生成 TestAllureCases 报告需要的数据存在 /temp 目录
    pytest.main(["-s", "-q", "test_Allure_Attachment.py", "--alluredir", "./TestAllureCases-Results", "--clean-alluredir"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system("allure generate ./TestAllureCases-Results/ -o ./TestAllureCases-Report/ --clean")