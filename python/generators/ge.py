# coding=utf-8

'''
Generators are functions that produces a sequence of results instead of a single sequence.
It generally contains the keyword yield. The main interest of generators compared to a
normal function is to avoid the creation of a list and therefore improve performance (
especially memory).

生成器是一个函数，这个函数接收一个叫yield的函数，这个yield有一些改变程序控制流的特殊本领。
生成器的实现要诀就在于在两个continuation之间来回传递控制流(generator对象和for循环之间)
'''