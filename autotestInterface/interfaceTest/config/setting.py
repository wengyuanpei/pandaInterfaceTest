#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'weng'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = BASE_DIR +"\\database\\config.ini"

# 测试用例模板文件
SOURCE_FILE = BASE_DIR+"\\database\\DemoAPITestCase.xlsx"

# excel测试用例结果文件
TARGET_FILE = BASE_DIR+"\\report\\excelReport\\DemoAPITestCase.xlsx"
# 测试用例报告
TEST_REPORT = BASE_DIR+"\\report"
# 测试用例程序文件
TEST_CASE = BASE_DIR+"\\testcase"


