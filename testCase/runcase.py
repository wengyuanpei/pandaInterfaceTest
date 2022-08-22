import unittest
from pandaInterfaceTest.testCase.interfacecase import *
from pandaInterfaceTest.common.resultPath import *
from BeautifulReport import BeautifulReport as bf



suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestPandaInterface))

report_path1 = saveReportPath()
report_path = report_path1 + '.html'
# fp = open(report_path, 'wb')
# run=HTMLTestReport.HTMLTestRunner(title='接口测试报告', description='接口测试报告,脚本版本号V202208', stream=fp)
# run.run(my_suite)
# fp.close()
run = bf(suite) #实例化BeautifulReport模块
repost_path=saveReportPath()
run.report(filename="test",description='这个描述参数是必填的',report_dir=repost_path)