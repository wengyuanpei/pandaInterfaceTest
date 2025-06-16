import random



def generate_numbers():

    # 随机生成6个红球号码（1-33之间）
    red_balls = random.sample(range(1, 34), 6)
    # 随机生成1个蓝球号码（1-16之间）
    blue_ball = random.randint(1, 17)
    print('blue_ball',blue_ball)
    return sorted(red_balls) + [blue_ball]



def buy_lottery_ticket():

    # 购买一张双色球彩票，返回彩票号码

    return generate_numbers()



def predict_lottery():

    # 预测下一期双色球中奖号码

    red_balls = random.sample(range(1, 34), 6)

    blue_ball = random.randint(1, 17)
    print('blue_ball', blue_ball)
    return sorted(red_balls) + [blue_ball]


def generate_numbers_check():

    # 随机生成6个红球号码（1-33之间）

    red_balls = random.sample(range(1, 34), 6)

    # 随机生成1个蓝球号码（1-16之间）

    blue_ball = random.randint(1, 17)

    return sorted(red_balls) + [blue_ball]


a=0
while True:
    my_tickt=generate_numbers()
    print("my",set(my_tickt))
    winner=predict_lottery()
    print("winner",set(winner))
    my_tickt_check=generate_numbers_check()
    print("my_tickt_check",my_tickt_check)
    a+=1
    print("预测的第%d次" %a)
    if set(my_tickt)==set(winner)==set(my_tickt_check):
        break