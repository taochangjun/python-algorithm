#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 5:09 下午
# @Author  : Thomas
# @File    : 判定字符是否唯一.py
# @Description :  实现一个算法，确定一个字符串 s 的所有字符是否全都不同

"""
Python中的位运算符：
    & ： 与
    | :  或
    ^ :  异或（当两个对应位不同时结果位为1）
    ~ :  取反
    << :  左移 （低位移动到高位，相当与 * 2的移动位数次数)
    >> :  右移  (高位移动到低位，相当与 / 2的移动位数次数)

eg:
1 <<  4  :  1 左移4位， 即 1 * (2 ** 4) = 16
"""


class Solution:
    def is_unique(self, astr: str) -> bool:
        mark = 0
        for ch in astr:
            move_bit = ord(ch) - ord('a')
            if mark & (1 << move_bit) != 0:
                return False
            else:
                mark |= 1 << move_bit

        return True

