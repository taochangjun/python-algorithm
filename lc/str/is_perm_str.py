#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/17 6:58 下午
# @Author  : Thomas
# @File    : 判定是否互为字符重排.py
# @Description: 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

# 示例 1：
#
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
# 示例 2：
#
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-permutation-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # 思路一：排序后比较是否一致即可, nlog(n)
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        return sorted(s1) == sorted(s2)

    def CheckPermutationV2(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        # 空间换时间
        import collections
        m = collections.defaultdict(int)
        for ch in s1:
            m[ch] += 1
        for ch in s2:
            m[ch] -= 1

        for v in m.values():
            if v != 0:
                return False

        return True
