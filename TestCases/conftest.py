# coding=utf-8
# conftest.py
# 1.conftest.py文件名字是固定的，不可以做任何修改
# 2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录
# 3.conftest.py文件所在目录必须存在__init__.py文件
# 4.conftest.py文件不能被其他文件导入
# 5.所有同目录测试文件运行前都会执行conftest.py文件

import pytest
@pytest.fixture()
def login():
    print('\n---------------conftest文件login方法开始执行----------------------------')
    print('login in conftest.py')
    print('----------------conftest.py文件login方法执行结束---------------------------')