# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # 交换变量
    a = 10
    b = 20
    print('交换前 a=%d,b=%d' %(a,b))
    a,b = b,a
    print('交换后 a=%d,b=%d' %(a,b))

    print('---------------------------------')
    for i in range(6):
        print(i)

    print('---------------------------------')
    names = ['raymond', 'rachel', 'matthew', 'roger',
             'betty', 'melissa', 'judith', 'charlie']
    print('join的使用：%s' %('-'.join(names)))

    print('---------------------------------')
    print('序列解包')
    p = 'vttalk', 'female', 30, 'python@qq.com'
    name, gender, age, email = p
    print('name:%s,gender:%s,age:%d,email=%s' %(name,gender,age,email))

