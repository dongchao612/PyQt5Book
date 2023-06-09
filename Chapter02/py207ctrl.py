# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py207ctrl.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

if __name__ == '__main__':
    # 1
    print('\n1,if')
    x, y, z = 10, 20, 5
    if x > y:
        print('x>y')
    else:
        print('x<y')

    # 2
    print('\n#2,elif')
    x, y, z = 10, 20, 5
    if x > y:
        print('x>y')
    elif x > z:
        print('x>z')

    # 3
    print('\n#3,while')
    x = 3
    while x > 0:
        print(x)
        x -= 1

    # 4
    print('\n#4,for')
    xlst = ['1', 'b', 'xxx']
    for x in xlst:
        print(x)

    # 5
    print('\n#5,for')
    for x in range(3):
        print(x)

