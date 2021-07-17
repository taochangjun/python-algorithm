#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 8:03 下午
# @Author  : Thomas
# @File    : URL化.py
# @Description: URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。

# 示例 1：
#
# 输入："Mr John Smith    ", 13
# 输出："Mr%20John%20Smith"
# 示例 2：
#
# 输入："               ", 5
# 输出："%20%20%20%20%20"
#  
#
# 提示：
#
# 字符串长度在 [0, 500000] 范围内。
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-url-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        # offer消失法。。。
        # 注意replace方法不会改变原始字符串，而是生成一个拷贝
        # return S[:length].replace(' ', '%20')

        # 字符串拼接性能巨差 ！！！
        # res = ""
        # for i in range(length):
        #     res += S[i] if S[i] != ' ' else '%20'
        # return res

        # 字符串join的方式性能要好些
        res = []
        for c in S[:length]:
            if c == ' ':
                c = '%20'
            res.append(c)
        return ''.join(res)
