from faker import *

#随机生成请求头
def user_agent():
    fc = Factory.create()
    user_agt=fc.user_agent()
    print(user_agt)
    return user_agt

def phone_num():
    fake=Faker(locale='zh_CN') # 初始化，指定生成中文格式数据
    phone = fake.phone_number()
    return  phone


def manname_num():
    fake = Faker(locale='zh_CN')  # 初始化，指定生成中文格式数据
    name=fake.name()
    return name

def cart_num():
    fake = Faker(locale='zh_CN')
    cart_num=fake.ssn()
    print(cart_num)




if __name__ == '__main__':
    manname_num()
    cart_num()
    user_agent()