#!/usr/bin/env python
#coding:utf-8
'''
    新式类和经典类的区别, 多继承代码演示

'''

class A:
    def __init__(self):
        print 'this is A'
    def save(self):
        print 'save method from A'

class B(A):
    def __init__(self):
        print 'this is B'

class C(A):
    def __init__(self):
        print 'this is c'
    def save(self):
        print 'save method from C'

class D(B, C, object):
    def __init__(self):
        print 'this is D'


d = D()
d.save()
