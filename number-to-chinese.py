#!/usr/local/bin/python
# -*- coding: utf-8 -*-

table = {
    '一':'壹', '二':'貮', '三':'參', '四':'肆', '五':'伍',
    '六':'陸', '七':'柒', '八':'捌', '九':'玖',
    '.':'點',
    '0':'零', '1':'壹', '2':'貮', '3':'參', '4':'肆',
    '5':'伍', '6':'陸', '7':'柒', '8':'捌', '9':'玖',
}

a = raw_input()
for i in table:
    a = a.replace(i, table[i])
print a
