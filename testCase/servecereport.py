# -*- coding:utf-8 -*-

import unittest
from testCase.seveceinterfacecase import *
from common.resultPath import *
from BeautifulReport import BeautifulReport as bf



suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(ServeceIterfaceTestCase))

report_path1 = saveReportPath()
report_path = report_path1 + '.html'
run = bf(suite) #实例化BeautifulReport模块
repost_path=saveReportPath()
run.report(filename="听力机定时执行线上环境接口测试报告",description='该报告汇总所有的接口测试',report_dir=r'C:\Users\zhang\Desktop\pandaInterfaceTest\result')



