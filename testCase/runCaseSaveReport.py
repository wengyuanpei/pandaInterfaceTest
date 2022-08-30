import unittest
from pandaInterfaceTest.testCase.interfacecase_for_web import *
from pandaInterfaceTest.common.resultPath import *
from BeautifulReport import BeautifulReport as bf



suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPandaInterface))

report_path1 = saveReportPath()
report_path = report_path1 + '.html'
run = bf(suite) #实例化BeautifulReport模块
repost_path=saveReportPath()
run.report(filename="这是熊猫平板的接口测试报告",description='该报告汇总所有的接口测试',report_dir=repost_path)



