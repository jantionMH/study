#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 冒泡排序

import utils

def bubble_sort(nums: list):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def do(self, func):
        '''todo'''
        for k, v in utils.randoms:
            func(k)
            self.assertEqual(k, v)

    def test_func(self):
        self.do(bubble_sort)

if __name__ == "__main__":
    unittest.main()
