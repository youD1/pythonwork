# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 生成 0 ~ 9 之间的随机数
# 导入 random(随机数) 模块
import random
num = random.randint(0,9)
if num % 2 == 0:
    print("mai")
else:
    print("bumai")