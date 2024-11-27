import unittest
import BeautifulReport

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_01(self):
        '''测试用例01'''
        self.assertEqual(1,1)


    def test_02(self):
        '''测试用例02'''
        self.assertEqual(1,1)

    def test_03(self):
        '''测试用例03'''
        self.assertEqual(1,1)

    def tearDown(self):
        pass

if __name__ == '__main__':


    '''
report （ 文件名 -> 测试报告名称， 如果不指定默认
文件名为report.html
description -> 测试报告用例名称展示
report_dir='.“ -> 报告文件写入路径
theme='theme_default' -> 报告主题样式 theme_default theme_cyan theme_candy theme_memories
)
    '''
    testunit = unittest.TestSuite()
    # 加载用例
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    result = BeautifulReport.BeautifulReport(testunit)
    result.report("第二个测试报告","report1.html")