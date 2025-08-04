import os

def requirements_pull():
    # 先获取基础目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 然后拼接路径
    path = os.path.join(base_dir, "config", "requirements.txt")
    cmd="pip freeze > %s" % path
    #导出项目所有依赖
    os.system(cmd)
    return path
if __name__ == '__main__':
    print(requirements_pull())

