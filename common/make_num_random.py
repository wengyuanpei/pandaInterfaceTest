#生成不重复的随机数字的包


import random

def random_num():
    num_rad = random.sample(range(100000000000000000), 1)
    print(num_rad[0])
    return str(num_rad[0])

if __name__=="__main__":
    random_num()