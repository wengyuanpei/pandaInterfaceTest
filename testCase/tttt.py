# coding=utf-8
import os
import subprocess
from datetime import datetime

COMMAND = "adb shell top"  # 常量
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), "Log")
print(log_path)


class LogcatCathcher(object):
    def __init__(self):
        self.log_file = None
        self.hf = None
        self._create_hf()
        self.p_obj = subprocess.Popen(
            args=COMMAND,
            stdin=None, stdout=self.hf,
            stderr=self.hf, shell=False)

    def _create_hf(self):
        now_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(log_path, "Logcat_" + now_time + ".txt")
        # 因为没指定具体路径，默认就是在当前脚本运行的路径下创建这个log_file
        self.hf = open("%s" % self.log_file, "wb")

    def catch_logcat(self):
        print("Logcat catching...")
        # 持续询问是否需要停止截取
        judgement = input("If you think it is enough, please input Y:")
        while judgement != "Y" and judgement != "y":  # 这里必须是and.
            print("Invalid input, please input Y")
            judgement = input("If you think it is enough, please input Y:")
        else:
            if judgement == "Y" or judgement == "y":  # 如果收到停止Yes信号，则开始结束截取
                self.p_obj.terminate()
                self.p_obj.kill()
                self.hf.close()  # 关闭文件句柄
        return os.path.abspath(self.log_file)


if __name__ == '__main__':
    l_obj = LogcatCathcher()
    print("Logcat log has saved to %s" % l_obj.catch_logcat())
    os.system("pause")
