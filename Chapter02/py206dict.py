# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py206dict.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

if __name__ == '__main__':
    # 1
    print('\n#1')
    zdict = {}
    zdict['w1'] = 'hello'
    zdict['w2'] = 'ziwang.com'
    print('zdict,', zdict)

    # 2
    print('\n#2')
    vdict = {'url1': 'TopQuant.vip'
        , 'url2': 'www.TopQuant.vip'
        , 'url3': 'ziwang.com'}
    print('vdict,', vdict)

    # 3
    print('\n#3')
    s2 = zdict['w1']
    print('s2,', s2)
    s3 = vdict['url2']
    print('s3,', s3)
