import time, os


def saveReportPath():
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    absPath = os.path.abspath('../result')
    # print('报告创建时间:' + current_time)
    repot_path = os.path.join(absPath, 'interface_report-' + str(current_time))
    # print('测试报告路径：', repot_path)
    return repot_path


